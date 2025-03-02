# coding=UTF-8
#
# SPDX-FileCopyrightText: 2021-2022 Darren <1912544842@qq.com>
#
# SPDX-License-Identifier: Apache-2.0

import argparse
import json
import logging
import os
import platform
import re
import shutil
import subprocess
import sys
import time
import zipfile

import esptool
import toml

import spiffsgen
import luadb

logging.basicConfig(format='- [%(levelname)s]: %(message)s', level=logging.INFO)


def flashFs(fspath, port, baud, chip, offset, size):
    if chip == "esp32c3" or chip == "esp32c3-usb" or chip == "esp32s3":
        if getattr(sys, 'frozen', False):
            bundle_dir = sys._MEIPASS
        else:
            bundle_dir = os.path.dirname(os.path.abspath(__file__))
        # luac
        if os.path.exists('tmp'):
            shutil.rmtree('tmp')
        
        cmd = ""
        if usePlat == "Windows":
            cmd = bundle_dir + "\\bin\\luac_536_32bits.exe -o" + " tmp/"
        elif usePlat == "Linux":
            cmd = bundle_dir + "/bin/luac_536_32bits -o" + " tmp/"
        else:
            pass
        # windows和linux执行luac,mac暂跳过不执行
        if cmd != "":
            os.mkdir('tmp')
            for root, dirs, name in os.walk(fspath):
                for i in range(len(name)):
                    if name[i].endswith(".lua"):
                        cmdd =  cmd + os.path.basename(name[i]) + "c " + fspath + os.path.basename(name[i])
                        a = os.system(cmdd)
                        if a != 0:
                            logging.error("luac failed")
                            sys.exit(-1)
                    # 其他文件直接拷贝
                    else:
                        shutil.copy(fspath + name[i], "tmp/" + os.path.basename(name[i]))
        else:
            shutil.copytree(fspath, "tmp/")

        # 制作fs分区
        if config[chip]["Luadb"]:
            if not luadb.merge("tmp/"):
                logging.error("Luadb merge FAIL!!!")
                sys.exit(-1)
        else:
            with open('script.bin', 'wb') as image_file:
                image_size = int(size, 0)
                spiffs_build_default = spiffsgen.SpiffsBuildConfig(256, spiffsgen.SPIFFS_PAGE_IX_LEN,
                                                                4096, spiffsgen.SPIFFS_BLOCK_IX_LEN, 4,
                                                                32, spiffsgen.SPIFFS_OBJ_ID_LEN,
                                                                spiffsgen.SPIFFS_SPAN_IX_LEN,
                                                                True, True, 'little',
                                                                True, True)
                spiffs = spiffsgen.SpiffsFS(image_size, spiffs_build_default)
                for root, dirs, files in os.walk("tmp/", followlinks=False):
                    for f in files:
                        full_path = os.path.join(root, f)
                        spiffs.create_file('/' + os.path.relpath(full_path, "tmp/").replace('\\', '/'),
                                        full_path)
                image = spiffs.to_binary()
                image_file.write(image)
                image_file.close()
    else:
        logging.error("not support chip")
        sys.exit(-1)

    board = chip
    if board == "esp32c3-usb":
        board = "esp32c3"
    command = ['--port', port,
                '--baud', baud,
                '--chip', board,
                'write_flash',
                offset,
                "script.bin"]
    if config[chip]["Luadb"]:
        command[-2] = config[chip]["LuadbOffset"]
        command[-1] = "disk.fs"
    esptool.main(command)
    # 最后删除临时目录
    shutil.rmtree("tmp")


def pkgRom(chip):
    if chip == "esp32c3" or chip == "esp32c3-usb" or chip == "esp32s3":
        # 查找固件位置
        with open(config['pkg']['Repo'] + '/build/' + "flasher_args.json", 'r', encoding='utf-8') as flash_args:
            j = json.load(flash_args)
            if j['extra_esptool_args']['chip'] != chip and j['extra_esptool_args']['chip']+"-usb" != chip:
                logging.error("The selected chip is inconsistent with the build")
                sys.exit(-1)
            ss = sorted(
                ((o, f) for (o, f) in j['flash_files'].items()),
                key=lambda x: int(x[0], 0),
            )
            flash_args.close()

        # 获取版本信息
        # logging.info("start get version")
        # with open(config['pkg']['Repo'] + 'components/luat/include/luat_base.h', 'r', encoding='utf-8') as f:
        #     for line in f.readlines():
        #         line = line.strip('\n')
        #         if re.match('#define LUAT_VERSION', line):
        #             vc = re.sub('^#define LUAT_VERSION', '', line).strip()
        #             versionCore = re.sub(r'"(?!")', '', vc)
        #             break
        # logging.info("versionCore:{}".format(versionCore))

        with open(config['pkg']['Repo'] + '/components/luat/include/luat_conf_bsp.h', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                line = line.strip('\n')
                if re.match('#define LUAT_BSP_VERSION', line):
                    vb = re.sub('^#define LUAT_BSP_VERSION', '', line).strip()
                    versionBsp = re.sub(r'"(?!")', '', vb)
                    break
                else:
                    versionBsp = "unknown"
            f.close()
        logging.info("versionBsp:{}".format(versionBsp))

        # 判断打包类型
        if not config['pkg']['Release']:
            logging.warning("user build")
            git_sha1 = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).strip()
            firmware_name = "LuatOS-SoC_" + str(chip).upper().replace("-", "_")  + '_' + \
                            git_sha1.decode() + "_" + \
                            time.strftime("%Y%m%d%H%M%S", time.localtime())
        else:
            logging.warning("Release build")
            firmware_name = "LuatOS-SoC_" + versionBsp+ '_'  + str(chip).upper().replace("-", "_") 

        # 进入合并流程
        base_offset = 0x0
        with open("luatos_esp32.bin", "wb") as fout:
            for offset, name in ss:
                fout.write(b"\xff" * (int(offset, 16) - base_offset))
                base_offset = int(offset, 16)
                with open(config['pkg']['Repo'] + '/build/' + name, "rb") as fin:
                    data = fin.read()
                    fout.write(data)
                    base_offset += len(data)
                    fin.close()
            fout.close()

        if config["pkg"]["SocSupport"]:
            if not os.path.exists('tmp'):
                os.mkdir('tmp')
            else:
                shutil.rmtree('tmp')
                os.mkdir('tmp')
            shutil.move("luatos_esp32.bin", 'tmp/')
            shutil.copy(config["pkg"]["Repo"] + "soc_tools/soc_download.exe", 'tmp/')
            if chip == "esp32c3":
                shutil.copy(config["pkg"]["Repo"] + "soc_tools/info_c3.json", 'tmp/')
                os.rename("tmp/info_c3.json","tmp/info.json")
            elif chip == "esp32c3-usb":
                shutil.copy(config["pkg"]["Repo"] + "soc_tools/info_c3_usb.json", 'tmp/')
                os.rename("tmp/info_c3_usb.json","tmp/info.json")
            elif chip == "esp32s3":
                shutil.copy(config["pkg"]["Repo"] + "soc_tools/info_s3.json", 'tmp/')
                os.rename("tmp/info_s3.json","tmp/info.json")
            shutil.copy(config["pkg"]["Repo"] + "components/luat/include/luat_conf_bsp.h", 'tmp/')
            # 改下bsp版本号
            # with open('./tmp/info.json', 'r', encoding='utf-8') as f:
            #     fir_info = json.load(f)
            #     if f['rom']['version-bsp'] != versionBsp:
            #         f['rom']['version-bsp'] = versionBsp
            #         info_j = json.dumps(fir_info)
            #         with open('./tmp/info.json', 'w') as f:
            #             f.write(info_j)
            #             f.close()
            #     else:
            #         pass
            # f.close()
            z = zipfile.ZipFile(firmware_name + ".soc", "w")
            if os.path.isdir("tmp"):
                for d in os.listdir("tmp"):
                    z.write("tmp/" + d, arcname=d)
            z.close()
            shutil.rmtree("tmp")
            config[chip]['Firmware'] = firmware_name + ".soc"
        else:
            os.rename("luatos_esp32.bin", firmware_name + ".bin")
            config[chip]['Firmware'] = firmware_name + ".bin"
        # 写入配置
        with open('config.toml', "w", encoding='utf-8') as f:
            toml.dump(config, f)
            f.close()

    else:
        logging.error("not support chip")
        sys.exit(-1)


def flashRom(rom, port, baud, chip):
    if chip == "esp32c3" or "esp32c3-usb" or chip == "esp32s3":
        if not os.path.isfile(rom):
            logging.error("Firmware not configured")
            sys.exit(-1)
        board = chip
        if board == "esp32c3-usb":
            board = "esp32c3"
        command_erase = ['--chip', board, '--port', port, '--baud', baud, 'erase_flash']
        command = ['--chip', board, '--port', port, '--baud', baud, 'write_flash', '0x0', rom]
        if config["pkg"]["SocSupport"]:
            if not os.path.exists('tmp'):
                os.mkdir('tmp')
            else:
                shutil.rmtree('tmp')
                os.mkdir('tmp')
            zfile = zipfile.ZipFile(config[ChipName]['Firmware'], "r")
            zfile.extractall('./tmp')
            command[-1] = "./tmp/luatos_esp32.bin"
        else:
            pass
        if config[chip]["Type"] == "uart":
            logging.info("select uart flash")
        elif config[chip]["Type"] == "usb":
            logging.info("select usb flash")
            command_erase.remove("--baud")
            command_erase.remove(baud)
            command.remove("--baud")
            command.remove(baud)
        else:
            logging.error("Flash Type error")
            sys.exit(-1)

        logging.info("erase flash")
        esptool.main(command_erase)
        logging.info("start flash firmware")
        esptool.main(command)
        
        if os.path.exists('tmp'):
            shutil.rmtree('tmp')
    else:
        logging.error("not support chip")
        sys.exit(-1)


def get_version():
    return '3.2.0'


if __name__ == '__main__':
    usePlat = platform.system()
    if not os.path.exists("config.toml"):
        logging.error("config.toml not found ,please check")
        sys.exit(-1)
    config = toml.load("config.toml")
    parser = argparse.ArgumentParser(description="ESP32 Flash Tool")
    parser.add_argument('-v', '--version', action='version', version=get_version(), help='Show version')
    parser.add_argument('-t', '--target', help='Chip型号:esp32c3,esp32c3-usb,esp32s3')
    parser.add_argument('-f', '--fs', action="store_true", help='下载脚本')
    parser.add_argument('-r', '--rom', action="store_true", help='下载底层固件')
    parser.add_argument('-p', '--pkg', action="store_true", help='打包固件')
    args = parser.parse_args()

    ChipName = args.target
    if ChipName is None:
        logging.error("未选择chip")
        sys.exit(-1)
    if args.pkg:
        pkgRom(ChipName)
    if args.rom:
        flashRom(config[ChipName]['Firmware'],
                 config[ChipName]['COM'],
                 config[ChipName]['Baud'],
                 ChipName)
    if args.fs:
        if not config[ChipName]['FsPath'].endswith("/"):
            Fspath = config[ChipName]['FsPath'] + "/"
        else:
            Fspath = config[ChipName]['FsPath']
        flashFs(Fspath,
                config[ChipName]['COM'],
                config[ChipName]['Baud'],
                ChipName,
                config[ChipName]['FsOffset'],
                config[ChipName]['FsSize'])

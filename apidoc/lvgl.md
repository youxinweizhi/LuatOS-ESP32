# lvgl - LVGL图像库

## lvgl.scr_act()

获取当前活跃的screen对象

**参数**

|传入值类型|解释|
|-|-|
|return|screen指针|

**返回值**

无

**例子**

```lua
local scr = lvgl.scr_act()


```

---

## lvgl.layer_top()

获取layer_top

**参数**

|传入值类型|解释|
|-|-|
|return|layer指针|

**返回值**

无

**例子**

无

---

## lvgl.layer_sys()

获取layer_sys

**参数**

|传入值类型|解释|
|-|-|
|return|layer指针|

**返回值**

无

**例子**

无

---

## lvgl.scr_load(scr)

载入指定的screen

**参数**

|传入值类型|解释|
|-|-|
|userdata|screen指针|

**返回值**

无

**例子**

```lua
    local scr = lvgl.obj_create(nil, nil)
    local btn = lvgl.btn_create(scr)
    lvgl.obj_align(btn, lvgl.scr_act(), lvgl.ALIGN_CENTER, 0, 0)
    local label = lvgl.label_create(btn)
    lvgl.label_set_text(label, "LuatOS!")
    lvgl.scr_load(scr)

```

---

## lvgl.theme_set_act(name)

设置主题

**参数**

|传入值类型|解释|
|-|-|
|string|主题名称,可选值有 default/mono/empty/material_light/material_dark/material_no_transition/material_no_focus|

**返回值**

|返回值类型|解释|
|-|-|
|bool|成功返回true,否则返回nil|

**例子**

```lua
-- 黑白主题
lvgl.theme_set_act("mono")
-- 空白主题
lvgl.theme_set_act("empty")

```

---

## lvgl.init(w, h, lcd, buff_size, buff_mode)

初始化LVGL

**参数**

|传入值类型|解释|
|-|-|
|int|屏幕宽,可选,默认从lcd取|
|int|屏幕高,可选,默认从lcd取|
|userdata|lcd指针,可选,lcd初始化后有默认值,预留的多屏入口|
|int|缓冲区大小,默认宽*10, 不含色深.|
|int|缓冲模式,默认0, 单buff模式, 可选1,双buff模式|

**返回值**

|返回值类型|解释|
|-|-|
|bool|成功返回true,否则返回false|

**例子**

无

---

## lvgl.anim_create()

创建并初始化一个anim

**参数**

无

**返回值**

|返回值类型|解释|
|-|-|
|userdata|anim指针|

**例子**

```lua
local anim = lvgl.anim_create()

```

---

## lvgl.anim_free(anim)

释放一个anim

**参数**

无

**返回值**

无

**例子**

```lua
local lvgl.anim_free(anim)

```

---

## lvgl.anim_path_t()

创建一个lv_anim_path_t

**参数**

无

**返回值**

|返回值类型|解释|
|-|-|
|userdata|lv_anim_path_t指针|

**例子**

```lua
local anim_path_t = lvgl.anim_path_t()

```

---

## lvgl.anim_path_t_free(anim_path_t)

释放一个lv_anim_path_t

**参数**

无

**返回值**

无

**例子**

```lua
local lvgl.anim_path_t_free(anim_path_t)

```

---

## lvgl.anim_set_path_str(anim, tp)

设置动画路径方式

**参数**

|传入值类型|解释|
|-|-|
|userdata|动画指针|
|string|类型, 支持 linear/ease_in/ease_out/ease_in_out/overshoot/bounce/step|

**返回值**

|返回值类型|解释|
|-|-|
|nil|无返回值|

**例子**

无

---

## lvgl.obj_set_event_cb(obj, func)

设置组件的事件回调

**参数**

|传入值类型|解释|
|-|-|
|userdata|lvgl组件指针|
|func|lua函数, 参数有2个 (obj, event), 其中obj是当前对象, event是事件类型, 为整型|

**返回值**

|返回值类型|解释|
|-|-|
|nil|无返回值|

**例子**

无

---

## lvgl.obj_set_signal_cb(obj, func)

设置组件的信号回调

**参数**

|传入值类型|解释|
|-|-|
|userdata|lvgl组件指针|
|func|lua函数, 参数有2个 (obj, signal), 其中obj是当前对象, signal是信号类型, 为整型|

**返回值**

|返回值类型|解释|
|-|-|
|nil|无返回值|

**例子**

无

---

## lvgl.anim_set_exec_cb(anim, func)

设置动画回调

**参数**

|传入值类型|解释|
|-|-|
|userdata|动画指针|
|userdata|lvgl组件指针|
|func|lua函数, 参数有2个 (obj, value), 其中obj是当前对象, signal是信号类型, 为整型|

**返回值**

|返回值类型|解释|
|-|-|
|nil|无返回值|

**例子**

无

---

## lvgl.anim_set_ready_cb(anim, func)

设置动画回调

**参数**

|传入值类型|解释|
|-|-|
|userdata|动画指针|
|userdata|lvgl组件指针|
|func|lua函数, 参数有1个 (anim), 其中anim是当前对象|

**返回值**

|返回值类型|解释|
|-|-|
|nil|无返回值|

**例子**

无

---

## lvgl.anim_path_set_cb(path, func)

设置动画回调

**参数**

|传入值类型|解释|
|-|-|
|userdata|动画指针|
|userdata|lvgl组件指针|
|func|lua函数, 参数有1个 (path), 其中path是当前对象|

**返回值**

|返回值类型|解释|
|-|-|
|nil|无返回值|

**例子**

无

---

## lvgl.draw_mask_radius_param_t()

创建一个lv_draw_mask_radius_param_t

**参数**

无

**返回值**

|返回值类型|解释|
|-|-|
|userdata|lv_draw_mask_radius_param_t指针|

**例子**

```lua
local radius = lvgl.draw_mask_radius_param_t()

```

---

## lvgl.draw_mask_radius_param_t_free(radius)

释放一个lv_draw_mask_radius_param_t

**参数**

无

**返回值**

无

**例子**

```lua
local lvgl.draw_mask_radius_param_t_free(radius)

```

---

## lvgl.draw_mask_line_param_t()

创建一个lv_draw_mask_line_param_t

**参数**

无

**返回值**

|返回值类型|解释|
|-|-|
|userdata|lv_draw_mask_line_param_t指针|

**例子**

```lua
local line = lvgl.draw_mask_line_param_t()

```

---

## lvgl.draw_mask_line_param_t_free(line)

释放一个lv_draw_mask_line_param_t

**参数**

无

**返回值**

无

**例子**

```lua
local lvgl.draw_mask_line_param_t_free(line)

```

---

## lvgl.draw_mask_fade_param_t()

创建一个lv_draw_mask_fade_param_t

**参数**

无

**返回值**

|返回值类型|解释|
|-|-|
|userdata|lv_draw_mask_fade_param_t指针|

**例子**

```lua
local fade = lvgl.draw_mask_fade_param_t()

```

---

## lvgl.draw_mask_fade_param_t_free(fade)

释放一个lv_draw_mask_fade_param_t

**参数**

无

**返回值**

无

**例子**

```lua
local lvgl.draw_mask_fade_param_t_free(fade)

```

---

## lvgl.font_get(name)

获取内置字体

**参数**

|传入值类型|解释|
|-|-|
|string|字体名称+字号, 例如 opposans_m_10 simsun_48|

**返回值**

|返回值类型|解释|
|-|-|
|userdata|字体指针|

**例子**

```lua

local font = lvgl.font_get("simsun_48")

```

---

## lvgl.font_load(path)

从文件系统加载字体

**参数**

|传入值类型|解释|
|-|-|
|string|字体路径|

**返回值**

|返回值类型|解释|
|-|-|
|userdata|字体指针|

**例子**

```lua
local font = lvgl.font_load("/font_simsun_32.bin")

```

---

## lvgl.font_free(font)

释放字体,慎用!!!仅通过font_load加载的字体允许卸载,通过font_get获取的字体不允许卸载

**参数**

|传入值类型|解释|
|-|-|
|string|字体路径|

**返回值**

|返回值类型|解释|
|-|-|
|userdata|字体指针|

**例子**

```lua
local font = lvgl.font_load("/font_simsun_32.bin")
-- N N N N 操作
-- 确定字体不被使用,不被引用,且内存紧张需要释放
lvgl.font_free(font)

```

---

## lvgl.gif_create(parent, path)

创建gif组件

**参数**

|传入值类型|解释|
|-|-|
|userdata|父组件,可以是nil,但通常不会是nil|
|string|文件路径|

**返回值**

|返回值类型|解释|
|-|-|
|userdata|组件指针,若失败会返回nil,建议检查|

**例子**

```lua
local gif = lvgl.gif_create(scr, "S/emtry.gif")
if gif then
    log.info("gif", "create ok")
end


```

---

## lvgl.gif_restart(gif)

重新播放gif组件

**参数**

|传入值类型|解释|
|-|-|
|userdata|gif组件支持, 由gif_create方法返回|

**返回值**

|返回值类型|解释|
|-|-|
|nil|无返回值|

**例子**

```lua
local gif = lvgl.gif_create(scr, "S/emtry.gif")
if gif then
    log.info("gif", "create ok")
end


```

---

## lvgl.indev_drv_register(tp, dtp)

注册输入设备驱动

**参数**

|传入值类型|解释|
|-|-|
|string|设备类型，当前支持"pointer",指针类/触摸类均可|
|string|设备型号，当前支持"emulator",模拟器类型|

**返回值**

|返回值类型|解释|
|-|-|
|bool|成功返回true,否则返回false|

**例子**

```lua
lvgl.indev_drv_register("pointer", "emulator")

```

---

## lvgl.indev_point_emulator_update(x, y, state)

更新模拟输入设备的坐标数据

**参数**

|传入值类型|解释|
|-|-|
|int|x坐标,以左上角为0,右下角为最大值|
|int|y坐标,以左上角为0,右下角为最大值|
|int|状态, 0 为 释放, 1 为按下|

**返回值**

|返回值类型|解释|
|-|-|
|nil|无返回值|

**例子**

```lua
-- 模拟在屏幕上的点击,通过timeout模拟长按和短按
sys.taskInit(function(x, y, timeout)
    lvgl.indev_point_emulator_update(x, y, 1)
    sys.wait(timeout)
    lvgl.indev_point_emulator_update(x, y, 0)
end, 240, 120, 50)

```

---

## lvgl.qrcode_create(parent, size, dark_color, light_color)

创建qrcode组件

**参数**

|传入值类型|解释|
|-|-|
|userdata|父组件|
|int|长度,因为qrcode是正方形|
|int|二维码中数据点的颜色, RGB颜色, 默认 0x3333ff|
|int|二维码中背景点的颜色, RGB颜色, 默认 0xeeeeff|

**返回值**

|返回值类型|解释|
|-|-|
|userdata|qrcode组件|

**例子**

```lua
-- 创建并显示qrcode
local qrcode = lvgl.qrcode_create(scr, 100)
lvgl.qrcode_update(qrcode, "https://luatos.com")
lvgl.obj_align(qrcode, lvgl.scr_act(), lvgl.ALIGN_CENTER, -100, -100)

```

---

## lvgl.qrcode_update(qrcode, cnt)

设置qrcode组件的二维码内容,配合qrcode_create使用

**参数**

|传入值类型|解释|
|-|-|
|userdata|qrcode组件,由qrcode_create创建|
|string|二维码的内容数据|

**返回值**

|返回值类型|解释|
|-|-|
|bool|更新成功返回true,否则返回false. 通常只有数据太长无法容纳才会返回false|

**例子**

无

---

## lvgl.qrcode_delete(qrcode)

删除qrcode组件

**参数**

|传入值类型|解释|
|-|-|
|userdata|qrcode组件,由qrcode_create创建|

**返回值**

|返回值类型|解释|
|-|-|
|nil|无返回值|

**例子**

无

---

## lvgl.style_t()

创建一个style

**参数**

无

**返回值**

|返回值类型|解释|
|-|-|
|userdata|style指针|

**例子**

```lua
local style = lvgl.style_t()
lvgl.style_init(style)

```

---

## lvgl.style_create()

创建一个style并初始化

**参数**

无

**返回值**

|返回值类型|解释|
|-|-|
|userdata|style指针|

**例子**

```lua
local style = lvgl.style_create()

```

---

## lvgl.style_list_create()

创建一个style_list

**参数**

无

**返回值**

|返回值类型|解释|
|-|-|
|userdata|style指针|

**例子**

```lua
local style = lvgl.style_create()

```

---

## lvgl.style_list_t()

创建一个style_list

**参数**

无

**返回值**

|返回值类型|解释|
|-|-|
|userdata|style指针|

**例子**

```lua
local style = lvgl.style_list_t()

```

---

## lvgl.style_delete(style)

删除style,慎用,通常不会执行删除操作

**参数**

|传入值类型|解释|
|-|-|
|userdata|style指针|

**返回值**

无

**例子**

```lua
local style = lvgl.style_create()
-- ...
-- ...
-- lvgl.style_delete(style)

```

---

## lvgl.style_delete(style)

删除style_list,慎用,通常不会执行删除操作

**参数**

|传入值类型|解释|
|-|-|
|userdata|style指针|

**返回值**

无

**例子**

```lua
local style_list = lvgl.style_list_create()
-- ...
-- ...
-- lvgl.style_list_delete(style_list)

```

---

## lvgl.scr_act()

获取当前活跃的screen对象

**参数**

|传入值类型|解释|
|-|-|
|return|screen指针|

**返回值**

无

**例子**

```lua
local scr = lvgl.scr_act()


```

---

## lvgl.layout_top()

获取layout_top

**参数**

|传入值类型|解释|
|-|-|
|return|layout指针|

**返回值**

无

**例子**

无

---

## lvgl.layout_sys()

获取layout_sys

**参数**

|传入值类型|解释|
|-|-|
|return|layout指针|

**返回值**

无

**例子**

无

---

## lvgl.scr_load(scr)

载入指定的screen

**参数**

|传入值类型|解释|
|-|-|
|userdata|screen指针|

**返回值**

无

**例子**

```lua
lvgl.disp_set_bg_color(nil, 0xFFFFFF)
local scr = lvgl.obj_create(nil, nil)
local btn = lvgl.btn_create(scr)
lvgl.obj_align(btn, lvgl.scr_act(), lvgl.ALIGN_CENTER, 0, 0)
lvgl.label_set_text(label, "LuatOS!")
lvgl.scr_load(scr)

```

---

## lvgl.anim_create()

创建并初始化一个anim

**参数**

无

**返回值**

|返回值类型|解释|
|-|-|
|userdata|anim指针|

**例子**

```lua
local anim = lvgl.anim_create()

```

---

## lvgl.anim_free(anim)

释放一个anim

**参数**

无

**返回值**

无

**例子**

```lua
local lvgl.anim_free(anim)

```

---

## lvgl.anim_set_path_str(anim, tp)

设置动画路径方式

**参数**

|传入值类型|解释|
|-|-|
|userdata|动画指针|
|string|类型, 支持 linear/ease_in/ease_out/ease_in_out/overshoot/bounce/step|

**返回值**

|返回值类型|解释|
|-|-|
|nil|无返回值|

**例子**

无

---

## lvgl.obj_add_event_cb(obj, func)

设置组件的事件回调

**参数**

|传入值类型|解释|
|-|-|
|userdata|lvgl组件指针|
|func|lua函数, 参数有2个 (obj, event), 其中obj是当前对象, event是事件类型, 为整型|

**返回值**

|返回值类型|解释|
|-|-|
|nil|无返回值|

**例子**

无

---

## lvgl.anim_set_exec_cb(anim, func)

设置动画回调

**参数**

|传入值类型|解释|
|-|-|
|userdata|动画指针|
|userdata|lvgl组件指针|
|func|lua函数, 参数有2个 (obj, value), 其中obj是当前对象, signal是信号类型, 为整型|

**返回值**

|返回值类型|解释|
|-|-|
|nil|无返回值|

**例子**

无

---

## lvgl.anim_set_ready_cb(anim, func)

设置动画回调

**参数**

|传入值类型|解释|
|-|-|
|userdata|动画指针|
|userdata|lvgl组件指针|
|func|lua函数, 参数有1个 (anim), 其中anim是当前对象|

**返回值**

|返回值类型|解释|
|-|-|
|nil|无返回值|

**例子**

无

---

## lvgl.draw_mask_radius_param_t()

创建一个lv_draw_mask_radius_param_t

**参数**

无

**返回值**

|返回值类型|解释|
|-|-|
|userdata|lv_draw_mask_radius_param_t指针|

**例子**

```lua
local radius = lvgl.draw_mask_radius_param_t()

```

---

## lvgl.draw_mask_radius_param_t_free(radius)

释放一个lv_draw_mask_radius_param_t

**参数**

无

**返回值**

无

**例子**

```lua
local lvgl.draw_mask_radius_param_t_free(radius)

```

---

## lvgl.draw_mask_line_param_t()

创建一个lv_draw_mask_line_param_t

**参数**

无

**返回值**

|返回值类型|解释|
|-|-|
|userdata|lv_draw_mask_line_param_t指针|

**例子**

```lua
local line = lvgl.draw_mask_line_param_t()

```

---

## lvgl.draw_mask_line_param_t_free(line)

释放一个lv_draw_mask_line_param_t

**参数**

无

**返回值**

无

**例子**

```lua
local lvgl.draw_mask_line_param_t_free(line)

```

---

## lvgl.draw_mask_fade_param_t()

创建一个lv_draw_mask_fade_param_t

**参数**

无

**返回值**

|返回值类型|解释|
|-|-|
|userdata|lv_draw_mask_fade_param_t指针|

**例子**

```lua
local fade = lvgl.draw_mask_fade_param_t()

```

---

## lvgl.draw_mask_fade_param_t_free(fade)

释放一个lv_draw_mask_fade_param_t

**参数**

无

**返回值**

无

**例子**

```lua
local lvgl.draw_mask_fade_param_t_free(fade)

```

---

## lvgl.font_get(name)

获取内置字体

**参数**

|传入值类型|解释|
|-|-|
|string|字体名称+字号, 例如 opposans_m_10 simsun_48|

**返回值**

|返回值类型|解释|
|-|-|
|userdata|字体指针|

**例子**

```lua

local font = lvgl.font_get("simsun_48")

```

---

## lvgl.font_load(path)

从文件系统加载字体

**参数**

|传入值类型|解释|
|-|-|
|string|字体路径|

**返回值**

|返回值类型|解释|
|-|-|
|userdata|字体指针|

**例子**

```lua
local font = lvgl.font_load("/font_simsun_32.bin")

```

---

## lvgl.font_free(font)

释放字体,慎用!!!仅通过font_load加载的字体允许卸载,通过font_get获取的字体不允许卸载

**参数**

|传入值类型|解释|
|-|-|
|string|字体路径|

**返回值**

|返回值类型|解释|
|-|-|
|userdata|字体指针|

**例子**

```lua
local font = lvgl.font_load("/font_simsun_32.bin")
-- N N N N 操作
-- 确定字体不被使用,不被引用,且内存紧张需要释放
lvgl.font_free(font)

```

---

## lvgl.gif_create(parent, path)

创建gif组件

**参数**

|传入值类型|解释|
|-|-|
|userdata|父组件,可以是nil,但通常不会是nil|
|string|文件路径|

**返回值**

|返回值类型|解释|
|-|-|
|userdata|组件指针,若失败会返回nil,建议检查|

**例子**

```lua
local gif = lvgl.gif_create(scr, "S/emtry.gif")
if gif then
    log.info("gif", "create ok")
end


```

---

## lvgl.gif_restart(gif)

重新播放gif组件

**参数**

|传入值类型|解释|
|-|-|
|userdata|gif组件支持, 由gif_create方法返回|

**返回值**

|返回值类型|解释|
|-|-|
|nil|无返回值|

**例子**

```lua
local gif = lvgl.gif_create(scr, "S/emtry.gif")
if gif then
    log.info("gif", "create ok")
end


```

---

## lvgl.indev_drv_register(tp, dtp)

注册输入设备驱动

**参数**

|传入值类型|解释|
|-|-|
|string|设备类型，当前支持"pointer",指针类/触摸类均可|
|string|设备型号，当前支持"emulator",模拟器类型|

**返回值**

|返回值类型|解释|
|-|-|
|bool|成功返回true,否则返回false|

**例子**

```lua
lvgl.indev_drv_register("pointer", "emulator")

```

---

## lvgl.indev_point_emulator_update(x, y, state)

更新模拟输入设备的坐标数据

**参数**

|传入值类型|解释|
|-|-|
|int|x坐标,以左上角为0,右下角为最大值|
|int|y坐标,以左上角为0,右下角为最大值|
|int|状态, 0 为 释放, 1 为按下|

**返回值**

|返回值类型|解释|
|-|-|
|nil|无返回值|

**例子**

```lua
-- 模拟在屏幕上的点击,通过timeout模拟长按和短按
sys.taskInit(function(x, y, timeout)
    lvgl.indev_point_emulator_update(x, y, 1)
    sys.wait(timeout)
    lvgl.indev_point_emulator_update(x, y, 0)
end, 240, 120, 50)

```

---

## lvgl.qrcode_create(parent, size, dark_color, light_color)

创建qrcode组件

**参数**

|传入值类型|解释|
|-|-|
|userdata|父组件|
|int|长度,因为qrcode是正方形|
|int|二维码中数据点的颜色, RGB颜色, 默认 0x3333ff|
|int|二维码中背景点的颜色, RGB颜色, 默认 0xeeeeff|

**返回值**

|返回值类型|解释|
|-|-|
|userdata|qrcode组件|

**例子**

```lua
-- 创建并显示qrcode
local qrcode = lvgl.qrcode_create(scr, 100)
lvgl.qrcode_update(qrcode, "https://luatos.com")
lvgl.obj_align(qrcode, lvgl.scr_act(), lvgl.ALIGN_CENTER, -100, -100)

```

---

## lvgl.qrcode_update(qrcode, cnt)

设置qrcode组件的二维码内容,配合qrcode_create使用

**参数**

|传入值类型|解释|
|-|-|
|userdata|qrcode组件,由qrcode_create创建|
|string|二维码的内容数据|

**返回值**

|返回值类型|解释|
|-|-|
|bool|更新成功返回true,否则返回false. 通常只有数据太长无法容纳才会返回false|

**例子**

无

---

## lvgl.qrcode_delete(qrcode)

删除qrcode组件

**参数**

|传入值类型|解释|
|-|-|
|userdata|qrcode组件,由qrcode_create创建|

**返回值**

|返回值类型|解释|
|-|-|
|nil|无返回值|

**例子**

无

---

## lvgl.style_t()

创建一个style

**参数**

无

**返回值**

|返回值类型|解释|
|-|-|
|userdata|style指针|

**例子**

```lua
local style = lvgl.style_t()
lvgl.style_init(style)

```

---

## lvgl.style_create()

创建一个style并初始化

**参数**

无

**返回值**

|返回值类型|解释|
|-|-|
|userdata|style指针|

**例子**

```lua
local style = lvgl.style_create()

```

---

## lvgl.style_delete(style)

删除style,慎用,通常不会执行删除操作

**参数**

|传入值类型|解释|
|-|-|
|userdata|style指针|

**返回值**

无

**例子**

```lua
local style = lvgl.style_create()
-- ...
-- ...
-- lvgl.style_delete(style)

```

---


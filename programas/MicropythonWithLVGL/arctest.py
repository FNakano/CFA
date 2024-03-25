import watch
watch.hardwareConfig()
import lvgl as lv
arc=lv.arc(lv.screen_active())
arc.set_size(200,200)
arc.center()
arc.set_bg_angles(0,360)
arc.set_rotation(270)  # should not be negative
# arc.set_start_angle(0)
# arc.set_end_angle(90)
arc.set_range(0,12)
arc.set_value(4)
lbl1=lv.label(lv.screen_active())
lbl1.set_style_text_font(lv.font_montserrat_24,0)
lbl1.text='4'
arc.rotate_obj_to_angle(lbl1, 25)
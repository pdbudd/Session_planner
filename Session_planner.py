import dearpygui.dearpygui as dpg
import Places
 

dpg.create_context()
dpg.create_viewport(title='World overview', width=1200, height=900)
with dpg.window(label="Main window"):
    add_place = dpg.add_button(label="Add place", callback=Places.Add_place)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
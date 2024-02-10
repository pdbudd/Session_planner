import dearpygui.dearpygui as dpg

def Save_place(sender, app_data):
    name = dpg.get_value("place_name")
    print(f"Saved place {name}")
    Close()

def Add_place(sender, app_data):
    print(f"sender is: {sender}")
    print(f"app_data is: {app_data}")
    with dpg.window(label="Add place", pos=[100,0], tag="place_window", no_close=True):
        dpg.add_input_text(label="Name of place",parent="Add place",tag="place_name")
        dpg.add_button(label="Save", callback=Save_place)
        dpg.add_button(label="Cancel", callback=Close)

def Close():
    dpg.delete_item("place_window")
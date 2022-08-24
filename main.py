import pyautogui

from WeaponFactoryOOP.core import get_classes_dictionary, create_instance_by_index, Injector
from WeaponFactoryOOP.enums import SlotTypes
from WeaponFactoryOOP.helpers import seed, display_main_menu, display_text_create_menu, list_instances_menu, \
    input_command

list_of_weapon_objects = []
list_of_attachment_objects = []

weapons_library: str = 'class_library_weapons'
attachments_library: str = 'class_library_attachments'
weapons_json_file: str = 'weapons_list.json'
attachments_json_file: str = 'attachments_list.json'


def run():
    create_menu_weapons, class_dict_weapons = get_classes_dictionary(weapons_library)
    create_menu_attachments, class_dict_attachments = get_classes_dictionary(attachments_library)

    seed(list_of_weapon_objects, class_dict_weapons, weapons_json_file)
    seed(list_of_attachment_objects, class_dict_attachments, attachments_json_file)

    # Temporary Test of functionality =========================================

    weapon_args = {
        "manufacture": "CZ",
        "serial_number": "5765fhh5A668",
        "model": "SP-01 SHADOW",
        "weapon_type": "Gun",
        "cal": "9x19",
        "type_of_sight": "fiber optic",
        "series": "75"
    }

    suppressor_args = {
        "model": "SomeModel",
        "slot_type": SlotTypes.BARREL,
        "weight": 5,
        "length": 70,
        "outer_diameter": 20,
        "inner_diameter": 9,
        "cal": "9x19"
    }

    weapon = Injector(class_dict_weapons[2][1], weapon_args, class_dict_attachments[1][1], suppressor_args).init_and_inject_weapon_attachment()
    weapon._make_some_noise()
    list_of_attachment_objects.append(weapon.remove_attachment('barrel'))
    weapon._make_some_noise()


    # ================================================================================

    display_main_menu()

    input_data = input_command((1, 3))

    while input_data != 'stop':
        if input_data == '1':
            # this clear pycharm console - you need to set shortcut for
            # 'clear all' option in preferences, otherwise you have use oc.system() method
            pyautogui.hotkey('ctrl', ';')

            exit_option = display_text_create_menu(create_menu_weapons)

            input_data = input_command((1, exit_option))

            if input_data == str(exit_option):
                pyautogui.hotkey('ctrl', ';')
                display_main_menu()
                continue

            # create instance and return to main menu
            create_instance_by_index(input_data, class_dict_weapons, create_menu_weapons, list_of_weapon_objects)

            pyautogui.hotkey('ctrl', ';')
            input_data = ''
            display_main_menu()

        if input_data == '2':
            # list of instances and operations with them
            list_instances_menu(list_of_weapon_objects)

        if input_data == '3':
            input_data = 'stop'
            print('Have a nice day! Bye! PEW PEW PEW')
            return input_data

        input_data = input_command((1, 3))


if __name__ == '__main__':
    run()

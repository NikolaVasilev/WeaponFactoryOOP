import pyautogui

from WeaponFactoryOOP.helpers import seed, display_main_menu, display_text_create_menu, list_instances_menu, \
    get_classes_dictionary, create_instance_by_index, input_command
from WeaponFactoryOOP.validations import test_input_value, ValueLowError, ValueHighError

# add input validations

list_of_weapon_objects = []


def run():
    create_menu, class_dict = get_classes_dictionary()

    display_main_menu()
    seed(list_of_weapon_objects, class_dict)

    input_data = input_command((1, 3))

    while input_data != 'stop':
        if input_data == '1':
            # this clear pycharm console - you need to set shortcut for
            # 'clear all' option in preferences, otherwise you have use oc.system() method
            pyautogui.hotkey('ctrl', ';')

            exit_option = display_text_create_menu(create_menu)

            input_data = input_command((1, exit_option))

            if input_data == str(exit_option):
                pyautogui.hotkey('ctrl', ';')
                display_main_menu()
                continue

            # create instance and return to main menu
            create_instance_by_index(input_data, class_dict, create_menu, list_of_weapon_objects)

            pyautogui.hotkey('ctrl', ';')
            input_data = ''
            display_main_menu()

        if input_data == '2':
            # list of instances and operations with them
            list_instances_menu(list_of_weapon_objects)

        if input_data == '3':
            input_data = 'stop'
            print('Have a nice day! Bye! PEW PEW PEW ')
            return input_data

        input_data = input("Please make your choice:")


if __name__ == '__main__':
    run()

import pyautogui

from WeaponFactoryOOP.helpers import seed, display_main_menu, display_text_create_menu, list_instances_menu, \
    get_classes_dictionary, create_instance_by_index
from WeaponFactoryOOP.validations import test_input_value, ValueLowError, ValueHighError

# add input validations

list_of_weapon_objects = []


def run():
    create_menu, class_dict = get_classes_dictionary()

    display_main_menu()
    seed(list_of_weapon_objects)

    while True:
        try:
            input_data = input("Please make your choice:")
            test_input_value(input_data, (1, 3))
            break
        except ValueLowError as err:
            print(err.msg)
        except ValueHighError as err:
            print(err.msg)
        except Exception as err:
            print(err)

    while input_data != 'stop':
        if input_data == '1':
            # this clear pycharm console - you need to set shortcut for
            # 'clear all' option in preferences, otherwise you have use oc.system() method
            pyautogui.hotkey('ctrl', ';')

            display_text_create_menu(create_menu)
            input_data = input("Please make your choice:")

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
            print('Have a nice day! Bye!')
            return input_data

        input_data = input("Please make your choice:")


if __name__ == '__main__':
    run()

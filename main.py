import sys
import inspect
import pyautogui
from WeaponFactoryOOP.validations import test_input_value, ValueLowError, ValueHighError
from WeaponFactoryOOP.class_library import Weapon, FireArms, ColdBladedWeapon, Axe, Sword


def get_classes_dictionary():
    cls_members = [member for member in inspect.getmembers(sys.modules[__name__], inspect.isclass) if member[1].__module__ == "WeaponFactoryOOP.class_library"]
    classes = dict()

    for cls in cls_members:
        args = inspect.getfullargspec(cls[1].__init__)[0]
        args.remove('self')
        classes[cls[1].__doc__] = args

    return classes, cls_members


list_of_weapon_objects = []


def display_text_create_menu(class_dict: dict):
    print("You are able to create instance of weapon object. You can chose between:")
    text_options = ''
    for index, key in enumerate(class_dict):
        text_options += f'{index + 1} - {key}\n'
    text_options += f'{len(class_dict) + 1} - Exit'

    return print(text_options)


def display_main_menu():
    return print('You are able to:\n1 - Create a new instance\n2 - To list all instances\n3 - Exit ')


def list_instances_menu():
    pyautogui.hotkey('ctrl', ';')
    # available operations
    print('These are available weapons. You are able to see detailed info by them, choosing the number in front of '
          'them:\n')
    for index, instance in enumerate(list_of_weapon_objects):
        print(f"{index + 1} - {instance}")
    exit_option = len(list_of_weapon_objects) + 1
    print(f"{exit_option} - Return to previous menu")
    input_data = input()
    return


def create_instance(index: str, class_dict: list, create_menu: dict):
    class_instance = class_dict[int(index) - 1][1]

    args = list(create_menu.values())[int(index) - 1]
    class_args = []
    pyautogui.hotkey('ctrl', ';')

    for arg in args:
        input_data = input(f'Please enter value for {arg}:')
        class_args.append(input_data)

    print(len(class_args))
    object_instance = class_instance(*class_args)

    return list_of_weapon_objects.append(object_instance)


# add input validations


def run():
    create_menu, class_dict = get_classes_dictionary()

    display_main_menu()

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
            create_instance(input_data, class_dict, create_menu)

            pyautogui.hotkey('ctrl', ';')
            input_data = ''
            display_main_menu()

        if input_data == '2':
            # list of instances and operations with them
            list_instances_menu()

        if input_data == '3':
            input_data = 'stop'
            return input_data

        input_data = input("Please make your choice:")


if __name__ == '__main__':
    run()

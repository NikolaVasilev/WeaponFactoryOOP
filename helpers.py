import inspect
import json
import sys

import pyautogui

from WeaponFactoryOOP.class_library import Weapon, FireArms, ColdBladedWeapon, Axe, Sword
from WeaponFactoryOOP.validations import test_input_value, ValueLowError, ValueHighError


# class create instance

def seed(list_of_weapon_objects, class_dict):
    with open('WeaponFactoryOOP/weapon_list.json') as file:
        data = json.load(file)

        for weapon_class in data:
            class_name, weapon_objects = list(weapon_class.items())[0]
            instance_weapon_class = [weapon_class for weapon_class in class_dict if weapon_class[0] == class_name][0][1]

            for weapon_object in weapon_objects:
                dto = weapon_object

                instance_object = create_instance(instance_weapon_class, dto)
                list_of_weapon_objects.append(instance_object)

        file.close()
    return list_of_weapon_objects


def input_command(desired_range):
    while True:
        try:
            input_data = input("Please make your choice:")
            test_input_value(input_data, desired_range)
            return input_data
        except ValueLowError as err:
            print(err.msg)
        except ValueHighError as err:
            print(err.msg)
        except Exception as err:
            print(err)


# this should be moved from here
def get_classes_dictionary():
    cls_members = [member for member in inspect.getmembers(sys.modules[__name__], inspect.isclass) if
                   member[1].__module__ == "WeaponFactoryOOP.class_library"]
    classes = dict()

    for cls in cls_members:
        args = inspect.getfullargspec(cls[1].__init__)[0]
        args.remove('self')
        classes[cls[1].__doc__] = args

    return classes, cls_members


# this should be moved from here
def create_instance(class_instance, class_args):
    return class_instance(**class_args)


# this should be moved from here
def create_instance_by_index(index: str, class_dict: list, create_menu: dict, list_of_weapon_objects: list):
    class_instance = class_dict[int(index) - 1][1]

    args = list(create_menu.values())[int(index) - 1]
    pyautogui.hotkey('ctrl', ';')

    weapon_dto = {}

    for arg in args:
        input_data = input(f'Please enter value for {arg}:')
        weapon_dto[arg] = input_data

    object_instance = create_instance(class_instance, weapon_dto)

    return list_of_weapon_objects.append(object_instance)


# unfinished
def display_text_create_menu(class_dict: dict):
    print("You are able to create instance of weapon object. You can chose between:")
    text_options = ''
    exit_option = len(class_dict) + 1
    for index, key in enumerate(class_dict):
        text_options += f'{index + 1} - {key}\n'
    text_options += f'{exit_option} - Exit'
    print(text_options)

    return exit_option


def display_main_menu():
    return print('You are able to:\n1 - Create a new instance\n2 - To list all instances\n3 - Exit ')


# UNFINISHED
def list_instances_menu(list_of_weapon_objects):
    pyautogui.hotkey('ctrl', ';')
    # should implement available operations
    print('These are available weapons. You are able to see detailed info by them, choosing the number in front of '
          'them:\n')
    for index, instance in enumerate(list_of_weapon_objects):
        print(f"{index + 1} - {instance}")
    exit_option = len(list_of_weapon_objects) + 1
    print(f"{exit_option} - Return to previous menu\n")
    input_data = input('Please make your choice:')

    if int(input_data) == exit_option:
        pyautogui.hotkey('ctrl', ';')
        return display_main_menu()

    # call function detailed view by instance of weapon
    return

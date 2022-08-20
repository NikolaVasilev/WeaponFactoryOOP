import inspect
import sys

import pyautogui
from WeaponFactoryOOP.class_library import Weapon, FireArms, ColdBladedWeapon, Axe, Sword


def get_classes_dictionary():
    cls_members = [member for member in inspect.getmembers(sys.modules[__name__], inspect.isclass) if
                   member[1].__module__ == "WeaponFactoryOOP.class_library"]
    classes = dict()

    for cls in cls_members:
        args = inspect.getfullargspec(cls[1].__init__)[0]
        args.remove('self')
        classes[cls[1].__doc__] = args

    return classes, cls_members


def create_instance(class_instance, class_args):
    return class_instance(**class_args)


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

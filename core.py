import inspect
import sys

import pyautogui
from WeaponFactoryOOP.class_library_weapons import Weapon, FireArms, ColdBladedWeapon, Axe, Sword
from WeaponFactoryOOP.class_library_attachment import Suppressor, Muzzle


def get_cls_members(class_library_module):
    return [member for member in inspect.getmembers(sys.modules[__name__], inspect.isclass) if
            member[1].__module__ == class_library_module]


def get_classes_dictionary(class_library):
    if class_library == 'class_library_weapons':
        cls_members = get_cls_members('WeaponFactoryOOP.class_library_weapons')
    else:
        cls_members = get_cls_members('WeaponFactoryOOP.class_library_attachment')

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

    if hasattr(class_instance, '_list_of_attachments'):
        # menu should ask to inject instance which already exist or create new attachment and inject. In option two I
        # will be able to use injector class just for example and I have to add created instances into the list.
        # is_mounted variable should be set it to true. When user unmount attachment, it has to be moved into
        # attribute list and is_mounted should be set it up to false
        pass

    object_instance = create_instance(class_instance, weapon_dto)

    return list_of_weapon_objects.append(object_instance)

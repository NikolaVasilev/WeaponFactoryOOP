import inspect
import sys

import pyautogui
from WeaponFactoryOOP.class_library_weapons import Weapon, FireArms, ColdBladedWeapon, Axe, Sword
from WeaponFactoryOOP.class_library_attachments import Suppressor, Muzzle
from enums import SlotTypes


# this will be useful if we save instances in json or db and load it from there
# should be moved to appropriate modul
class Injector:
    def __init__(self, weapon: type, weapon_args: dict, attribute: type, attribute_args):
        self.attribute_args = attribute_args
        self.attribute = attribute
        self.weapon_args = weapon_args
        self.weapon = weapon

    def init_and_inject_weapon_attachment(self):
        new_weapon = self.weapon(**self.weapon_args)
        new_attachment = self.attribute(**self.attribute_args)
        new_attachment._is_mounted = True
        new_attachment._weapon = f'{new_weapon.weapon_type} "{new_weapon.manufacture}{new_weapon.series} - {new_weapon.model}'
        new_weapon._slot_attachments[str(new_attachment._slot_type)] = new_attachment
        return new_weapon


# Temporary Test of functionality =========================================

gun = FireArms(manufacture='CZ', serial_number='45464', model='SP-01 Shadow', weapon_type='Gun', cal='9x19',
                  type_of_sight='fiber optic', series='75')
sup = Suppressor('some model', 1, 5, 5, 5, 5, '9x19')


# ================================================


def get_cls_members(class_library_module):
    return [member for member in inspect.getmembers(sys.modules[__name__], inspect.isclass) if
            member[1].__module__ == class_library_module]


def get_classes_dictionary(class_library):
    cls_members = get_cls_members(f'WeaponFactoryOOP.{class_library}')

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
        # menu should ask user, to inject instance which already exist or has to create new attachment and inject it. In
        # option two I will be able to use injector class just for example and I have to add created instances into
        # the list. is_mounted variable should be set it to true. When user unmount attachment, it has to be moved
        # into attribute list and is_mounted should be set it up to false
        pass

    object_instance = create_instance(class_instance, weapon_dto)

    return list_of_weapon_objects.append(object_instance)

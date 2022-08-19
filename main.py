import sys
import inspect
import pyautogui
from WeaponFactoryOOP.validations import test_input_value, ValueLowError, ValueHighError


class Weapon:
    """Weapon"""

    def __init__(self, manufacture: str, serial_number: str, weapon_type: str):
        self.weapon_type = weapon_type
        self.serial_number = serial_number
        self.manufacture = manufacture

        self._killable = True

    def base_description(self):
        return f'{self.weapon_type} {self.manufacture} with S/N: {self.serial_number}'

    def __str__(self):
        return f'{self.weapon_type} {self.manufacture}'


class FireArms(Weapon):
    """Firearms"""

    def __init__(self, manufacture: str, serial_number: str, model: str, weapon_type: str, cal: str, type_of_sight: str,
                 series=''):
        self.model = model
        self.type_of_sight = type_of_sight
        self.cal = cal
        self.series = series

        Weapon.__init__(self, manufacture, serial_number, weapon_type)

    def description(self):
        return f'{self.weapon_type} "{self.manufacture}{self.series} - {self.model}" is "{self.cal}" caliber and have a {self.type_of_sight} type of sight '


class ColdBladedWeapon(Weapon):
    """Cold Bladed Weapon"""

    def __init__(self, manufacture: str, serial_number: str, weapon_type: str, blade_type: str, blade_dimensions: dict):
        self.blade_dimensions = blade_dimensions
        self.blade_type = blade_type

        Weapon.__init__(self, manufacture, serial_number, weapon_type)

    def __blade_dimensions_as_string(self):
        return f"{self.blade_dimensions['blade_length']}x{self.blade_dimensions['blade_height']}"

    def description(self):
        return f"This {self.weapon_type} is manufactured by {self.manufacture} with S/N: {self.serial_number}. It has {self.blade_type} blade with {self.__blade_dimensions_as_string()}mm dimensions"

    def __str__(self):
        return f'This {self.weapon_type} is manufactured by {self.manufacture}'


class Axe(ColdBladedWeapon):
    """Axe"""

    def __init__(self, manufacture: str, serial_number: str, weapon_type: str, blade_type: str, blade_dimensions: dict):
        ColdBladedWeapon.__init__(self, manufacture, serial_number, weapon_type, blade_type, blade_dimensions)

    def description(self):
        return f"This {self.weapon_type} is manufactured by {self.manufacture} with S/N: {self.serial_number}. It has {self.blade_type} blade with {self.blade_dimensions['blade_length']}mm length"


class Sword(ColdBladedWeapon):
    """Sword"""

    def __init__(self, manufacture: str, serial_number: str, weapon_type: str, blade_type: str, blade_dimensions: dict):
        ColdBladedWeapon.__init__(self, manufacture, serial_number, weapon_type, blade_type, blade_dimensions)

    def description(self):
        return f"This {self.weapon_type} is manufactured by {self.manufacture} with S/N: {self.serial_number}. It has {self.blade_type} blade with {self.blade_dimensions['blade_length']}mm length"


def get_classes_dictionary():
    cls_members = inspect.getmembers(sys.modules[__name__], inspect.isclass)
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
    print('These are available weapons you can see detailed info by choosing the number in front of them:\n')
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
    object_instance = class_instance(*class_args)

    return list_of_weapon_objects.append(object_instance)


# input validations


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
    # validate_input(input_data)

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

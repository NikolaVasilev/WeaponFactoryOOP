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

    def __init__(self, manufacture: str, serial_number: str, model: str, weapon_type: str, cal: str, type_of_sight: str, series=''):
        self.model = model
        self.type_of_sight = type_of_sight
        self.cal = cal
        self.series = series
        # TODO add and remove methods, I also have to add implementation of injector class for attachments(suppressors,
        #  muzzles and others.)

        Weapon.__init__(self, manufacture, serial_number, weapon_type)

    _list_of_attachments = []

    def description(self):
        return f'{self.weapon_type} "{self.manufacture}{self.series} - {self.model}" is "{self.cal}" caliber and have a {self.type_of_sight} type of sight '

    def _make_some_noise(self):
        print('PEW PEW PEW PEW') if not self._list_of_attachments else print('sup sup sup .... :D')
        return self


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

    def _make_some_noise(self):
        print('KLUC KLUC KLUC KLUC......')
        return self

    def __str__(self):
        return f'This {self.weapon_type} is manufactured by {self.manufacture}'


class Axe(ColdBladedWeapon):
    """Axe"""

    def __init__(self, manufacture: str, serial_number: str, weapon_type: str, blade_type: str, blade_dimensions: dict):
        ColdBladedWeapon.__init__(self, manufacture, serial_number, weapon_type, blade_type, blade_dimensions)

    def description(self):
        return f"This {self.weapon_type} is manufactured by {self.manufacture} with S/N: {self.serial_number}. It has {self.blade_type} blade with {self.blade_dimensions['blade_length']}mm length"

    def _make_some_noise(self):
        print('TUP HRUC KLUC TUP.....Your head is rolling.:D')
        return self


class Sword(ColdBladedWeapon):
    """Sword"""

    def __init__(self, manufacture: str, serial_number: str, weapon_type: str, blade_type: str, blade_dimensions: dict):
        ColdBladedWeapon.__init__(self, manufacture, serial_number, weapon_type, blade_type, blade_dimensions)

    def description(self):
        return f"This {self.weapon_type} is manufactured by {self.manufacture} with S/N: {self.serial_number}. It has {self.blade_type} blade with {self.blade_dimensions['blade_length']}mm length"

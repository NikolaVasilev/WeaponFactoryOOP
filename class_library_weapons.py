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

    _slot_attachments = {
        'barrel': None,
        'under_barrel': None,
        'sight': None
    }

    def _is_slot_empty(self, type_of_slot: str):
        return True if self._slot_attachments[type_of_slot] is None else False

    def description(self):
        return f'{self.weapon_type} "{self.manufacture}{self.series} - {self.model}" is "{self.cal}" caliber and have a {self.type_of_sight} type of sight '

    def _make_some_noise(self):
        print('sup sup sup .... :D') if not self._is_slot_empty('barrel') and (
                self._slot_attachments['barrel'].__doc__ == 'Suppressor') else print('PEW PEW PEW PEW')
        return self

    def remove_attachment(self, attachment: str):
        self._slot_attachments[attachment]._is_mounted = False
        weapon_attachment = self._slot_attachments[attachment]
        self._slot_attachments[attachment] = None
        return weapon_attachment


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

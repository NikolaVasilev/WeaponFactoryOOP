from abc import ABC, abstractmethod

from WeaponFactoryOOP.enums import SlotTypes


class Base(ABC):
    def __init__(self, type: str, model: str, slot_type: SlotTypes, weight: float, length: float, outer_diameter: float,
                 inner_diameter: float, cal: str):
        self._type = type
        self._model = model
        self._weight = weight
        self._length = length
        self._outer_diameter = outer_diameter
        self._inner_diameter = inner_diameter
        self._cal = cal
        self._slot_type = slot_type
        self._is_mounted = False

    @abstractmethod
    def _base_description(self):
        pass

    @abstractmethod
    def _is_mounted_as_string(self):
        pass


class Attachment(Base):
    def __init__(self, type, model, slot_type, weight, length, outer_diameter, inner_diameter, cal):
        super().__init__(type, model, slot_type, weight, length, outer_diameter, inner_diameter, cal)

    _weapon = ''

    def _base_description(self):
        return ''

    def _is_mounted_as_string(self):
        text = f'The {self._type} {self._model} is mounted' if self._is_mounted else f'The {self._type} {self._model} is not mounted '
        if self._weapon:
            text = f'{text} on {self._weapon}'
        return text


class Suppressor(Attachment):
    """Suppressor"""

    def __init__(self, model, slot_type, weight, length, outer_diameter, inner_diameter, cal):
        super().__init__(self.__doc__, model, slot_type, weight, length, outer_diameter, inner_diameter, cal)


class Muzzle(Attachment):
    """Muzzle"""

    def __init__(self, model, slot_type, weight, length, outer_diameter, inner_diameter, cal):
        super().__init__(self.__doc__, model, slot_type, weight, length, outer_diameter, inner_diameter, cal)

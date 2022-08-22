from abc import ABC, abstractmethod


class Base(ABC):
    def __init__(self, type: str, model: str, weight: float, length: float, outer_diameter: float,
                 inner_diameter: float, cal: str):
        self._type = type
        self._model = model
        self._weight = weight
        self._length = length
        self._outer_diameter = outer_diameter
        self._inner_diameter = inner_diameter
        self._cal = cal
        self._is_mounted = False

    @abstractmethod
    def _base_description(self):
        pass

    @abstractmethod
    def _is_mounted_as_string(self):
        pass


class Attachment(Base):
    def __init__(self, type, model, weight, length, outer_diameter, inner_diameter, cal):
        super().__init__(type, model, weight, length, outer_diameter, inner_diameter, cal)

    def _base_description(self):
        return ''

    def _is_mounted_as_string(self):
        return f'The {self._type} {self._model} is mounted' if self._is_mounted else f'The {self._type} {self._model} is not mounted'


class Suppressor(Attachment):
    """Suppressor"""

    def __init__(self, model, weight, length, outer_diameter, inner_diameter, cal):
        super().__init__(self.__doc__, model, weight, length, outer_diameter, inner_diameter, cal)


class Muzzle(Attachment):
    """Muzzle"""

    def __init__(self, model, weight, length, outer_diameter, inner_diameter, cal):
        super().__init__(self.__doc__, model, weight, length, outer_diameter, inner_diameter, cal)
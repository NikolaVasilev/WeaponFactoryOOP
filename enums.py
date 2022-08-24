from enum import Enum


class SlotTypes(Enum):
    BARREL = 1
    UNDER_BARREL = 2
    SIGHT = 3

    def __str__(self):
        return f'{self.name.lower()}'

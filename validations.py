class ValueHighError(Exception):
    def __init__(self, msg, value):
        self.msg = msg
        self.value = value


class ValueLowError(Exception):
    def __init__(self, msg, value):
        self.msg = msg
        self.value = value


def test_input_value(value: str, desired_range: tuple):
    if int(value) < desired_range[0]:
        print('ok')
        raise ValueLowError(
            f'Error: {value} is not in presented options! Should be between {desired_range[0]} and {desired_range[1]}',
            value)

    if int(value) > desired_range[1]:
        raise ValueLowError(
            f'Error: {value} is not in presented options! The number should be between {desired_range[0]} and {desired_range[1]}',
            value)

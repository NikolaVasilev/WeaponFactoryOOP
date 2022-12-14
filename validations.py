import random


class ValueHighError(Exception):
    def __init__(self, msg, value):
        self.msg = msg
        self.value = value


class ValueLowError(Exception):
    def __init__(self, msg, value):
        self.msg = msg
        self.value = value


def test_input_value(value: str, desired_range: tuple):
    try:
        int(value)
    except ValueError as e:
        raise Exception(random_error_msg(value)) from e

    if int(value) < desired_range[0]:
        raise ValueLowError(
            f'Error: {value} is not in presented options! Should be between {desired_range[0]} and {desired_range[1]}',
            value)

    if int(value) > desired_range[1]:
        raise ValueLowError(
            f'Error: {value} is not in presented options! The number should be between {desired_range[0]} and {desired_range[1]}',
            value)


def random_error_msg(value):
    msg = [
        f"Error: This '{value}' should be number not a string!",
        f"Error: Why you wouldn't understand '{value}' should be number not a string!",
        f"Error: Dude are you fucking stupid? Why you wouldn't understand '{value}' should be number not a string!",
    ]
    return random.choice(msg)

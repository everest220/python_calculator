# Function for calculating the remainder of a division
def remainder_integer_division(dividend: int, divider: int):
    result = dividend // divider
    remainder = dividend - (divider * result)
    return remainder


def multiple_number(number_to_test: int, multiple_to_use: int):
    if remainder_integer_division(number_to_test, multiple_to_use) == 0:
        return True
    else:
        return False




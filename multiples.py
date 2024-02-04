# Function for calculating the remainder of a division
def remainder_integer_division(dividend: int, divider: int):
    result = dividend // divider
    remainder = dividend - (divider * result)
    return remainder


# Another Function checking that a number is even
def even_number(number_to_test: int):
    if remainder_integer_division(number_to_test, 2) == 0:
        return True
    else:
        return False

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


def is_prime_number(number_to_test: int):
    for multiple_to_use in range(2, number_to_test - 1):
        result = multiple_number(number_to_test, multiple_to_use)
        if result == True:
            return False
    # La boucle for est terminée. Tous les nombres ont été testés et on n'est jamais sorti de la fonction.
    return True

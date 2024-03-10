import multiples
limit_to_display = input("Donne la limite des nombres premiers à afficher : ")
limit_to_display_int = int(limit_to_display)
for numbers_to_test in range(1, limit_to_display_int):
    result = multiples.is_prime_number(numbers_to_test)
    if result == True:
        print(numbers_to_test)

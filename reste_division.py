def reste_division_entiere(dividende: int, diviseur: int):
    quotient = dividende // diviseur
    reste = dividende - (diviseur * quotient)
    return reste

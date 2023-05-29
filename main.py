"""Módulo com funções."""


def is_prime(number: int) -> bool:
    """Retorna True se o número for primo e False caso contrário."""
    if number <= 1:
        return None
    elif number >= 2:
        eh_primo = True
        for i in range (2, int(number**0.5) + 1):
            if number % i == 0:
                eh_primo = False
            break
    if eh_primo:
        return True
    else:
        return False


def list_prime_factors(number: int) -> list[int]:
    """Retorna uma lista com os fatores primos de cada número da lista fornecida."""
    fatores = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            fatores.append(divisor)
            number /= divisor
        else:
            divisor += 1
    return fatores

  

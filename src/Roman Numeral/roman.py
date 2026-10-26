__author__ = 'smelnyk'

ROMAN_VALUES = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'),
]

ROMAN_SYMBOLS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def get_roman_numeral(number):
    """Retorna o numeral romano correspondente ao inteiro positivo informado."""
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError(
            "The value you entered is invalid: {num} is not a positive integer.".format(num=number))

    if number <= 0:
        raise TypeError(
            "The number you entered is invalid: {num} is not a positive integer.".format(num=number))

    numeral = ''
    for value, symbol in ROMAN_VALUES:
        while number >= value:
            numeral += symbol
            number -= value
    return numeral


def get_number_from_roman_numeral(numeral):
    """Retorna o inteiro correspondente ao numeral romano informado (aceita minusculas)."""
    if not isinstance(numeral, str) or numeral.strip() == '':
        raise ValueError("The value you entered is invalid: {num} is not a roman numeral.".format(num=numeral))

    numeral = numeral.upper()
    if any(letter not in ROMAN_SYMBOLS for letter in numeral):
        raise ValueError("The value you entered is invalid: {num} is not a roman numeral.".format(num=numeral))

    total = 0
    for i, letter in enumerate(numeral):
        value = ROMAN_SYMBOLS[letter]
        if i + 1 < len(numeral) and value < ROMAN_SYMBOLS[numeral[i + 1]]:
            total -= value
        else:
            total += value
    return total
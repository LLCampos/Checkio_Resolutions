def arabic_to_roman(arabic):
    """This is best explained with an example.

    Consider the number 76. The algorithm checks which is the biggest number
    of the numbers that have special symbols in roman numerals
    (arabic_to_roman_dict) and that can be subtracted to 76 without
    returning a negative value. In this case, this number is 50.

    So the first digit of roman numeral correspondent to 76 is 'L', which stands
    for 50 in roman numerals.

    We repeat the process for the result of the subtraction of 76 and 50,
    that is, 26, and so on until we get 0 as a result of a subtraction, in which
    case, we already have the complete roman numeral of 76."""

    roman = ''

    arabic_to_roman_dict = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }

    key_arabic_numbers = sorted(arabic_to_roman_dict.keys(), reverse=True)

    while arabic != 0:
        for number in key_arabic_numbers:
            if arabic - number >= 0:
                arabic -= number
                roman += arabic_to_roman_dict[number]
                break
    return roman


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert arabic_to_roman(6) == 'VI', '6'
    assert arabic_to_roman(76) == 'LXXVI', '76'
    assert arabic_to_roman(499) == 'CDXCIX', '499'
    assert arabic_to_roman(3888) == 'MMMDCCCLXXXVIII', '3888'

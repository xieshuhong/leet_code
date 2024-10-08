def intToRoman(num: int) -> str:
    roman_numerals = [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1)
    ]
    result = []
    
    for symbol, value in roman_numerals:
        count = num // value
        if count > 0:
            result.append(symbol*count)
            num = num % value
            
    return ''.join(result)
    

s = 1994
print(intToRoman(1994))
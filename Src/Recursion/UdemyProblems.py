#Problem -- 1 (Power of Number)
def powerOfNumber(number:int, power:int):
    if power == 0:
        return 1
    elif power == 1:
        return number
    else:
        return number * powerOfNumber(number,power - 1);

print(powerOfNumber(5,10))


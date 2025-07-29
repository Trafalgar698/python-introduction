def fizzbuzz(number: int) -> str:
    if number %3 == 0 or '3' in str(number):
        return "Fizz"
    elif number %5 == 0 or '5' in str(number):
        return "Buzz"


    return str(number)
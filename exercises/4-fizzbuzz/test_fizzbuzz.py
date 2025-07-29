from src import fizzbuzz

def test_1_should_be_1():
    assert fizzbuzz(1) == '1'

def test_2_should_be_2():
    assert fizzbuzz(2) == '2'

def test_3_should_be_Fizz():
    assert fizzbuzz(3) == 'Fizz'

def test_5_should_be_Buzz():
    assert fizzbuzz(5) == 'Buzz'

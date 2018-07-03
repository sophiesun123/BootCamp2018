# test_smallest_factor.py

import pytest
import UnitTesting as ut

# Problem 1
def test_smallest_factor():
	assert ut.smallest_factor(1) == 1, "1 doesn't work"
	assert ut.smallest_factor(2) == 2, "2 doesn't work"
	assert ut.smallest_factor(4) == 2, "4 doesn't work" 
	assert ut.smallest_factor(5) == 5, "5 doesn't work"
	assert ut.smallest_factor(6) == 2, "6 doesn't work" 
	assert ut.smallest_factor(15) == 3, "15 doesn't work" 

# Problem 2
def test_month_length():
	assert ut.month_length("January", leap_year = True) == 31, "January leap year doesn't work"
	assert ut.month_length("January", leap_year = False) == 31, "January doesn't work"
	assert ut.month_length("February", leap_year = False) == 28, "February doesn't work"
	assert ut.month_length("February", leap_year = True) == 29, "February leap year doesn't work"
	assert ut.month_length("April", leap_year = True) == 30, "April leap year doesn't work"
	assert ut.month_length("April", leap_year = False) == 30, "April leap year doesn't work"
	assert ut.month_length("Sophie", leap_year = True) == None, "Invalid month doesn't work"

# Problem 3
def test_operate():
	with pytest.raises(TypeError) as excinfo:
		ut.operate(1, 2, 3)
	assert excinfo.value.args[0] == "oper must be a string"
	assert ut.operate(1, 2, '+') == 3, "1 + 2 doesn't work"
	assert ut.operate(2, 1, '-') == 1, "2 - 1 doesn't work"
	assert ut.operate(1, 2, '*') == 2, "1 * 2 doesn't work"
	assert ut.operate(2, 1, '/') == 2, "2 / 1 doesn't work"
	with pytest.raises(ZeroDivisionError) as excinfo:
		ut.operate(1, 0, '/')
	assert excinfo.value.args[0] == "division by zero is undefined"
	with pytest.raises(ValueError) as excinfo:
		ut.operate(1, 2, 'a')
	assert excinfo.value.args[0] == "oper must be one of '+', '/', '-', or '*'"

# Problem 4
from UnitTesting import Fraction
@pytest.fixture
def set_up_fractions():
	frac_1_3 = ut.Fraction(1, 3)
	frac_1_2 = ut.Fraction(1, 2)
	frac_n2_3 = ut.Fraction(-2, 3)
	return frac_1_3, frac_1_2, frac_n2_3
def test_fraction_init(set_up_fractions):
	frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
	assert frac_1_3.numer == 1
	assert frac_1_2.denom == 2
	assert frac_n2_3.numer == -2
	frac = ut.Fraction(30, 42) # 30/42 reduces to 5/7.
	assert frac.numer == 5
	assert frac.denom == 7
	with pytest.raises(ZeroDivisionError) as excinfo:
		ut.Fraction(1, 0)
	assert excinfo.value.args[0] == "denominator cannot be zero"
	with pytest.raises(TypeError) as excinfo:
		ut.Fraction(1., 2.)
	assert excinfo.value.args[0] == "numerator and denominator must be integers"
def test_fraction_str(set_up_fractions):
	frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
	assert str(frac_1_3) == "1 / 3"
	assert str(frac_1_2) == "1 / 2"
	assert str(frac_n2_3) == "-2 / 3"
	assert str(Fraction(2, 1)) == "2"
def test_fraction_float(set_up_fractions):
	frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
	assert float(frac_1_3) == 1 / 3.
	assert float(frac_1_2) == .5
	assert float(frac_n2_3) == -2 / 3.
def test_fraction_eq(set_up_fractions):
	frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
	assert frac_1_2 == ut.Fraction(1, 2)
	assert frac_1_3 == ut.Fraction(2, 6)
	assert frac_n2_3 == ut.Fraction(8, -12)
	assert ut.Fraction(1, 2) == 2 / 4.
def test_fraction_add(set_up_fractions):
	frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
	assert frac_1_3 + frac_1_2 == ut.Fraction(5, 6)
	assert frac_1_3 + frac_n2_3 == ut.Fraction(-1, 3)
	assert frac_1_2 + frac_n2_3 == ut.Fraction(-1, 6)
def test_fraction_sub(set_up_fractions):
	frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
	assert frac_1_3 - frac_1_2 == ut.Fraction(-1, 6)
	assert frac_1_3 - frac_n2_3 == ut.Fraction(3, 3)
	assert frac_1_2 - frac_n2_3 == ut.Fraction(7, 6)
def test_fraction_mult(set_up_fractions): 
	frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
	assert frac_1_3 * frac_1_2 == ut.Fraction(1, 6)
	assert frac_1_3 * frac_n2_3 == ut.Fraction(-2, 9)
	assert frac_1_2 * frac_n2_3 == ut.Fraction(-2, 6)
def test_fraction_truediv(set_up_fractions):
	frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
	assert frac_1_3 / frac_1_2 == ut.Fraction(2, 3)
	assert frac_1_3 / frac_n2_3 == ut.Fraction(-1, 2)
	assert frac_1_2 / frac_n2_3 == ut.Fraction(-3, 4)
	with pytest.raises(ZeroDivisionError) as excinfo:
		frac_1_3 / ut.Fraction(0, 1)
	assert excinfo.value.args[0] == "cannot divide by zero"

# Problem 5
hand1 = ["1022", "1122", "0100", "2021", "0010", "2201", "2111", "0020", "1102", "0210", "2110", "1020"]
hand2 = ["1022"]
hand3 = ["1022", "1022", "0100", "2021", "0010", "2201", "2111", "0020", "1102", "0210", "2110", "1020"]
hand4 = ["102", "1122", "0100", "2021", "0010", "2201", "2111", "0020", "1102", "0210", "2110", "1020"]
hand5 = ["1023", "1122", "0100", "2021", "0010", "2201", "2111", "0020", "1102", "0210", "2110", "1020"]

def test_count_sets():
	assert ut.count_sets(hand1) == 6
	with pytest.raises(ValueError) as excinfo:
		ut.count_sets(hand2)
	assert excinfo.value.args[0] == "there are not exactly 12 cards"
	with pytest.raises(ValueError) as excinfo:
		ut.count_sets(hand3)
	assert excinfo.value.args[0] == "the cards are not all unique"
	with pytest.raises(ValueError) as excinfo:
		ut.count_sets(hand4)
	assert excinfo.value.args[0] == "one or more cards does not have exactly 4 digits"
	with pytest.raises(ValueError) as excinfo:
		ut.count_sets(hand5)
	assert excinfo.value.args[0] == "one or more cards has a character other than 0, 1, or 2"

def test_is_set():
	assert ut.is_set("1022", "2021", "0020") == True
	assert ut.is_set("1022", "1122", "0100") == False










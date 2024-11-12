from sortowanieprzezwstawianie import sortwstawianie
import pytest


def test_1():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sortwstawianie(l) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def test_2():
    l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert sortwstawianie(l) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def test_3():
    l = [5, 3, 8, 3, 9, 5, 3, 2, 5]
    assert sortwstawianie(l) == [2, 3, 3, 3, 5, 5, 5, 8, 9]
def test_4():
    l = [7]
    assert sortwstawianie(l) == [7]
def test_5():
    l = [9, 1]
    assert sortwstawianie(l) == [1, 9]
def test_6():
    l = [-3, -1, -7, -5, -2, -8, -6]
    assert sortwstawianie(l) == [-8, -7, -6, -5, -3, -2, -1]
def test_7():
    l = [5, -3, 8, -1, 2, -4, 7, -2]
    assert sortwstawianie(l) == [-4, -3, -2, -1, 2, 5, 7, 8]
def test_8():
    l = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert sortwstawianie(l) == [0, 0, 0, 0, 0, 0, 0, 0, 0]
def test_9():
    l = [1, 5, 3, 9999, 2, 6]
    assert sortwstawianie(l) == [1, 2, 3, 5, 6, 9999]
def test_10():
    l = []
    assert sortwstawianie(l) == []


from hypothesis import given, strategies as st
import neetcode_practice_2024.two_pointers.problem_1_valid_palindrom as problem
import random
import itertools
import string

import importlib

importlib.reload(problem)


@given(st.text(min_size=1))
def test_solution_valid(half):
    input = half + "".join(reversed(half))
    assert problem.solution_straightforward(input) is True
    assert problem.solution_stack(input) is True


@given(st.text(min_size=1))
def test_solution_invalid(half):
    input = half + "".join(reversed(half)) + "__"
    assert problem.solution_straightforward(input) is False
    assert problem.solution_stack(input) is False


def test_solution_hardcoded():
    assert problem.solution_straightforward("") is True
    assert problem.solution_straightforward("a") is True
    assert problem.solution_straightforward("aa") is True
    assert problem.solution_straightforward("aba") is True
    assert problem.solution_straightforward("abba") is True
    assert problem.solution_straightforward("abab") is False
    assert problem.solution_straightforward("a ") is False
    assert problem.solution_straightforward(" a") is False

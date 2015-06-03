# -*- coding: utf-8 -*-

import pytest

from ish import ish
from ish import TRUE_STRINGS

def test_true_ish():
    assert 'Yeah' == True-ish
    assert 'yup' == True-ish

def test_true_ish_unicode():
    mine = u'نعم'
    assert  mine == True-ish

def test_false_ish():
    assert 'Nope' == False-ish
    assert 'Nah' == False-ish

def test_maybe():
    with pytest.raises(ValueError):
        'Whatever' == True-ish

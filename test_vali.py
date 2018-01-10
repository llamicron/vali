import unittest
import pytest

from vali import validate, ValidationError


class TestVali(unittest.TestCase):
    def setUp(self):
        pass

    def test_only_accepts_a_dict(self):
        with self.assertRaises(ValueError):
            validate('anything but a dict')
            validate('string')
            validate(('tuple', 'tuple'))
            validate(54)

    def test_values_must_be_lists(self):
        with self.assertRaises(ValueError):
            validate({'string': []})
            validate({'string': int})
            validate({'string': (int, 'required')})
            validate({'string': None})
            validate({'string': False})

    def test_it_returns_false_for_bad_validations(self):
        results = validate({
            14: [str],
            'string': [int],
            '': ['required'],
            None: ['required'],
            ('not', 'a', 'list'): [bool],
        })
        assert not results

    def test_it_raises_an_exception_if_chosen(self):
        with self.assertRaises(ValidationError):
            results = validate({
                14: [str],
                'string': [int],
                'not a tuple': [tuple],
                None: ['required'],
            }, raise_on_failure=True)

    def test_it_returns_failed_validations_if_chosen(self):
        results = validate({
            45: [int, 'required'],
            'not a failure': [str],
            'is a failure': [tuple],
            'is another failure': [list]
        }, return_failures=True)
        assert results
        assert type(results) is list
        assert len(results) == 2
        assert type(results[0]) is tuple

    def test_good_values(self):
        assert validate({
            45: [int, 'required'],
            'string': [str, 'required'],
            '': [str],
            ('f', 's'): [tuple]
        })

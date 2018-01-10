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

    def test_keys_have_to_be_a_valid_type(self):
        with self.assertRaises(TypeError):
            validate({
                'not': 'string',
                'a': 15,
                'valid': 14.8,
                'type': ('first', 'second'),
                'in': {'key': 'value'},
                'the_keys': ['first', 'second'],
            })

    def test_it_returns_false_for_bad_validations(self):
        results = validate({
            str: 14,
            int: 'string',
            tuple: ['not', 'a', 'tuple'],
            list: ('not', 'a', 'list'),
        })
        assert not results

    def test_it_raises_an_exception_if_chosen(self):
        with self.assertRaises(ValidationError):
            results = validate({
                str: 14,
                int: 'string',
                tuple: ['not', 'a', 'tuple'],
                list: ('not', 'a', 'list'),
            }, raise_on_failure=True)

    def test_it_returns_failed_validations_if_chosen(self):
        results = validate({
            int: 45,
            str: 'not a failure',
            tuple: 'is a failure',
            list: 'is another failure'
        }, return_failures=True)
        assert results
        assert type(results) is list
        assert len(results) == 2
        assert type(results[0]) is tuple

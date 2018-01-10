#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""


class ValidationError(ValueError):
    pass


def validate(types, raise_on_failure=False, return_failures=False):
    # Make sure they give us a dict
    if not isinstance(types, dict):
        raise ValueError("Types must be of type dict")

    # Make sure each key is a valid type
    for key in types.keys():
        if not type(key) is type:
            raise TypeError("A valid type must be supplied")

    # Check to make sure the type of the value is the same as the given type
    # AKA validate
    failed = []
    for given_type, value in types.items():
        # If the type is not a list, but we have a list of values:
        if given_type is not list and type(value) is list:
            for item in types.get(given_type):
                validate_value(return_failures, raise_on_failure, failed, given_type, item)

        elif type(value) is not given_type:
            # Failed Validation
            validate_value(return_failures, raise_on_failure, failed, given_type, value)

    if failed:
        return failed


def validate_value(return_failures, raise_on_failure, failed, given_type, value):
    if return_failures:
        failed.append((given_type, value))
        return

    if raise_on_failure:
        if given_type != type(value):
            raise ValidationError(
                "Validation Failed: type of given value (%s) does not match the given type (%s)" % (
                    type(value), given_type))
    # Default behavior
    return False


if __name__ == "__main__":
    validate({str: "Validate"}, raise_on_failure=True)
    validate({str: ["Hello", "World"]}, raise_on_failure=True)
    validate({int: [42]}, raise_on_failure=True)

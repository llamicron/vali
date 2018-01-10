#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""


class ValidationError(ValueError):
    pass

def validate(types, raise_on_failure=False, return_failures=False):
    # Make sure they give us a dict
    if not isinstance(types, dict):
        raise ValueError("Types must be of type dict")

    # Make sure each value is a list
    for key, value in types.items():
        if not type(value) is list:
            raise ValueError("Value must be of type list")

    # Check to make sure the type of the value is the same as the given type
    # AKA validate
    failed = []
    for value, validations in types.items():
        if not type(value) in validations:
            # failed type check
            if return_failures:
                failed.append((validations, value))
                continue
            if raise_on_failure:
                raise ValidationError("Validation Failed: value given (%s) does not meet all validations (%s)" % (
                    value, validations))
            # Default behavior

            return False
        if 'required' in validations:
            if not value:
                return False

    if failed:
        return failed
    return True

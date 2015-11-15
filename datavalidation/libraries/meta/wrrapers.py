import os
import importlib
import collections


"""
Searches for libraries in `datavalidation.libraries` module

Expects Wrapper and VALIDATORS variables to be defined in library's package

Stores wrappers for libraries for later invocations
"""


def __package_path():
    return os.path.dirname(
        os.path.dirname(
            os.path.abspath(
                __file__
            )
        )
    )


def __package_children():
    return os.listdir(
        __package_path()
    )


def __get_libraries_names_wrappers_and_validators():
    for name in __package_children():
        try:
            library = importlib.import_module(
                'datavalidation.libraries.{}'.format(name)
            )
            yield name, library.Wrapper, library.VALIDATORS
        except (AttributeError, ImportError):
            pass


def __get_wrappers():
    wrappers = collections.defaultdict(dict)
    for name, wrapper, validators in __get_libraries_names_wrappers_and_validators():
        for validator_type, validator in validators.items():
            wrappers[validator_type][name] = wrapper(validator)
    return wrappers


ALL = __get_wrappers()

#!/usr/bin/env python

"""
An abominably-implemented FizzBuzz implementation.

PEP-8 Compliant.
"""

import argparse
from functools import wraps
from inspect import isclass
from itertools import product
import logging
from pprint import pformat
import re
from io import StringIO


def divisible_by(divisor):
    """
    Return a function that tests if a number is divisible by `divisor`.
    """
    def is_divisible(n):
        """ Placeholder docstring. """
        return n % divisor == 0
    is_divisible.__doc__ = """
        Return True if `n` is divisible by {}.
    """.format(divisor)
    return is_divisible


def identity(n):
    """ Return n """
    return n


def identifiericate(s):
    """
    Convert a string to a valid Python identifier.
    """
    return re.sub(r'[^a-z0-9_]', '', re.sub(r'[ \-]', '_', str(s).lower()))


def returner(val):
    """
    Return a function that takes a parameter, but always returns `val`.

    The function will have a clever name.
    """
    name = identifiericate(val)
    funcname = "i_will_return_{name}".format(name=name)

    def i_will_return(n):
        """ Placeholder docstring. """
        return val
    i_will_return.__name__ = funcname
    i_will_return.__doc__ = """
        A function that returns {!r}
    """.strip().format(val)

    return i_will_return


class UnFizzBuzzable(Exception):
    """
    An exception raised by a fizz-buzz strategy if it cannot resolve the
    provided number.
    """
    def __init__(self, n, test_result, lookup):
        msg = """I don't know what to do with n={}.
Test result is {}.
Rules are {}""".format(
            n, test_result, lookup)
        super(UnFizzBuzzable, self).__init__(msg)


class FizzBuzz(object):
    """
    An infinite iterable (and callable) that executes a given
    FizzBuzz strategy.
    """
    def __init__(self, strategy):
        self._strategy = strategy

    def __call__(self, n):
        """
        Generate a FizzBuzz result for `n`.
        """
        return self._strategy(n)

    def __iter__(self):
        """ An infinite iterator over FizzBuzz values. """
        i = 0
        while True:
            i += 1
            yield self(i)


def fizz_buzz(strategy):
    if isclass(strategy):
        @wraps(strategy)
        def fizz_buzz_creator(*args, **kwargs):
            return FizzBuzz(strategy(*args, **kwargs))
        return fizz_buzz_creator
    else:
        return FizzBuzz(strategy)


@fizz_buzz
def fizz_buzz_elif(n):
    """
    Return the correct FizzBuzz value for n by testing divisibility in
    an if-elif.
    """
    divisible_by_3 = n % 3 == 0
    divisible_by_5 = n % 5 == 0
    if divisible_by_3 and divisible_by_5:
        return "Fizz Buzz!"
    elif divisible_by_3:
        return "Fizz!"
    elif divisible_by_5:
        return "Buzz!"
    return n


@fizz_buzz
class FizzBuzzLookupStrategy(object):
    """
    A FizzBuzz strategy implemented by looking up handlers in a provided
    truth-table.
    """
    def __init__(self, tests, rules):
        self._tests = tests
        self._lookup = {}
        for spec, handler in rules:
            self.add_rule(spec, handler)

    def add_rule(self, spec, handler):
        for key in product(
                *([True, False] if x is None else [x] for x in spec)):
            self._lookup[key] = handler

    def __call__(self, n):
        """
        Generate a FizzBuzz result for `n`, using the lookup strategy.
        """
        key = tuple(test(n) for test in self._tests)
        try:
            handler = self._lookup[key]
            logging.debug("Value {}, handled by {!s}".format(n, handler))
            logging.debug("Handler doc: {}".format(handler.__doc__))
            return handler(n)
        except KeyError:
            raise UnFizzBuzzable(n, key, self)

    def __str__(self):
        result = StringIO()
        print >>result, "FizzBuzzLookupStrategy ["
        rules = [(k, v) for k, v in self._lookup.items()]
        rules.sort(key=lambda r: r[0])
        for key, handler in rules:
            criteria = ' '.join(['T' if test else '.' for test in key])
            print "{}    {!r}".format(criteria, handler)
        print >>result, "]"
        return result.getvalue()


fizz_buzz_lookup = FizzBuzzLookupStrategy(
    [divisible_by(3), divisible_by(5), divisible_by(12)],
    [
        ((False, False, False), identity),
        ((False, True, False), returner("Buzz!")),
        ((True, False, False), returner("Fizz!")),
        ((True, True, False), returner("Fizz Buzz!")),
        ((None, None, True), returner("Oh Yes!")),
    ]
)


def main():
    """
    Print out FizzBuzz values every quarter-second, forever.
    """
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-v', '--verbose', action='store_true')

    arguments = arg_parser.parse_args()

    if arguments.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # fizz_buzz_elif = FizzBuzz(fizz_buzz_elif)

    import time
    for n, v in enumerate(fizz_buzz_lookup, start=1):
        print "{}: {}".format(n, v)
        time.sleep(0.25)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import re
import sys


def magic_match(pattern, target):
    """
    Match a regex against a target string.

    Assign the result to a 'match' variable in the *caller's scope*.
    """
    frame = sys._getframe(1)
    result = re.match(pattern, target)
    # This is properly, properly evil. Don't do this:
    frame.f_locals['match'] = result
    return result


if magic_match(r'[abcde]+', sys.argv[1]):
    print(f"Your match was {match.group(0)}")
else:
    print('There was no match')

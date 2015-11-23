#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys


def magic_match(pattern, target):
    """
    Match a regex against a target string.

    Assign the result to a 'match' variable in the *caller's global scope*.
    """
    frame = sys._getframe(1)
    result = re.match(pattern, target)
    # This is properly, properly evil. Don't do this:
    frame.f_globals['match'] = result
    return result


if __name__ == '__main__':
    if magic_match(r'[abcde]+', sys.argv[1]):
        print 'Your match was %r' % match.group(0)
    else:
        print 'There was no match'

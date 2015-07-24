# -*- coding: utf-8 -*-
import sys

class UnIshable(Exception):
    pass


TRUE_STRINGS = [
    'true', 'yes', 'on', '1', 'yeah', 'yup',
    'oui',  # French
    'ja',   # German, Danish, Dutch, Afrikaans, Swedish, Norwegian
    'sim',  # Portuguese
    'sea',  # Irish
    'jes',  # Esperanto
    u'نعم'.lower(),  # Arabic
]
FALSE_STRINGS = [
    'false', 'no', 'off' '0', 'nope', 'nah',
    'non',   # French
    'nein',  # German
    'nej',   # Danish
    'nee',   # Dutch
    u'لأ'.lower(),     # Arabic
]
HAPPY_STRINGS = [
    'happy',
    'happy-face',
    'joyful',
]
ANGRY_STRINGS = [
    'angry',
    'anger',
    'grrr',
]
NEUTRAL_STRINGS = [
    'neutral',
]


class TrueIsh(object):
    def __eq__(self, other):
        if isinstance(other, basestring):
            if isinstance(other, str):
                cleaned_value = other.decode('utf-8').strip().lower()
            else:
                cleaned_value = other.strip().lower()
            is_trueish = cleaned_value in TRUE_STRINGS
            is_falseish = cleaned_value in FALSE_STRINGS
            print is_trueish, is_falseish
            if is_trueish:
                return True
            elif is_falseish:
                return False
            else:
                raise ValueError(
                    "Maybe! ({!r} is not recognised)".format(other))
        else:
            return bool(other)


class FalseIsh(object):
    def __eq__(self, other):
        return not trueish.__eq__(other)


class HappyIsh(object):
    def __eq__(self, other):
        # TODO - Return True if 'other' is happy!
        pass


class AngryIsh(object):
    def __eq__(self, other):
        # TODO - Return True if 'other' is angry!
        pass


class NeutralIsh(object):
    def __eq__(self, other):
        # TODO - Return True if 'other' is neutral!
        pass


class Ish(object):
    def __rsub__(self, other):
        if other is True:
            return trueish
        elif other is False:
            return falseish
        elif isinstance(other, str):
            if other.lower() in HAPPY_STRINGS:
                return happyish
            elif other.lower() in ANGRY_STRINGS:
                return angryish
            elif other.lower() in NEUTRAL_STRINGS:
                return neutralish
        raise UnIshable('{0!r} cannot be ished'.format(other))


happyish = HappyIsh()
angryish = AngryIsh()
neutralish = NeutralIsh()
trueish = TrueIsh()
falseish = FalseIsh()
ish = Ish()
__rsub__ = ish.__rsub__


class RsubableModule(type(sys)):
    def __init__(self, original_module):
        type(sys).__init__(self, original_module.__name__)
        self._original_module = original_module

    def __rsub__(self, *args, **kwargs):
        return self._original_module.__rsub__(*args, **kwargs)

    def __getattribute__(self, item):
        if item in ['__rsub__', '_original_module']:
            return object.__getattribute__(self, item)
        return getattr(self._original_module, item)


sys.modules[__name__] = RsubableModule(sys.modules[__name__])


if __name__ == '__main__':
    print 'Yup' == True-ish
    print 'Nope' == True-ish
    print 'False' == False-ish
    print 'Yeah' == False-ish
    print 'Whatever' == True-ish

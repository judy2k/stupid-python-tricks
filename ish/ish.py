# -*- coding: utf-8 -*-

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
    'false', 'no', 'off' '0', 'nope', 'nah', '',
    'non',   # French
    'nein',  # German
    'nej',   # Danish
    'nee',   # Dutch
    u'لأ'.lower(),     # Arabic
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


class Ish(object):
    def __rsub__(self, other):
        if other is True:
            return trueish
        elif other is False:
            return falseish

trueish = TrueIsh()
falseish = FalseIsh()
ish = Ish()

if __name__ == '__main__':
    print 'Yup' == True-ish
    print 'Nope' == True-ish
    print 'False' == False-ish
    print 'Yeah' == False-ish
    print 'Whatever' == True-ish

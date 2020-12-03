#!/usr/bin/env python3

class AutoPropertyMeta(type):
    def __init__(cls, name, bases, attrd):
        # Find all getter methods:
        for prop_name in [name[4:] for name in attrd if
                          name.startswith('get_')]:
            # Obtain references to the getter and optionally setter methods:
            getter = attrd.get('get_' + prop_name)
            setter = attrd.get('set_' + prop_name, None)

            # Create a new property using the getter and optional setter:
            prop = property(getter, setter)

            # Apply the new property, and remove the getter and setter from
            # the class:
            attrd[prop_name] = prop
            setattr(cls, prop_name, prop)
            delattr(cls, 'get_' + prop_name)
            if setter:
                delattr(cls, 'set_' + prop_name)

        return super(AutoPropertyMeta, cls).__init__(name, bases, attrd)


class AutoProperty:
    # Apply the magic property-applying metaclass:
    __metaclass__ = AutoPropertyMeta


class MyRecord(AutoProperty):
    """ This class magically has its get and set methods replaced with
    properties, because its metaclass is AutoPropertyMeta:

    # Say hello to Bernard:
    >>> bernard = MyRecord('Bernard', 'H', 'Fitch')

    # Print out the full name:
    >>> print bernard
    Bernard H. Fitch

    # We now have a read-only property, 'first':
    >>> print bernard.first
    Bernard

    # The defined 'get_first' method has disappeared:
    >>> print bernard.get_first()
    Traceback (most recent call last):
        ...
    AttributeError: 'MyRecord' object has no attribute 'get_first'

    # We can also access Bernard's middle initial:
    >>> print bernard.initial
    H

    # Because there's a setter, we can also set the initial:
    >>> bernard.initial = 'J'

    # ... and let's just make sure that's changed the value of initial:
    >>> print bernard
    Bernard J. Fitch

    # And if we do a 'dir' on Bernard, we can't see any magic:
    >>> print sorted( \
            [attr for attr in dir(bernard) if not attr.startswith('_')])
    ['first', 'initial', 'last']
    """

    def __init__(self, first, initial, last):
        self._first = first
        self._last = last
        self._initial = initial

    def get_first(self):
        return self._first

    def get_initial(self):
        return self._initial

    def set_initial(self, initial):
        self._initial = initial

    def get_last(self):
        return self._last

    def __str__(self):
        return "%s %s. %s" % (self._first, self._initial, self._last)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

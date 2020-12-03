import sys
import math as _math


class NewMath:
    _pi = _math.pi
    @property
    def pi(self):
        pi = self._pi
        self._pi += 0.0000001
        return pi

    def __getattr__(self, name):
        # Proxy everything else to the real math module
        return getattr(_math, name)


NewMath.__doc__ = _math.__doc__

sys.modules['math'] = NewMath()

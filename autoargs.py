from inspect import signature


def auto_args(target):
    """
    A decorator for automatically copying constructor arguments to `self`.
    """
    # Get a signature object for the target method:
    sig = signature(target)

    def replacement(self, *args, **kwargs):
        # Parse the provided arguments using the target's signature:
        bound_args = sig.bind(self, *args, **kwargs)
        # Save away the arguments on `self`:
        for k, v in bound_args.arguments.items():
            if k != "self":
                setattr(self, k, v)
        # Call the actual constructor for anything else:
        target(self, *args, **kwargs)

    return replacement


# Test out the decorator by writing a class and autoarg-ing the constructor:
class MyClass:
    @auto_args
    def __init__(self, a, b, c=None):
        pass


# Create an instance and check that the values have been stored away:
m = MyClass("A", "B", "C")
print(m.__dict__)  # => {'a': 'A', 'b': 'B', 'c': 'C'}

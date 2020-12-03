"""We were discussing when to invoke `super().tearDown` on Django tests... a friend said
>  a built-in context manager type thing for super calls would be a cool language feature

Here's an implimentation go on, use it in real tests
your future self will be ~proud~ ~confused~ ... cursing you
"""
import functools
import inspect


def super_later(f):
    """Makes sure the wrapped function tries to call its
    namesake on super() as the last thing it does
    """

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        fs_cls = context_that_defined(f)
        fs_cls_parent = inspect.getmro(fs_cls)[1]
        fs_cls_parent_f = getattr(fs_cls_parent, f.__name__, None)
        try:
            f(*args, **kwargs)
        except Exception as err:
            raise (err)
        finally:
            if fs_cls_parent_f:
                fs_cls_parent_f(*args, **kwargs)

    return wrapper


def context_that_defined(callable):
    """Try to get the context where `callable` was defined
    """
    if inspect.ismethod(callable):
        for cls in inspect.getmro(callable.__self__.__class__):
            if cls.__dict__.get(callable.__name__) is callable:
                return cls
        # 1st failover parse __qualname__
        callable = callable.__func__
    if inspect.isfunction(callable):
        cls = getattr(
            inspect.getmodule(callable),
            callable.__qualname__.split(".<locals>", 1)[0].rsplit(".", 1)[0],
        )
        if isinstance(cls, type):
            return cls
    # 2nd failover for descriptors
    return getattr(callable, "__objclass__", None)


class DecoratorParent:
    def some_method(self):
        print("called Parent.some_method")


class DecoratorChild(DecoratorParent):
    @super_later
    def some_method(self):
        print("called Child.some_method")


class FinalSuperMeta(type):
    def __new__(cls, name, bases, local):
        for attr in local:
            value = local[attr]
            if callable(value):
                local[attr] = super_later(value)
        return type.__new__(cls, name, bases, local)


class DontForgetToCall(metaclass=FinalSuperMeta):
    """All child classes will attempt
    to call `super().childs_method`
    on _all_ their methods
    """

    def exists_on_parent_too(self):
        print("called DontForgetToCall.exists_on_parent_too")


class CantForgetSuper(DontForgetToCall):
    def exists_on_parent_too(self):
        """will _implicitly_ call its parent.exists_on_parent_too"""
        print("called CantForgetSuper.exists_on_parent_too")

    def only_on_childclass(self):
        """no only_on_childclass  method on parent so we'll only print 1 thing"""
        print("called CantForgetSuper.only_on_childclass")


def decorator_example():
    """
    >>> child = DecoratorChild()
    >>> child.some_method()
    called Child.some_method
    called Parent.some_method
    """
    child = DecoratorChild()
    child.some_method()


def metaclass_example():
    """
    >>> will_call_parent = CantForgetSuper()
    >>> will_call_parent.exists_on_parent_too()
    called CantForgetSuper.exists_on_parent_too
    called DontForgetToCall.exists_on_parent_too

    >>> will_call_parent.only_on_childclass()
    called CantForgetSuper.only_on_childclass
    """
    will_call_parent = CantForgetSuper()
    will_call_parent.exists_on_parent_too()
    will_call_parent.only_on_childclass()


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print("calling decorated `Child().some_method` calls its superclass:")
    decorator_example()
    print()
    print("CantForgetSuper _implicitally_ calls its parents methods, if they exist:")
    metaclass_example()

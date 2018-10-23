import functools
import random


def once_only(f):
    '''A function decorater that ensures the decorated function is only called
       once during the lifetime of the VM.'''
    static_data = dict(been_called=False, result=None)

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if not static_data['been_called']:
            static_data['result'] = f(*args, **kwargs)
            static_data['been_called'] = True
            return static_data['result']

    return wrapper


class DependencyNotFoundError(NameError):
    pass


def depends(dependency_list):
    '''A function decorator that  ensures that the depended-upon functions are
       called (in order) before the decorated function is called. Dependencies
       will be called without any arguments.'''

    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            for dependency in dependency_list:
                if callable(dependency):
                    dependency()
                else:
                    if dependency in globals():
                        globals()[dependency]()
                    else:
                        raise DependencyNotFoundError(
                            "Dependency not found: %s" % dependency)
            return f(*args, **kwargs)

        return wrapper

    return decorator


def krisskross(fn):
    """
    Well make you jump, jump (out of a window)
    50% chance of reversing the order of args and kwargs keys
    """

    def wrapped(*args, **kwargs):
        if random.randint(1, 2) == 1:
            for k, v in kwargs.items():
                kwargs[k[::-1]] = v
                del kwargs[k]
            return fn(*args[::-1], **kwargs)
        return fn(*args, **kwargs)
    return wrapped


@once_only
def should_only_run_once():
    print "Function has been run!"


should_only_run_once()
should_only_run_once()


def a1():
    print 'a1'


def b1():
    print 'b1'


@depends([a1, b1])
def c1():
    print 'c1'


print '--------'
c1()


@depends([a1])
def b2():
    print 'b2'


@depends([b2])
def c2():
    print 'c2'


print '--------'
c2()


@depends(['a1', 'b1'])
def c3():
    print 'c3'

print '--------'
c3()

@krisskross
def guess_the_order(*args, **kwargs):
    print args
    print kwargs


guess_the_order(1,2,3, hello='world')
guess_the_order(1,2,3, hello='world')
guess_the_order(1,2,3, hello='world')
guess_the_order(1,2,3, hello='world')
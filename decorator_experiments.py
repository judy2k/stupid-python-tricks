import functools

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
                  raise DependencyNotFoundError("Dependency not found: %s" % dependency)
         return f(*args, **kwargs)
      return wrapper
   return decorator

@once_only
def should_only_run_once():
   print "Function has been run!"

should_only_run_once()
should_only_run_once()

def a():
   print 'a1',
def b():
   print 'b1',
@depends([a,b])
def c():
   print 'c1'

c()

@depends([a])
def b():
   print 'b2',
@depends([b])
def c():
   print 'c2'
c()

# There's a bug in this last one - calls a1 twice:
@depends(['a', 'b'])
def c():
   print 'c3'
c()

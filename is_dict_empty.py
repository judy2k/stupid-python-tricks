import io
from contextlib import redirect_stdout


# https://twitter.com/aaronbassett/status/1467564070870134790
def is_dict_empty(d):
    s = io.StringIO()

    with redirect_stdout(s):
        print(d)
    
    return len(s.getvalue()) == 3


print(is_dict_empty({}))  # => True
print(is_dict_empty({"Hello": "World"}))  # => False

# Stupid Python Tricks

This is (or will be) a consolidated repository of all the stupid Python tricks
I have written (and can still find).

A *stupid python trick* is usually an experiment with an advanced language
feature; ostensibly to learn how it works, but usually in order to abuse that
feature to write something truly horrible.

I used to be a Perl programmer.

I am also [no longer](CONTRIBUTORS.md) the only person responsible for all of this.


## fizz_buzz_abomination

This one got out of hand. It is an attempt to write Fizz Buzz, using as many
language features as possible. It uses a bunch of functional techniques, a
strategy pattern implementation, and dynamically named closures (I was
especially proud of that).

It is PEP-8 compliant.

## one_line_regex

A friend of mine used to complain that he couldn't run a regex as part of an
`if` statement's expression if he wanted to use the returned groups (you can
in Perl using implicit variables).

I worked out how to modify the caller's scope to dynamically add a variable
containing the result of the pattern match. *Mission accomplished*.

## Ish

Ish is a stupid library that allows you to test if a variable is `tru-ish` or
`false-ish`.

It exports a single variable called `ish`, which can be subtracted from `True`
or `False` to create a TrueIsh or FalseIsh object. This can be compared with
the value to see if it either:

1. Evaluates to `True`
2. Is a string containing the English, French, German, Danish, Dutch,
   Afrikaans, Swedish, Norwegian, Portuguese, Irish, Esperanto or Arabic for
   either `Yes` or `No` (or a handful of slang words with the same meaning).

If it is a string containing none of these known words, it raises
a `ValueError`

```python
if 'Yup' == True-ish:
    print 'True-ish!'
```

## marge_simpson

I wanted to see if I could create an emoticon that was valid Python syntax.
It turns out I could! `OOO[:-P]`

## clever_path_ob

Subclass `str`, add a bunch of interesting properties and methods, and *voila*,
easy path management, if a little bit too much voodoo.

**Note:** I'm not 100% sure I wrote this. Some of it doesn't seem like my style.
It's possible I came up with inspiration from looking at someone else's code.

## decorator_experiments

Contains an 'everlasting cache' (which is not very useful), and a (crazy)
decorator-based dependency calling mechanism. Warning, may cause seizures!

## stupid_metaclass_tricks

Only one trick! A metaclass that automatically replaces `get_` and `set_`
methods with properties that call the methods. Too much magic, but a neat trick,
I think.

## Deepish learning

A deep neural network based facial expression classifier is available.
Using it requires [Theano](http://deeplearning.net/software/theano/)
([Theano on Github](https://github.com/Theano/Theano)),
[Lasagne](http://github.com/Lasagne/Lasagne), and
[OpenCV 3](http://opencv.org/) with Python bindings.

To run a live demo, use IPython Notebook to run
`Live Deep Neural Network Demo.ipynb`. If you want to train a new model, run
`Train deep neural network.ipynb`.

To install OpenCV 3 on Windows, download the installer, find the .pyd extension
and put it into your Python interpreter's `Lib/site-packages` path.
To install it on MacOS X, use brew;
[installation instructions for OpenCV 2](https://jjyap.wordpress.com/2014/05/24/installing-opencv-2-4-9-on-mac-osx-with-python-support/)
(also worked for me for OpenCV v3). You must make OpenCV available to Python in the
same way as windows (put library in `lib/site-packages`/
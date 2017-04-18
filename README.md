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
`false-ish`. *Ish has graduated to its own [repository](https://github.com/judy2k/ish)!*

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

## true_false

You've all heard of the classic `#define TRUE FALSE` trick in C, right?

## gradually_worse_pi

Import this module, then import `math` and print out `pi` in a loop. I guarantee you'll be surprised!

## autoargs

It's so tiresome writing constructors that copy all their arguments to `self`. Now you can just use this very clever `@autoargs` decorator, and all will be done for you!
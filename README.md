# Stupid Python Tricks

This is (or will be) a consolidated repository of all the stupid Python tricks
I have written (and can still find).

A *stupid python trick* is usually an experiment with an advanced language
feature; ostensibly to learn how it works, but usually in order to abuse that
feature to write something truly horrible.

I used to be a Perl programmer.


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

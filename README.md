[![Build Status](https://github.com/localstack/airspeed/actions/workflows/main.yml/badge.svg)](https://github.com/localstack/airspeed/actions)
[![PyPI version](https://img.shields.io/pypi/v/airspeed-ext.svg)](https://pypi.org/project/airspeed-ext/)

# Airspeed - a Python template engine

This is a fork of the original [`airspeed`](https://github.com/purcell/airspeed) library, with some extensions used in [LocalStack](https://github.com/localstack/localstack).

⚠️ Note: This fork of `airspeed` focuses on providing maximum parity with AWS' implementation of Velocity templates (used in, e.g., API Gateway or AppSync). In some cases, the behavior may diverge from the VTL spec, or from the Velocity [reference implementation](https://velocity.apache.org/download.cgi).

## Change Log:
* v0.6.9: Small improvement of `Assignment`, introducing `AssignmentTerm` to help future expandability.
* v0.6.8: Added support for bracket in Assignment with `#set`; Added support for `Array.set`
* v0.6.7: fix support for floating point starting with a decimal; Implement `REPLACE_FORMAL_TEXT` to allow bypassing silent behavior of `FormalReference` element.
* v0.6.6: add support for `$string.matches( $pattern )`; fix bug where some escaped character would prevent string matching
* v0.6.5: handle `$map.put('key', null)` correctly
* v0.6.4: add support for string.indexOf, string.substring and array.isEmpty
* v0.6.3: array notation for dicts using string literals and merge upstream patches
* v0.6.2: add support to contains and toString functions
* v0.6.1: improve handling of multi-line dict expressions
* v0.6.0: add initial setup for snapshot testing against AWS and Java VTL; enhance AWS parity

---
Original README below ...
---

## What is Airspeed?

Airspeed is a powerful and easy-to-use templating engine for Python
that aims for a high level of compatibility with the popular
[Velocity](http://velocity.apache.org/engine/devel/user-guide.html)
library for Java.

## Selling points

* Compatible with Velocity templates
* Compatible with Python 2.7 and greater, including Jython
* Features include macros definitions, conditionals, sub-templates and much more
* Airspeed is already being put to serious use
* Comprehensive set of unit tests; the entire library was written test-first
* Reasonably fast
* A single Python module of a few kilobytes, and not the 500kb of Velocity
* Liberal licence (BSD-style)

## Why another templating engine?

A number of excellent templating mechanisms already exist for Python,
including [Cheetah](http://www.cheetahtemplate.org/), which has a
syntax similar to Airspeed.

However, in making Airspeed's syntax *identical* to that of Velocity,
our goal is to allow Python programmers to prototype, replace or
extend Java code that relies on Velocity.

A simple example:

```python
t = airspeed.Template("""
Old people:
#foreach ($person in $people)
 #if($person.age > 70)
  $person.name
 #end
#end

Third person is $people[2].name
""")
people = [{'name': 'Bill', 'age': 100}, {'name': 'Bob', 'age': 90}, {'name': 'Mark', 'age': 25}]
print t.merge(locals())
```

You can also use "Loaders" to allow templates to include each other using the `#include` or `#parse` directives:

```
% cat /tmp/1.txt
Bingo!
% cat /tmp/2.txt
#parse ("2.txt")
% python
Python 2.4.4 (#1, May 28 2007, 00:47:43)
[GCC 4.0.1 (Apple Computer, Inc. build 5367)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from airspeed import CachingFileLoader
>>> loader = CachingFileLoader("/tmp")
>>> template = loader.load_template("1.txt")
>>> template.merge({}, loader=loader)
'Bingo!\n'
```

### How compatible is Airspeed with Velocity?

All Airspeed templates should work correctly with Velocity. The vast
majority of Velocity templates will work correctly with Airspeed.

### What does and doesn't work?

Airspeed currently implements a very significant subset of the
Velocity functionality, including `$variables`, the `#if`, `#foreach`,
`#macro`, `#include` and `#parse` directives, and `"$interpolated #strings()"`. Templates are unicode-safe.

The output of templates in Airspeed is not yet 'whitespace compatible'
with Velocity's rendering of the same templates, which generally does
not matter for web applications.

### Where do I get it?

https://github.com/purcell/airspeed

### Getting started

The
[Velocity User Guide](http://velocity.apache.org/engine/releases/velocity-1.7/user-guide.html)
shows how to write templates.  Our unit tests show how to use the
templates from your code.

### Reporting bugs

Please feel free to create tickets for bugs or desired features.

### Who is to blame?

Airspeed was conceived by Chris Tarttelin, and implemented jointly in
a test-driven manner by Steve Purcell and Chris Tarttelin. We can be
contacted by e-mail by using our first names (at) pythonconsulting dot
com.

Extensions for compatibility with Velocity 1.7 were kindly provided by
[Giannis Dzegoutanis](https://github.com/erasmospunk), and further modernization
has been done by [David Black](https://github.com/dbaxa/).

<hr>

[💝 Support this project and my other Open Source work](https://www.patreon.com/sanityinc)

[💼 LinkedIn profile](https://uk.linkedin.com/in/stevepurcell)

[✍ sanityinc.com](http://www.sanityinc.com/)

[🐦 @sanityinc](https://twitter.com/sanityinc)

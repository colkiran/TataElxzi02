
# emulate C style - printf
format = "Welcome %s, What a %s Player"
print(format)
values = ("Sachin", "superb")                   # tuples
print(values)
print(format % values)

print("-" * 40)
format = "Welcome %s, with a rating of %.3f, what a %s Player"
print(format % ("Sachin", 4, "class"))
print(format % ("Sachin", 4.3245645, "class"))
print(format % ("Sachin", 4.8, "class"))
print(format % ("Sachin", 4.8999, "class"))
print("Welcome %s, with a rating of %.3f, what a %s Player" % ("Sachin", 4.7999, "class"))

# emulate unix style
print("-" * 40)
print("-" * 40)
from string import Template
tmpl = Template("Welcome $name, what a $adj player")
print(f"tmpl, {tmpl}")
print(tmpl.substitute(name="Sachin", adj="class"))

# format method of string class python
print("Welcome {}, what a {} player for {}".format("Rahul", "class", "India"))
print("Welcome {0}, what a {1} player for {2}".format("Rahul", "class", "India"))
print("Welcome {2}, what a {0} player for {1}".format("class", "India", "Rahul"))
print("Welcome {name}, what a {adj} player for {ctr}".format(name="Rahul", adj="class", ctr="India"))
print("Welcome {0}, what a {1} player for {ctr}".format("Rahul", "class", ctr="India"))
print("Welcome {name}, with a rating of {rating}, what a {adj} Player".format(
    name="Sachin", rating=4.7999, adj="class"))
print("Welcome {name}, with a rating of {rating:.3f}, what a {adj} Player".format(
    name="Sachin", rating=4.7999, adj="class"))

# Interpolation
print("-" * 40)
from math import pi, e
print(f"PI = {pi} and Euler's constant = {e}")

print("PI = {} and Euler's constant = {}".format(pi, e))
print("PI = {0} and Euler's constant = {1}".format(pi, e))

full_name = ['Sachin', "Tendulkar"]                 # list (array)
print("Mr. {name}".format(name=full_name))
print("Mr. {name[0]}".format(name=full_name))
print("Mr. {name[1]}".format(name=full_name))
print("Mr. {name[0]} {name[1]}".format(name=full_name))

print("-" * 40)

import math
print(__name__)             # name of the module    __name__    double underscore = dunder name
print(math.__name__)

print('The {mod.__name__} module gives the value of {mod.pi} and eulers '
      'constant {mod.e}'.format(mod=math))

print("Conversions".center(40, "-"))
print("{val} {val} {val}".format(val="A"))
print("{val!s} {val!r} {val!a}".format(val="A"))

print("The number {num} {num} {num}".format(num=36))
print("The number {num} {num:f} {num:b}".format(num=36))
print("The number {num:10} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=36234235))

print("Alignment".center(40, "-"))
print("{num:15}Dravid".format(num=3))
print("{num:15}Dravid".format(num="Rahul"))
print("{}".format("Rahul Dravid"))
print("{:.5}".format("Rahul Dravid"))

print("-" * 40)
print("{pi:10.3}".format(pi=pi))
print("{pi:010.3}".format(pi=pi))
print("{pi:010.4}".format(pi=pi))
print("{pi:010.5}".format(pi=pi))

print("-" * 40)
print("{:10.2f}Sachin".format(pi))
print("{:<10.2f}Sachin".format(pi))                 # left align
print("{:^10.2f}Sachin".format(pi))                 # center align
print("{:>10.2f}Sachin".format(pi))                 # right align

print("{:-^40}".format("Hello World"))
print("Hello World".center(40, "-"))
print("{0:.<70}{1:.>5}".format("Python Basics", 30))


print("-" * 40)
def contents(content, pageno):
    print("{0:.<70}{1:.>5}".format(content, pageno))

contents("Functions", 50)
contents("Lambda", 65)
contents("Decorator", 80)

print("-" * 40)
print('{1}{0:{1}^{2}}{1}'.format("Hello World","=",40))
print("{0:{1}^40}".format("Hello", "="))


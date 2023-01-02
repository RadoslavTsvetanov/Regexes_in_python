# this is a simple search program which (obviously) searches for a pattern in a given string using the "re" module
import re
# with re.compile we crate a "re" object and that way we have access to the "re" methods
# with () we are creting regex grous which we can later use with the "group" method
thing_pattern = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
string_to_be_passed = "Hi my phone is 333-444-4444"
# "search" serches for the given pattern py its object in the sting provided by its argument
thing_to_be_found = thing_pattern.search(string_to_be_passed)
# group gives us access to the "found_thing"
print("thing you are looking for " + thing_to_be_found.group())
# in this case we are looking for a phone number
print("individual parts are:" + thing_to_be_found.group(1) + ", " +
      thing_to_be_found.group(2) + ", " + thing_to_be_found.group(3))
# if we want to detect special characters (for example "()") we need to use \ since that way we transform it into a raw string character
# the "|" is the equivelent of || in strings
heroRegex = re.compile(r'girl|boy')
string_to_be_passed = 'Alex is a girls'
mo1 = heroRegex.search(string_to_be_passed)
print(mo1.group())


# the ? operator is used t check whether something or not exists without returning None (for exanple if we want to look for insane insted of (inasne|sane) we use ?)
Regex = re.compile(r'(in)?sane')
string_to_be_passed = 'Bob is insane'
thing_to_be_found = Regex.search(string_to_be_passed)
print("Bob is " + thing_to_be_found.group())

# we tell it that there can be multiple "mi-s" if we want it to be atleast one time we need to use +(
Regex = re.compile(r'(mi)*')
string_to_be_passed = 'Bob snorted like this mimimimimimimimimimi'
if(Regex.search(string_to_be_passed) != None):
    i = string_to_be_passed.index(" ")
    print(string_to_be_passed[0:i])
    # it will print while it finds it
    found = Regex.search(string_to_be_passed)


# {} is used for repeting it without typing manually
haRegex = re.compile(r'(Ha){3,5}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())


# that how we define non greedy regex since without it it will continue untio the final
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
(mo2.group())


# since the start we have used search which ends with the first ocurrence of the regex

# with findall we go through the entire string
Regex = re.compile(r'(\d\d\d){3}')
string = '999999999 888888888'
found1 = Regex.findall(string)
print(found1)

# Shorthand character class
# Represents
# \d = Any numeric digit from 0 to 9.

# \D = Any character that is not a numeric digit from 0 to 9.

# \w = Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)

# \W = Any character that is not a letter, numeric digit, or the underscore character.

# \s = Any space, tab, or newline character. (Think of this as matching “space” characters.)

# \S = Any character that is not a space, tab, or newline.
# we can also create our own classes
# we can use $ and ^ to refernce the start and end of the string


# we use the "." to say that before the pointed sequence we have something and we want to take it
mimic_regex = re.compile(r'(.ut)')
string_to_be_passed = "hi is there but in the hut"
mimic_found = mimic_regex.findall(string_to_be_passed)
print(mimic_found)


# we use the (.*) to say that there is something.We use it to take the string content after something
long_regex = re.compile(r'First name: (.*) last name: (.*)')
string_to_be_passed = "First name: Hi last name: Bye"
find = long_regex.search(string_to_be_passed)
print(find.group(1), find.group(2))


# if we want a dot to get the "\n" (it usually doesnt) we need to use the DOTALL method of re (re>DOTALL)
# if we want case insensitive search we need to use the I method of re (re.I)

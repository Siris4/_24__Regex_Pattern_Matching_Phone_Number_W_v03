import re

haRegEx = re.compile(r'(Ha){3,5}')
haMo = haRegEx.search('HaHaHaHaHaHaHaHa that was really funny')
print(haMo.group())
#HaHaHaHaHa   #this may have 8 Ha's but the range only matches up to 5. Min of 3.

digitRegex = re.compile(r'(\d){3,5}')
digitMo = digitRegex.search('Can you find me? 4698763786')
print(digitMo.group())
#46987    # (5 digits max)

digitRegex = re.compile(r'(\d){3,5}?')  # ? doesn't mean 0 or 1 here, when it comes
# after a pattern like {3,5} (as opposed to immediately after a group), this means do
# a NON-GREEDY match, and will select the SMALLEST possible string.
digitMo = digitRegex.search('Can you find me? 4698763786')
print(digitMo.group())
#469    # (3 digits max, since ? is looking for the smallest non-greedy string digits)


#RegEx ,or regular expression is a sequence characters that forms a search pattern.
#RegEx can be used to check if a string contains the specified search pattern.
#python has a built-in module called re to work with regular expressions.
import re
#search for a pattern in a string
pattern = r"hello"
string = "hello world"
match = re.search(pattern, string)
if match:
    print("Pattern found in the string")
else:    print("Pattern not found in the string")

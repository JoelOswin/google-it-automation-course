#!/usr/bin/env python3
import re
def compare_strings(string1, string2):
 #Convert both strings to lowercase
 #and remove leading and trailing blanks
 string1 = string1.lower().strip()
 string2 = string2.lower().strip()
 #print(string1,string2)

 #Ignore punctuation
 punctuation = r"[.?!,;:\-']*" # re.error: bad character range :-' at position 6
 #print(re.search(punctuation,string1))



 string1 = re.sub(punctuation, r"", string1)
 string2 = re.sub(punctuation, r"", string2)
# print(string1,string2)

 #DEBUG CODE GOES HERE
 #9print(string1 == string2)


 return string1 == string2


print(compare_strings("Have a Great Day!", "Have a great day?")) # True
print(compare_strings("It's raining again.", "its raining, again")) # True
print(compare_strings("Learn to count: 1, 2, 3.", "Learn to count: one, two, three.")) # False
print(compare_strings("They found some body.", "They found somebody.")) # False

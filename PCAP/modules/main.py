# Option 1
#import helper

#name = "Vijai Anand Ramalingam"
#print(f"Uppercase Letters: {helper.extract_uppercase(name)}")
#print(f"Lowercase Letters: {helper.extract_lowercase(name)}")


# Option 2
from helper import extract_lowercase, extract_uppercase

name = "Vijai Anand Ramalingam"
print(f"Uppercase Letters: {extract_uppercase(name)}")
print(f"Lowercase Letters: {extract_lowercase(name)}")

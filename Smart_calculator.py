import sys
sys.path.append('/my_modules/')

import my_modules
from my_modules.mathy import *

print(responses[0])
print(responses[1])

while True:
    print()
    text=input("Enter calculations to be performed : ")
    for word in text.split(' '):
        if word.upper() in operations:
            try:
                l=extract_numbers_from_text(text)
                ans=operations[word.upper()](l[0],l[1])
                print(ans)
            except:
                print("Please enter valid string")
            finally:
                break
        elif word.upper() in commands:
            commands[word.upper()]()
            break
    else:
        sorry()

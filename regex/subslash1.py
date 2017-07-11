import re
# Lets try and reverse the order of the day and month in a date
# string. Notice how the replacement string also contains metacharacters
# (the back references to the captured groups) so we use a raw
# string for that as well.

name = input("Enter your name")
print(re.sub(r'(\w+) (\w+)', r'\2 \1', name))
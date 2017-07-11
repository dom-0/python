import re

text = "This is a happy world...but i am not sure if people are happy always"

pattern = re.compile(r'h(a)ppy')
for match in pattern.finditer(text):
    print("matched: {} inside happy at {}".format(match.group(1), match.span(1)))
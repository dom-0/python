import re

text = "The quick brown fox jumps over a lazy dog."



iterator = re.finditer(r'\b(\w)(\w)', text)
for i in iterator:
    print("{} {} {} {}".format(i.group(), i.span(), i.start(), i.end()))
    print("{} {} {} {}".format(i.group(1), i.span(1), i.start(1), i.end(1)))

print('-=' * 40)
print( re.findall (r'\b(\w)(\w*\b)', text))

print('-=' * 40)
for i in (re.findall(r'\b(\w)(\w*\W+)', text)):
    print(i)
    print(i[0].upper(), end="")
    print(i[1], end="")
    # print(i[2], end="")

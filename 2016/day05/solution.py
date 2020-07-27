import hashlib
import re

pattern = re.compile("^0{5}")
door = "ugkcyxxp"

code = [" "] * 8
i = 0
while(" " in code):
    text = door + str(i)
    result = hashlib.md5(bytes(text, 'utf-8')).hexdigest()
    if pattern.match(result):
        if result[5] in "01234567":
            idx = int(result[5])
            if code[idx] == " ":
                code[idx] = result[6]
                print(i)
    i += 1

print(code)
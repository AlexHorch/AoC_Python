start = "1321131112"

def step(text):
    result = ""
    prev = text[0]
    count = 1
    for i in range(len(text)-1):
        if text[i+1] == prev:
            count += 1
        else:
            result += str(count) + prev
            count = 1
            prev = text[i+1]
    result += str(count) + prev
    return result

def step_n_times(txt, n):
    result = txt
    for i in range(n):
        result = step(result)
    return result

a = step_n_times(start, 40)
b = step_n_times(a, 10)

print("after 40 iterations:", len(a), "; after 50 iterations:", len(b))
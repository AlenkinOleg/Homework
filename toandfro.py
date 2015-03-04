length = int(input())
if length != 0:
    string = str(raw_input())
while length != 0:
    newString = str()
    ns = str()
    i = 0
    for i in range(len(string) / length):
        if i % 2:
            newString += string[(i + 1) * length - 1:i * length - 1:-1]
        else:
            newString += string[i * length:(i + 1) * length:1]
    j = 0
    while j < length:
        i = 0
        while i < len(newString) / length:
            ns += newString[i * length +j]
            i += 1
        j += 1
    print(ns)
    length = int(input())
    if length != 0:
        string = str(raw_input())

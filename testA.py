str = "w w w a a w  "
new = str.split()
new.append(" ")

res = []

i = 0
arr = [new[i]]
while i < len(new) - 1:
    if new[i] != new[i + 1]:
        res.append(arr)
        arr = []
    arr.append(new[i + 1])
    i += 1

print(res)

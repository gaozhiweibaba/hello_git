num_list = []
for i in range(1, 100):
    if i % 7 == 0:
        num_list.append(i)
    if len(str(i)) <= 1:
        continue
    if list(str(i))[-1] == "7" and i not in num_list:
        num_list.append(i)

print(num_list)

print(len(num_list))


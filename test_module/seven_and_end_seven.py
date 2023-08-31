def seven_end(begin_num, end_num):
    num_list = []
    for i in range(begin_num, end_num):
        if i % 7 == 0:
            num_list.append(i)
        if len(str(i)) <= 1:
            continue
        if list(str(i))[-1] == "7" and i not in num_list:
            num_list.append(i)
    return num_list


seven_list = seven_end(1, 100)
print(seven_list)

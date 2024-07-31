# 有个列表["hello", "world", "yoyo"]，如何把列表里面的字符串联起来，得到字符串“hello_world_yoyo"?
def replace(list_list):
    new_str = ""
    for i in list_list:
        new_str += i
        if i == "yoyo":
            break
        else:
            new_str += "_"
    return new_str


# test_list = ["hello", "world", "yoyo"]
# end_list = replace(test_list)
# print(end_list)


# 把字符串s 中的每个空格替换成"%20"，输入: s = "We are happy."，输出:We%20are%20happy."。
def replace_space(space_str):
    new_two_str = space_str.replace(" ", "20%")
    return new_two_str


# two_str = "We are happy."
# end_list = replace_space(two_str)
# print(end_list)


# Python如何打印99乘法表?
def nine_ride_nine():
    for i in range(10):
        for k in range(i):
            result = i * (k + 1)
            print("%s * %s = %s" % (i, k+1, result), end=' ')
        print()


# nine_ride_nine()


# 从下标0开始索引，找出单词“welcome”在字符串"Hello, welcome tomy world.”中出现的位置，找不到返回-1。
def select_str(select_str_data, select_str_in):
    exist_list = list(select_str_in)

    for i in select_str_data:
        try:
            index = exist_list.index(i)
            print(i, "的下标是:", index)
        except Exception as e:
            print(i, "的位置找不到-1")


# word = "welcome"
# exist = "Hello, welcome tomy world."
# select_str(word, exist)


# 统计字符串"Hello, welcome to my world.”中字母w出现的次数。


def str_count(str_count_data, str_count_str):
    count_w = 0
    for i in str_count_str:
        if i == str_count_data:
            count_w += 1
    print(count_w)


three_str = "Hello, welcome to my world"
# str_count("w", three_str)


# 输入一个字符串str，输出第m个只出现过n 次的字符，如在字符串gbgkkdehh中，找出第2个只出现1次的字符，输出结果:d

four_str = "gbgkkdehh"







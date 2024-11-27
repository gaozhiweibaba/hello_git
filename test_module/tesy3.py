# data:要排序的数据
def bubble(data):
    n = len(data)  # 得到数据长度n
    # 排序，对数据遍历n-1轮,因为最后剩下一个元素时，无需再排
    for i in range(n - 1):
        end = n - i - 1  # 每轮需比较n-i个数据，共需比较n-i-1次
        for j in range(0, end):  # 开始比较相邻的两个数据
            if (data[j] > data[j + 1]):  # 前一个元素>后一个元素时，交换
                data[j], data[j + 1] = data[j + 1], data[j]
        print(f"第{i + 1}轮排序后:", data)


data = [3, 5, 9, 7, 2, 1]
print("排序开始前:", data)
bubble(data)
print("排序完成后:", data)
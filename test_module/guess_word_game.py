# 在这个游戏中，你必须一个字母一个字母的猜出秘密单词。
# 如果你猜错了一个字母，你将丢掉一条命。
# 正如游戏名那样，你需要仔细选择字母，因为你的生命数量非常有限。

word_list = ["a", "b", "c", "d"]
game_count = len(word_list)
print("这是一个猜单词游戏，需要猜%s次，公有%s生命值" % (game_count, game_count))
for i in word_list:
    input_data = input("请输入本次字母：")
    if input_data == i:
        print("你赢了，正确答案是", i)
        print("❤" * game_count)
    else:
        print("你输了，生命值-1", )
        game_count -= 1
        print("❤" * game_count)



# 账户最大本金收益率 = 当周期最大累积净利润/当周期最大投入本金
# 当周期最大累积净利润 = 当日期末持仓市值(close price,multiplier,quantity) - 当日期初持仓市值 + 当日所有卖出收入 - 当日所有买入支出 + 昨日的当日累计利润
# 当周期最大投入本金 = 当周期每日累计投入本金 = 账户当周期的期初净资产 (net liquidation) + (∑当周期累计入金 - ∑当周期累计出金)
# 823856的这个账号

dangri_qimo_chicang = [9335.55991,9877.375766,9881.891929,10531.99486,11123.51935,11917.99302,11917.99302,11917.99302,
                       14848.49189,15818.45581,16083.68556,16323.96592,16234.07051,16234.07051,16234.07051,15911.87427,
                       16301.15397,16328.74798,15901.73155,15832.36962,15832.36962,15832.36962,15832.36962]


one_max_list = [9264.477085,
9339.267001,
9347.34291,
9314.552629,
9267.408716,
9194.149759,
9194.149759,
9194.149759,
8972.90362,
8981.185955,
9172.660922,
9381.79334,
9329.79748,
9329.79748,
9329.79748,
9582.525372,
9580.359065,
9608.425601,
9178.860292,
2537.482133,
2537.482133,
]

two_max_list = [18422.83562,
18422.83562,
18050.83562,
26894.39443,
27266.94528,
26370.90616,
26370.90616,
26370.90616]

print(max(two_max_list))


num = 15911.8742683-16234.0705139+576.76-0+(9582.525371959-9329.797480374)

# print((num / 9329.797480374)* 100)


max_num = 129653.1375
little_num = 127688.0272

new_num = (max_num - little_num)/max_num
# print(new_num* 100)


tt12 = -0.0337

tt11 = tt12 * 365 / 6
# print(tt11 * 100)


square = 126408.21 ** 2
# print("----", square)


p_one = 126764.4434634

p_two = 125782.9657025

num_new = (p_one-p_two) / p_one

print(num_new * 100)



shijianjiaquan = 1* (1-0.035356) * (1 -0.002588) * (1 -0.000005)* (1+0.000020) * (1+0.007117) * (1--0.002810) -1

print("------", shijianjiaquan )


one_num = (-0.035356 + 0.028267442987183644) ** 2
print("求和", one_num)


sum_list = [0.0000502475, 0.0006594337921320152, 0.0007987656836038058, 0.0008001794307531651, 0.0012520588055132498, 0.0006480814034457057]
print("zongshu", sum(sum_list))
print("zongshu/ 6:", sum(sum_list) / 6)

jieguo = 5.731861627494/6

print(jieguo)

zuidabenjin = 18422.83562 - 18050.83562 - 690 -3995.7131699999973
print("最大本金：", zuidabenjin)

zuidabenjin_num = -4041.3235099999984 / 31308.26879

print("收益率：", zuidabenjin_num * 100)



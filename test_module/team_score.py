# 资金量得分, AccountId =183998
# （单个参赛用户账户累计净值/所有参赛用户账户累计净值总和）*30%+(（n+1-名次）/n)*70%
n = 7
net_liquidation_d = 100.02
total_assets = 141797
rank = 5
assets_score = (net_liquidation_d / total_assets) * 0.3 + ((n + 1 - rank) / n) * 0.7 * 100
print("资金量得分", assets_score)


# 最大本金收益率, AccountId =183998
# 最大本金收益率得分=账户最大本金收益率/所有账户中最高的最大本金收益率*100
index_1_maximum_principal_return_rate_d = 42.02
top_return = 80.8
return_score = index_1_maximum_principal_return_rate_d / top_return * 100
print("最大本金收益率得分:", return_score)


#  累计净利润得分
# （账户累计净利润/所有账户最大累计净利润*100）*30%+（(n+1—名次)/n*100）*70%，
max_cumulative_net_profit_d = 62.99
top_profit = 3623.34
profile_user_count = 7
profile_rank = 4
profit_score = (max_cumulative_net_profit_d / top_profit * 100) * 0.3 + \
               ((profile_user_count+1-profile_rank)/profile_user_count* 100)*0.7
print("累计净利润得分:", profit_score)


# 最大回撤得分
# - 最大回撤得分=【名次得分*100%】100 =【（n+1-名次）/n*100%】*100
index_8_maximum_draw_down_rate_d_user_count = 7
index_8_maximum_draw_down_rate_d_rank = 4
drawdown_score = ((index_8_maximum_draw_down_rate_d_user_count + 1 - index_8_maximum_draw_down_rate_d_rank)
            / index_8_maximum_draw_down_rate_d_user_count * 1) * 100
print("最大回撤得分", drawdown_score)


# 个人日榜总分
total_points = assets_score*0.35 + return_score*0.3 + profit_score*0.2 + drawdown_score * 0.15
print("个人日榜总分:", total_points)


# 团队日榜成绩
team_score_d = [73.929375, 69.07048, 60.110466]
print("团队日榜成绩:", sum(team_score_d))


# 团队月榜成绩
team_score_m = [72.2113, 65.63719, 65.42245]
print("团队月榜成绩:", sum(team_score_m))


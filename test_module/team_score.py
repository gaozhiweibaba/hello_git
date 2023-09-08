import joint_sql


def team_score_day(account_id):
    score_sql = "select index_8_maximum_draw_down_rate_d,index_1_maximum_principal_return_rate_d," \
                "max_cumulative_net_profit_d, net_liquidation_d " \
                "from activity.dw_tidb_team_trade_score_base_i_d where account_id=%s;" % (account_id)
    score_list = joint_sql.joint_sql(score_sql)
    team_count_sql = "select count(*) from activity.teamgame_v3_team_contest_record where" \
                     " team_number='TEAM024c1816e20773d8'"
    team_count = joint_sql.joint_sql(team_count_sql)
    total_assets_sql = "select SUM(net_liquidation_d) from activity.dw_tidb_team_trade_score_base_i_d"
    total_assets = joint_sql.joint_sql(total_assets_sql)
    rank_sql = "select account_id, net_liquidation_d from activity.dw_tidb_team_trade_score_base_i_d " \
               "order by net_liquidation_d desc;"
    rank_data = joint_sql.rank_dict(rank_sql)
    rank = 1
    for i in rank_data:
        if account_id == int(list(i)[0]):
            break
        else:
            rank += 1

    # 资金量得分, AccountId =183998
    # （单个参赛用户账户累计净值/所有参赛用户账户累计净值总和）*30%+(（n+1-名次）/n)*70%
    net_liquidation_d = score_list[0]
    assets_score = (net_liquidation_d / total_assets[0]) * 0.3 + ((team_count[0] + 1 - rank) / team_count[0]) * 0.7 * 100
    print("资金量得分", assets_score)

    # 最大本金收益率, AccountId =183998
    # 最大本金收益率得分=账户最大本金收益率/所有账户中最高的最大本金收益率*100
    index_1_maximum_principal_return_rate_d = score_list[1]
    top_return_sql = "select index_1_maximum_principal_return_rate_d from activity.dw_tidb_team_trade_score_base_i_d" \
                     " order by index_1_maximum_principal_return_rate_d desc limit 1"
    top_return = joint_sql.joint_sql(top_return_sql)
    return_score = index_1_maximum_principal_return_rate_d / top_return[0] * 100
    print("最大本金收益率得分:", return_score)

    #  累计净利润得分
    # （账户累计净利润/所有账户最大累计净利润*100）*30%+（(n+1—名次)/n*100）*70%，
    max_cumulative_net_profit_d = score_list[2]
    top_profit_sql = "select max_cumulative_net_profit_d from activity.dw_tidb_team_trade_score_base_i_d" \
                     " order by max_cumulative_net_profit_d desc limit 1"
    top_profit = joint_sql.joint_sql(top_profit_sql)[0]
    profile_rank_sql = "select account_id, max_cumulative_net_profit_d from activity.dw_tidb_team_trade_score_base_i_d" \
                       " order by max_cumulative_net_profit_d  desc "
    profile_rank_data = joint_sql.rank_dict(profile_rank_sql)
    profile_rank = 1
    for i in profile_rank_data:
        if account_id == int(list(i)[0]):
            break
        else:
            profile_rank += 1
    profit_score = (max_cumulative_net_profit_d / top_profit * 100) * 0.3 + \
                   ((team_count[0] + 1 - profile_rank)/team_count[0] * 100)*0.7
    print("累计净利润得分:", profit_score)

    # 最大回撤得分
    # - 最大回撤得分=【名次得分*100%】100 =【（n+1-名次）/n*100%】*100
    index_8_maximum_draw_down_rate_d_rank_sql = "select account_id, index_8_maximum_draw_down_rate_d from" \
                                                " activity.dw_tidb_team_trade_score_base_i_d order by" \
                                                " index_8_maximum_draw_down_rate_d  desc "
    index_8_maximum_draw_down_rate_d_rank_data = joint_sql.rank_dict(index_8_maximum_draw_down_rate_d_rank_sql)
    index_8_maximum_draw_down_rate_d_rank_data_rank = 1
    for i in index_8_maximum_draw_down_rate_d_rank_data:
        if account_id == int(list(i)[0]):
            break
        else:
            index_8_maximum_draw_down_rate_d_rank_data_rank += 1
    drawdown_score = ((team_count[0] + 1 - index_8_maximum_draw_down_rate_d_rank_data_rank)
                / team_count[0] * 1) * 100
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


if __name__ == '__main__':
    team_score_day(183998)


import pymysql


def joint_sql(sql):
    conn = pymysql.connect(
        host='172.30.75.250',
        port=3311,
        user='campaign',
        password='Campaign2021',
        database='activity',
        charset='utf8'
    )

    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    score_list_day = []
    for i in result:
        for k in i:
            score_list_day.append(k)
    return score_list_day


def rank_dict(sql):
    conn = pymysql.connect(
        host='172.30.75.250',
        port=3311,
        user='campaign',
        password='Campaign2021',
        database='activity',
        charset='utf8'
    )

    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    rank_dick = dict((x, y) for x, y in result)
    my_list = list(zip(rank_dick.keys(), rank_dick.values()))
    return my_list

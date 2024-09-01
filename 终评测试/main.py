r"""
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \|     |// '.
                 / \|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\  - /// |     |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                       `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

           佛祖保佑     永不宕机     永无BUG
"""


import datetime

import itertools

# 开始日期及结束日期
START_DATE = datetime.datetime(2000, 1, 1)
END_DATE = datetime.datetime(2020, 10, 1)


def isStartOfMonth(day: datetime.datetime):
    """是否是月初"""
    return day.day == 1


def isMonday(day: datetime.datetime):
    """是否是周一"""
    return day.weekday() == 0


def main(start: datetime.datetime = START_DATE, end: datetime.datetime = END_DATE):
    # 基本天数
    baseDays = end - start
    if baseDays.days < 0:
        raise ValueError("开始日期不能大于结束日期")

    dateList: list[datetime.datetime] = []  # 所有成立的日期
    runTimes = baseDays.days  # 跑步的总距离(初始化为天数(正常情况每天一公里))
    for i, j, t in itertools.product(
        range(2000, 2020 + 1), range(1, 12 + 1), range(1, 31 + 1)  # 年份, 月份, 天数
    ):
        try:
            # 创建`datetime.datetime`对象时，如果当前日期不成立，则会报错
            date = datetime.datetime(i, j, t)

            # 检测是否超过结束日期
            if (end - date).days >= 0:
                dateList.append(date)
        except:
            ...

    for i in dateList:
        # 如果第一项条件成立就不会检测第二项，所以不需要特意检测既是月初又是周一的日期
        if isStartOfMonth(i):
            runTimes += 1
        elif isMonday(i):
            runTimes += 1

    return runTimes


if __name__ == "__main__":
    result = main()
    print(f"共跑了 {result}公里")

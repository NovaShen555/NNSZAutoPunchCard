import schedule
import time
from punch_crack import *


def getTime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def your_task():
    # 清除output.csv的数据
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([])
    # 读取data.csv的数据逐个执行
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # 尝试获取cardId是否合法
            time.sleep(2)
            ck = punchCard(row[0], row[1])
            print(row[0], row[1])
            # ck = {'code': 200}
            print(getTime()+str(ck))
            if ck['code'] == 200:
                # 将数据写入CSV文件
                with open('output.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([row[0], getTime()])

# 创建一个调度器对象
scheduler = schedule.Scheduler()

# 定义每周日到下一个周五的每天早上7点和下午2点执行任务
days_of_week = ["sunday", "monday", "tuesday", "wednesday", "thursday"]

for day in days_of_week:
    scheduler.every().day.at("06:55").do(your_task)
    scheduler.every().day.at("14:35").do(your_task)
    scheduler.every().day.at("18:55").do(your_task)

# 定义周五的执行任务
scheduler.every().friday.at("06:55").do(your_task)
scheduler.every().friday.at("14:35").do(your_task)

# your_task()
while True:
    scheduler.run_pending()
    time.sleep(1)

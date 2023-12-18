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
            try:
                ck = punchCard(row[0], row[1])
                time.sleep(2)
                print(row[0], row[1])
                # ck = {'code': 200}
                print(getTime()+str(ck))
                if ck['code'] == 200:
                    # 将数据写入CSV文件
                    with open('output.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([row[0], getTime()])
            except:
                print(getTime()+'error')
                time.sleep(2)
                continue

# 创建一个调度器对象
scheduler = schedule.Scheduler()


# 定义周日的执行任务
scheduler.every().sunday.at("14:25").do(your_task)
scheduler.every().sunday.at("18:25").do(your_task)

# 定义周一的执行任务
scheduler.every().monday.at("06:45").do(your_task)
scheduler.every().monday.at("14:25").do(your_task)
scheduler.every().monday.at("18:25").do(your_task)

# 定义周二的执行任务
scheduler.every().tuesday.at("06:45").do(your_task)
scheduler.every().tuesday.at("14:25").do(your_task)
scheduler.every().tuesday.at("18:25").do(your_task)

# 定义周三的执行任务
scheduler.every().wednesday.at("06:45").do(your_task)
scheduler.every().wednesday.at("14:25").do(your_task)
scheduler.every().wednesday.at("18:25").do(your_task)

# 定义周四的执行任务
scheduler.every().thursday.at("06:45").do(your_task)
scheduler.every().thursday.at("14:25").do(your_task)
scheduler.every().thursday.at("18:25").do(your_task)

# 定义周五的执行任务
scheduler.every().friday.at("06:45").do(your_task)
scheduler.every().friday.at("14:25").do(your_task)

# your_task()
while True:
    scheduler.run_pending()
    time.sleep(20)

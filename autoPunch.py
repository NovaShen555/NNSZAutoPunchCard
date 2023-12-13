import schedule
import time
from punch_crack import *

cardId = "1397479175"
deviceId = "E4246CB6B512"




def your_task():
    # 在这里定义你的任务
    print("执行任务")
    punchCard(cardId, deviceId)

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

# 运行调度器
while True:
    scheduler.run_pending()
    time.sleep(1)

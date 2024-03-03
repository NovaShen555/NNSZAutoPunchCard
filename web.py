import json
import time

from flask import Flask, render_template, request, flash
from punch_crack import *
from autoPunch import punch

app = Flask(__name__)

# 定义CSV文件的路径
csv_file = 'data.csv'
csv_file2 = 'output.csv'

def getTime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 获取来自表单的数据
        cardId = request.form['input1']
        deviceId = request.form['input2']

        err = 0
        # 查找是否有重复的数据
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == cardId:
                    err = 1

        if err == 0:
            # 尝试获取cardId是否合法
            ck = punchCard(cardId, deviceId)
            print(getTime()+str(ck))
            if ck['code'] != 200:
                err = 1

        if err == 0:
            # 将数据写入CSV文件
            with open(csv_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([cardId, deviceId])

    if request.method == 'GET':
        punch()

    # 从第一个CSV文件中读取数据
    table_data = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            table_data.append(row)

    # 从第二个CSV文件中读取数据
    table_data2 = []
    with open(csv_file2, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            table_data2.append(row)

    return render_template('index.html', table_data=table_data2, table_data2=table_data)


if __name__ == '__main__':
    app.run(debug=True)

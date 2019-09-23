# coding=utf-8
"""
Created on 2019/9/23 11:30

@author: EwdAger
"""
import os
import csv
from datetime import datetime

author = "ningwenjie"
project_disk_path = "F:"
project_path = "F:\multi-analysis"
this_path = os.getcwd()

git_com = """
    {0} & \
    cd {1} & \
    git log --author="{2}" --date=short --pretty=format:'"%ad","%s"' >{3}\\log.csv
    """.format(project_disk_path, project_path, author, this_path)

os.system(git_com)
print("=========== Git Message 下载完毕 ===========")
msg_buff = []

with open('log.csv', encoding='UTF-8') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        date = row[0].lstrip('\'')
        msg = row[1].rstrip('\'')
        date = datetime.strptime(date, '%Y-%m-%d')
        msg_buff.append([date, msg])

f.close()

start_time = input("从几号后开始的信息（例：2019-9-20）> ")
start_time = datetime.strptime(start_time, '%Y-%m-%d')
record_buff = []

print("=========== 该时间后的 msg 条数如下 ===========")
for i, v in enumerate(msg_buff):
    if v[0] >= start_time:
        print(i, v[1])
        record_buff.append(v[1])

print("=============================================")
title = input("请输入1级标题（例如：修复bug）> ")
count = 1
with open("weekly_record.txt", "w") as f:
    while title != "EOF":
        f.writelines("{0}. {1}\n".format(count, title))
        msg_index = input("请输入需写入{}的条目（例：0 1 3）> ".format(title))
        msg_index = msg_index.split(" ")
        for i, v in enumerate(msg_index):
            f.writelines("    {0}.{1} {2}\n".format(count, i+1, msg_buff[int(v)][1]))
        count += 1
        dis_sele = list(set([i for i in range(len(record_buff))])-set([int(i) for i in msg_index]))
        title = input("请输入{0}级标题（例如：修复bug）,结束请输入EOF,{1}未被选中> ".format(count, dis_sele))

f.close()

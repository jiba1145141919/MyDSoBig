import json
import time
from PIL import Image

# 打开对话文件
with open('jb.json', encoding='utf-8') as jb:
    sb = json.load(jb)

# 存储键
ikun = ('凌乱','恩熙')

# 初始化图片
dajiba = Image.open('Deadperson.JPG')
dajiba = dajiba.resize((150, 150))
xiaojiba = Image.open('NC.JPG')
xiaojiba = xiaojiba.resize((150, 150))
# 将两个图片存储在jiba中
jiba = [dajiba,xiaojiba]
try:
    for gunmu in range(len(sb)):
        # 用gunmu变量从头到尾遍历sb（jb.json）
        for xiongda in range(2):
            # 每轮对话总共有两个人发的消息
            jjbb = sb[gunmu][ikun[xiongda]]
            # 用gunmu的当前值查找对应的jb.json中的对话，然后再根据xiongda找到ikun里存储的键，用于查找一轮对话中的特定人发送的所有消息，存储在jjbb中
            for xionger in range(len(jjbb)):
                # xionger变量用于遍历此人发送的消息，并选中此人发送的某条消息
                jianbi = jjbb[xionger]
                # jianbi是被选中的消息
                time.sleep(len(str(jianbi)) ** 0.4)
                print(ikun[xiongda],'：',end = '')
                # ↑插入名字/↓查找可能的图片引用
                if type(jianbi)is int:
                    # 图片
                    jiba[jianbi-1].show()
                else:
                    # 非图片
                    time.sleep(0.7)
                    print(jianbi)
            # 空行
            print()
except:
    print('呃呃呃喷气背包出故障啦啊啊啊啊啊啊啊啊啊啊')
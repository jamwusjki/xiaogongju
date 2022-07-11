from time import*
from alive_progress import alive_bar
import os
import time
import sys
def cc(text):
    timee = 0.1
    for i in text:
        sleep(timee)
        print(i,end='',flush = True)
        sys.stdout.flush()
    print("",end="\n")
    return ""

def getsum():
    a = 0
    b = 0
    sue = 0
    a = int(input(cc("请输入数的个数:")))
    cc("ok!,稍等·············")
    print("已完成")
    for i in range(a):
        b = int(input(cc("请输入数字:")))
        sue = sue + b
    cc("正在计算中···········")
    cc("计算完毕")
    cc("结果为:")
    print(sue)
    
cc("嗨害嗨，没错又是那只鸽子回来了：），是不是很想我（嘿嘿），主要是登录系统有bug，过一会就登不上了呜呜呜")
cc("这次做点有实质性的东西，避免你们说我***，不多废话了，直接使用吧，bilibili搜千小青雉，期待你的关注！")
os.system("cls")
cc("欢迎使用zyr牌加总器")
cc("正在加载中")
with alive_bar(100,force_tty=True) as bar:
    for i in range(100):
        time.sleep(0.01)
        bar()

cc("加载完成！祝你使用愉快！")
getsum()
cc("还要继续吗？")
h = 0
cc("继续请输0，退出请输1")
h = input("输入的地方->")
if h == 0:
    getsum()
else:
    quit()
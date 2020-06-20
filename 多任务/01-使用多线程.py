import time
import threading


def sing():
    """
    唱歌五秒钟
    :return:None
    """
    for i in range(5):
        print("----正在唱歌----")
        time.sleep(1)


def dance():
    """
    跳舞五秒钟
    :return:None
    """
    for i in range(5):
        print("正在跳舞")
        time.sleep(1)


def main():
    """
    我们想让边唱歌变跳舞
    什么是多任务：多个东西一起执行
    什么事情都给干，一边学习一边听歌
    :return:
    """
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()

import socket


def send_message(udp_socket):
    # 要发送到那个ip地址和端口
    dest_ip = input("请输入对方ip")
    dest_port = int(input("请输入对方端口"))
    message = input("请输入要发送的内容")
    # 发送消息
    udp_socket.sendto(message.encode('utf-8'), (dest_ip, dest_port))
    print(udp_socket)


def recv_message(udp_socket):
    # 接收消息
    # 接收到的消息有两个部分，一个部分为消息体，一个部分为发送者的信息

    recv_data = udp_socket.recvfrom(1024)
    recv_message_content = recv_data[0].decode('utf-8')
    recv_addr = recv_data[1]
    print('%s:%s' % (recv_addr, recv_message_content))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 7788))
    while True:
        print("-----欢迎使用聊天系统v1.0------")
        op = input("请选择要进行的操作：1. 发送消息 2. 接收消息 3.退出系统")

        if op == "1":
            # 发送消息
            send_message(udp_socket)
        elif op == "2":
            # 接收消息
            recv_message(udp_socket)
        elif op == "3":
            # 退出程序
            break
        else:
            print("请重新输入")


if __name__ == '__main__':
    main()

import socket


def main():
    # 创建一个套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 从键盘获取数据
    dest_ip = input('请输入对方ip')
    dest_port = input('请输入对方端口')
    send_data = int(input("输入要发送的内容"))

    # 绑定端口
    udp_socket.bind("", 7788)

    # 使用套接字发送内容
    udp_socket.sendto(send_data.encode('utf-8'), (dest_ip, dest_port))

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()

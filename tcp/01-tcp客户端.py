import socket


def main():
    # 1. 创建tcp套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 连接服务器
    server_ip = input("请输入要连接的服务器ip地址：")
    # 注意要转int
    server_port = int(input("请输入端口号："))
    server_addr = (server_ip, server_port)
    tcp_socket.connect(server_addr)
    # 3. 发送数据/接收数据
    send_data = input("请输入要传输的内容：")
    # udp 是sendto
    tcp_socket.send(send_data.encode('utf-8'))
    recv_data = tcp_socket.recv(1024)
    print(recv_data)
    # 4. 关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()

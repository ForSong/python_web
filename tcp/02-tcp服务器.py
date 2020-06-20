import socket


def main():
    # 1. 创建套接字（买个手机）
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. bind绑定ip和port（插入手机卡）
    tcp_server.bind(('', 7788))
    # 3. listen，让默认的套接字由主动变为被动（将手机设置成响铃模式）
    tcp_server.listen(128)
    while True:
        # 4. accept等待客户端的连接（等待别人的电话到来）
        print("等待一个客户端的访问")
        # 拆包
        client_socket, client_addr = tcp_server.accept()
        # 接收客户端的请求
        recv_data = client_socket.recv(1024)
        print(recv_data)

        # 回送一部分数据给客户端
        client_socket.send("hahha".encode('utf-8'))

        # 关闭套接字
        # 关闭accept返回的套接字，意味着不会再为这个客户端服务
        client_socket.close()
    # 如果将监听套接字关闭了，那么会导致不能再次等待新客户端的到来，accept就会失败
    tcp_server.close()


if __name__ == '__main__':
    main()

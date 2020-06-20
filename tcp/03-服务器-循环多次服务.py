import socket


# 买电话，插入电话卡，打开电话铃声监听，等待别人的电话

def main():
    # 1. 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 绑定端口
    tcp_socket.bind(("", 7788))

    # 3. 将套接字设置为监听
    tcp_socket.listen(128)

    while True:
        print("等待一个客户端的到来。。。")
        # 4. 等待别人的电话到来(等待客户端的连接)
        client_socket, client_addr = tcp_socket.accept()
        print("一个新的客户端已经到来%s" % str(client_addr))
        while True:
            # 5. 接收客户端发送的请求
            recv_data = client_socket.recv(1024)
            print("客户端发送过来的请求是: %s" % recv_data.decode('utf-8'))
            # 如果recv解堵塞，那么有两种方式：
            # 1. 客户端发送数据
            # 2. 客户端调用了close导致了recv解阻塞
            # if 后面如果是数字且不是零，或者是元祖列表且不为空，都成立
            if recv_data:
                tcp_socket.send("hahhah---ok-----".encode('uft-8'))
            else:
                # 两个while true中有break只会跳出最近的那个
                break

            # 回送一部分数据给客户
            client_socket.send("hhahahah-----ok-----".encode('utf-8'))
        # 关闭套接字
        # 关闭accept返回的套接字，意味着不再为这个客户端进行服务
        client_socket.close()
        print("该次服务已经完毕")

    tcp_socket.close()


if __name__ == '__main__':
    main()

import socket


# 具有独立的功能
def send_file_2_client(tcp_client_socket, client_addr):
    # 1. 接收客户端发送过来的要下载的文件名
    # 链式编程
    file_name = tcp_client_socket.recv(1024).decode('utf-8')
    print("客户端(%s)需要下载的文件是：%s" % (str(client_addr), file_name))
    # 3. 打开这个文件并读取数据
    # with的前提是可以打开，一般是写文件，也就是新建文件的时候使用with
    file_content = None

    try:
        f = open(file_name, "rb")
        file_content = f.read()
    except Exception as ret:
        print("没有找到文件(%s)" % file_name)
    # 4. 发送文件数据给客户端
    if file_content:
        # 回写一部分数据给客户端
        tcp_client_socket.send(file_content)


def main():
    # 1. 买个手机（创建套接字 socket）
    # 被动套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 插入手机卡（绑定ip和端口号）
    tcp_server_socket.bind(("", 7788))
    # 3. 设置未响铃模式
    tcp_server_socket.listen(128)
    while True:
        # 4. 等待别人来电
        tcp_client_socket, client_addr = tcp_server_socket.accept()
        # 5. 调用发送文件函数，完成客户端服务
        send_file_2_client(tcp_client_socket, client_addr)
        # 关闭套接字
        tcp_client_socket.close()

    tcp_server_socket.close()


if __name__ == '__main__':
    main()

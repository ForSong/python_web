import socket


def main():
    # 1. 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 获取服务器的ip和端口号
    server_ip = input("请输入服务器地址")
    server_port = int(input("请输入端口号"))
    server_addr = (server_ip, server_port)

    # 3. 连接服务器
    tcp_socket.connect(server_addr)
    # 4. 获取下载的文件名
    download_file_name = input("请输入要下载的文件名")
    # 5. 将文件名字发送到服务器
    tcp_socket.send(download_file_name.encode('utf-8'))
    # 6. 接收文件中的数据
    recv_data = tcp_socket.recv(1024)  # 1Kb
    # 7. 保存接收到的数据到一个文件中
    # 下面的with代码是对：
    # f = open("xxx")
    # try:
    #   f.write()/read()
    #   except:
    #       f.close()
    # 这段代码的简写
    # 以w的方式打开，以二进制写入
    if recv_data:
        with open("[新]" + download_file_name, "wb") as f:
            f.write(recv_data)

    # 8. 关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()

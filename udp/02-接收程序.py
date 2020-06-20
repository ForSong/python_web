from socket import *


def main():

    # 发送数据的流程：创建套接字，发送数据，关闭
    # 接收数据的流程：创建套接字，绑定本地自己的信息(ip和port)，接收数据，关闭

    # 1. 创建套接字
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    # 2. 绑定本地的相关ini，如果一个网络程序不绑定，系统就会随机分配
    local_address = ('', 7788)  # ip地址和端口号，ip一般不用写，表示本机的任何一个ip
    # 保证端口号固定
    udp_socket.bind(local_address)  # 必须绑定自己电脑的ip和port

    while True:
        # 接收数据
        # 3. 等待接收对方发送的数据，参数表示接收的最大值
        # recv_data存储的是一个元祖(接收到的数据, (发送方的ip, port))
        recv_data = udp_socket.recvfrom(1024)
        recv_message = recv_data[0]  # 发送的信息，返回是一个utf-8的字节码
        send_addr = recv_data[1]  # 发送的地址，返回的是一个元祖
        if recv_message.decode('utf-8') == '关闭':
            print("谢谢使用，再见")
            break
        # 4. 显示接收到的数据
        print("%s:%s" % (str(send_addr), recv_message.decode('utf-8')))

    # 5. 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()

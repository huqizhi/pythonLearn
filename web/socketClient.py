import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host,port))
while True:
    data = input('> ')
    if not data:
        s.close()
        break
    try:
        s.send(data.encode())
        data = s.recv(1024).decode()
        print("返回：", data)
    except:
        print("服务已关闭")
        s.close()
        break;

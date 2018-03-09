import socket
import _thread
from time import ctime

# 为线程定义一个函数
def sockethandle(c,addr, delay):
    print("创建新线程：",addr)
    while True:
        try:
            data = c.recv(1024).decode()
            print("收到", addr, "：", data)
        except:
            print("客户端",addr,"：强制关闭")
            break

        if not data:
            print("客户端", addr, "：正常关闭")
            c.close()
            break
        else:
            c.send(('[%s] %s' % (ctime(), '服务器')).encode())

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    _thread.start_new_thread(sockethandle,(c,addr,2))
s.close()

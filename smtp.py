# coding=utf-8

from socket import *
import base64


SMTP_SERVER = 'smtp.exmail.qq.com'
FROM = 'me@gladuo.com'
TO = '564843720@qq.com'
SUBJECT = '666'
CONTENT = '就是666'


def connect():
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((SMTP_SERVER, 25))
    recv = client_socket.recv(1024)
    print recv
    return client_socket


def HELO(client_socket):
    command = 'HELO localhost\r\n'
    print command
    client_socket.send(command)
    recv = client_socket.recv(1024)
    print recv


def AUTH_LOGIN(client_socket):
    command = 'AUTH LOGIN\r\n'
    print command
    client_socket.send(command)
    recv = client_socket.recv(1024)
    print recv
    base64_user = base64.encodestring(FROM)
    print base64_user
    client_socket.send(base64_user+'\r\n')
    recv = client_socket.recv(1024)
    print recv
    print '******'
    client_socket.send('MjEwM--lalala--pZHVv\r\n')  # 要用 base64, 当然这里我是改了几个字符的啦
    recv = client_socket.recv(1024)
    print recv


def MAIL(client_socket):
    print 'RCPT TO: '+TO
    client_socket.send('RCPT TO: '+TO+'\r\n')
    recv = client_socket.recv(1024)
    print recv
    print 'MAIL FROM: '+FROM
    client_socket.send('MAIL FROM: '+FROM+'\r\n')
    recv = client_socket.recv(1024)
    print recv
    command = 'DATA'
    print command
    client_socket.send(command+'\r\n')
    recv = client_socket.recv(1024)
    print recv
    END_MSG = '\r\n.\r\n'
    data_msg = 'Date: Sat, 15 Apr 1995 02:33:00 +0800\r\n'
    from_msg = 'from: '+FROM.split('@')[0]+' '+FROM+'\r\n'
    to_msg = 'to: '+TO.split('@')[0]+' '+TO+'\r\n'
    subject = 'subject: '+SUBJECT+'\r\n'
    content = '\r\n'+CONTENT+'\r\n'
    msg = data_msg+from_msg+to_msg+subject+content+END_MSG
    print msg
    client_socket.send(msg)
    recv = client_socket.recv(1024)
    print recv


def disconnetc(client_socket):
    command = 'QUIT'
    print command
    client_socket.send(command+'\r\n')
    recv = client_socket.recv(1024)
    print recv


def send_email():
    client_socket = connect()
    HELO(client_socket)
    AUTH_LOGIN(client_socket)
    MAIL(client_socket)
    disconnetc(client_socket)

if __name__ == '__main__':
    send_email()

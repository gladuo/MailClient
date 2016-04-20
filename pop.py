# coding=utf-8

from socket import *

POP3_SERVER = 'pop.exmail.qq.com'
USER = 'web@gladuo.com'
PASS = '--lalala--'


def connect():
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((POP3_SERVER, 110))
    recv = client_socket.recv(1024)
    print recv
    return client_socket


def login(client_socket):
    command = 'USER '+USER+'\r\n'
    print command
    client_socket.send(command)
    recv = client_socket.recv(1024)
    print recv
    command = 'PASS '+PASS+'\r\n'
    print 'PASS '+'******'+'\r\n'
    client_socket.send(command)
    recv = client_socket.recv(1024)
    print recv


def get_stat(client_socket):
    command = 'STAT'+'\r\n'
    print command
    client_socket.send(command)
    recv = client_socket.recv(1024)
    print recv
    return int(recv.split(' ')[1])


def get_email(client_socket, email_id=1):
    command = 'RETR '+str(email_id)+'\r\n'
    print command
    client_socket.send(command)
    recv = client_socket.recv(1024)
    print recv
    recv = client_socket.recv(1024)
    print recv


def disconnetc(client_socket):
    command = 'QUIT'
    print command
    client_socket.send(command+'\r\n')
    recv = client_socket.recv(1024)
    print recv


def pop3_mail():
    client_socket = connect()
    login(client_socket)
    num = get_stat(client_socket)
    get_email(client_socket, num)
    disconnetc(client_socket)

if __name__ == '__main__':
    pop3_mail()

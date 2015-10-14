#!/usr/bin/env python
# -*- coding: utf8 -*-
# Cheack_IP.py
# Author: Jiangmf
# Date: 2014-08-22
import subprocess
import re
user = 'root'
host = 'localhost'
port = '22'
privatekey = '~/.ssh/id_rsa'


def read_from_cnf():
    m1 = re.search(r'\[ssh\].+', open('my.cnf', 'rb').read(), re.DOTALL)
    if m1:
        for line in m1.group().split('\n')[1:]:
            name = line.split('=')[0]
            if name in globals():
                globals()[name] = line.split('=')[1]

if __name__ == "__main__":
    read_from_cnf()
    command1 = "sftp -b ./sftp_cmds.txt -i {} -P {} {}@{}:/etc/apache2".format(
               privatekey, port, user, host)
    command2 = "ssh -i {} -p {} {}@{} \"service apache2 reload\"".format(
               privatekey, port, user, host)
    p0 = subprocess.Popen("echo Connecting to sftp server...",shell=True)
    p0.wait()
#    print command1
#    print command2
    p1 = subprocess.Popen(command1,shell=True)
    p1.wait()
    p2 = subprocess.Popen(command2,shell=True)
    p2.wait()

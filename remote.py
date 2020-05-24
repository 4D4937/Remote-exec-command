#!/usr/bin/python
# -- coding: utf-8 --
 
import paramiko
from optparse import OptionParser
from sys import argv
 
 
def ssh2(ip, port, username, password, cmd):
    for hosts in ip:
        try:
            paramiko.util.log_to_file('paramiko__.log')
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hosts, port, username, password, timeout=7)
            stdin, stdout, stderr = ssh.exec_command(cmd)
            cmd_result = stdout.read(), stderr.read()
            print '%s --> command has been submitted, results are as follows.' % (hosts)
            for o in cmd_result:
                print o,
            ssh.close()
            print "\n"
        except Exception, msg:
            print hosts, msg
 
 
if __name__ == '__main__':
 
    parser = OptionParser()
    parser.add_option("--ip",
                      dest="ipaddr",
                      help="target host ip address"
                      )
    parser.add_option("--ipfile",
                      dest="ipfile",
                      help="ip list file"
                      )
    parser.add_option("--port",
                      dest="port",
                      help="ssh port number"
                      )
    parser.add_option("--username",
                      dest="username",
                      help="ssh user name"
                      )
    parser.add_option("--password",
                      dest="password",
                      help="ssh password"
                      )
    parser.add_option("--cmd",
                      dest="cmd",
                      help="Commands to execute"
                      )
 
    (options, args) = parser.parse_args()
    if "--ip" in argv and "--ipfile" in argv:
        print "Accept only one argument, use  --ip or --ipfile"
        exit(1)
    if options.ipaddr == None:
        ip_list = open(options.ipfile, "r")
        ip = ip_list.read().split("\n")[:-1]
        ip_list.close()
 
    if options.ipfile == None:
        ip_list = options.ipaddr
        ip = ip_list.split(",")
 
    cmd = options.cmd
    port = int(options.port)
    username = options.username
    password = options.password
 
    ssh2(ip, port, username, password, cmd)
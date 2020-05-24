# Remote-exec-command
### install
``` bash
apt-get update
apt-get install gcc g++ openssl libssl-dev python-dev python-pip libffi-dev
pip install pycrypto
pip install paramiko
```
### example
``` bash
python run_cmd.py --ip 192.168.1.22 --port 22 --username root --password 123456 --cmd "ls -l"
```
``` bash
python remote.py --ip 192.168.7.19,192.168.7.20,192.168.10.177,192.168.73.145 --port 22 --username root --password 123456 --cmd "ls -l"
```
``` bash
python remote.py --ipfile /root/ip.txt --port 22 --username root --password 123456 --cmd "ls -l"
```

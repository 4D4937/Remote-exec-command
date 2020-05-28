# Install
``` bash
apt-get update
apt-get install gcc g++ openssl libssl-dev python-dev python-pip libffi-dev
pip install pycrypto paramiko
git clone https://github.com/4D4937/Remote-exec-command
```
# Usage
remote.py [options]
``` bash
Options:
  -h, --help           show this help message and exit
  --ip=IPADDR          target host ip address
  --ipfile=IPFILE      ip list file
  --port=PORT          ssh port number
  --username=USERNAME  ssh user name
  --password=PASSWORD  ssh password
  --cmd=CMD            Commands to execute
```
# Example
``` bash
python remote.py --ip 192.168.1.22 --port 22 --username root --password 123456 --cmd "ls -l"
```
``` bash
python remote.py --ip 192.168.7.19,192.168.7.20,192.168.10.177,192.168.73.145 --port 22 --username root --password 123456 --cmd "ls -l"
```
``` bash
python remote.py --ipfile ip.txt --port 22 --username root --password 123456 --cmd "ls -l"
```
# Error
-bash: !”: event not found"
``` bash
set +H
```

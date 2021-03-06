#!/usr/bin/python3

# this script connects to a mysql database via ssh

import pymysql
import paramiko
import pandas as pd
import os
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
from os.path import expanduser
from pathlib import Path
from dotenv import load_dotenv

# get private key from local .pem file
home = expanduser('~')
mypkey = paramiko.RSAKey.from_private_key_file(home + '/.ssh/authorized_keys.pem')

# set path to local credentials file
load_dotenv()
env_path = Path(home + '/.ssh') / '.env'
load_dotenv(dotenv_path=env_path)

# set variables for database access
sql_hostname = os.getenv('SQL_HOSTNAME')
sql_username = os.getenv('SQL_USERNAME')
sql_password = os.getenv('SQL_PASSWORD')
sql_main_database = os.getenv('SQL_MAIN_DATABASE')
sql_port = 3306
ssh_host = os.getenv('SSH_HOST')
ssh_user = os.getenv('SSH_USER')
ssh_port = 22
sql_ip = '1.1.1.1.1'

with SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_user,
        ssh_pkey=mypkey,
        remote_bind_address=(sql_hostname, sql_port)) as tunnel:
    conn = pymysql.connect(host='127.0.0.1', user=sql_username,
            passwd=sql_password, db=sql_main_database,
            port=tunnel.local_bind_port)
    query = '''select * from my_table where id = 12345678'''          # enter in database query here
    data = pd.read_sql_query(query, conn)
    conn.close()

#print data to console
    print(data)

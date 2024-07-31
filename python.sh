#!/usr/bin/env bash

set password $env(sudo_password)
spawn sudo apt-get install -y python3.8 python3.8-venv python3.8-dev
expect "password for" 
send "$password\r"
spawn python3.8 --version
expect eof



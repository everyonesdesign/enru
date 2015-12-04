#!/usr/bin/env bash

cd `dirname $0`
pip install -r ./requirements.pip

#move ruby file to lib folder and let execute it
cp ./enru.py /usr/local/lib/enru.py
chmod +x /usr/local/lib/enru.py

#move executable to /bin folder
cp ./enru.sh /usr/local/bin/enru
chmod +x /usr/local/bin/enru
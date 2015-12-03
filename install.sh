#!/usr/bin/env bash

cd `dirname $0`
pip install -r ./requirements.pip

#move ruby file to lib folder and let execute it
mkdir /usr/lib/enru -p
cp ./enru.py /usr/lib/enru/enru.py
chmod +x /usr/lib/enru/enru.py

#move executable to /bin folder
cp ./enru.sh /usr/bin/enru
chmod +x /usr/bin/enru
apt update 
apt-get install python3.8 python3.8-dev build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev -y
rm /usr/bin/python3
ln -s python3.8 /usr/bin/python3
python3 -m pip install -U pip
pip3 install -r req.txt

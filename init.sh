sudo apt update 
sudo apt-get install python3.8 python3.8-dev build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev -y
sudo rm /usr/bin/python3
sudo ln -s python3.8 /usr/bin/python3
sudo python3 -m pip install -U pip
pip3 install -r req.txt

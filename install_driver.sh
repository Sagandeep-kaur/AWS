# Download and Install chromedriver
wget -N https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.85/linux64/chrome-linux64.zip -P ~/
unzip ~/chrome-linux64.zip -d ~/
rm ~/chrome-linux64.zip
sudo mv -f ~/chrome /usr/local/bin/chrome
sudo chown root:root /usr/local/bin/chrome
sudo chmod 0755 /usr/local/bin/chrome


# Install chrome broswer
curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
apt-get -y update
apt-get -y install google-chrome-stable

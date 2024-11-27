#!/bin/sh
#get latest version
version=`curl http://chromedriver.storage.googleapis.com/LATEST_RELEASE)`;
echo 'Currently LATEST_RELEASE:' $version;
#download the latest version chrome driver available as per the above line
wget -N http://chromedriver.storage.googleapis.com/${version}/chromedriver_linux64.zip
unzip chromedriver_linux64.zip -d /usr/local/bin
chmod a+x /usr/local/bin/chromedriver
#upgrade to latest google chrome
yum upgrade google-chrome-stable
google_version=`google-chrome --version`;
echo 'Google Chrome Version:' $google_version;
echo 'Currently LATEST_RELEASE:' $version;
echo 'End of the script'
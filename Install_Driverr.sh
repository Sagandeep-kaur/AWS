yum update
ex /etc/yum.repos.d/google-chrome.repo << END
i
[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64
enabled=1
gpgcheck=1
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub
.
wq
END
#vi /etc/yum.repos.d/google-chrome.repo
#[google-chrome]
#name=google-chrome
#baseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64
#enabled=1
#gpgcheck=1
#gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub
sudo yum install google-chrome-stable

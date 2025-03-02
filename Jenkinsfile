pipeline {
    agent any
   
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // Add build steps here, like mvn clean install or npm run build
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                bat 'curl -L https://www.python.org/ftp/python/3.9.10/python-3.9.10.exe -o python-installer.exe'
                bat 'python-installer.exe /quiet InstallAllUsers=1 PrependPath=1' 
                bat 'python3 test_hello.py'
                // Add test steps here, like running unit tests
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Add deployment steps here
            }
        }
    }
}

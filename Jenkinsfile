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
                bat 'apt install python3 -y'
                bat 'python3 --version'
                sh 'python3 --version'
                sh 'python3 test_hello.py'
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

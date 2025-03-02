pipeline {
    agent any
    tools {
        python 'Python3'  // 'python3' should be the name of the Python installation you configured in Jenkins
    }
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
                sh 'python test_hello.py'
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

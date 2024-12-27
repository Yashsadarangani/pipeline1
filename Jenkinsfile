pipeline {
    agent any
    environment {
        PYTHON_PATH = 'C:\\Users\\Yashu Kun\\AppData\\Local\\Programs\\Python\\Python312;C:\\Users\\Yashu Kun\\AppData\\Local\\Programs\\Python\\Python312\\Scripts'
        PATH = "${PATH};C:\\Windows\\System32"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                pip install -r requirements.txt
                '''
            }
        }
        stage('SonarAnalysis') {
            environment {
                SONAR_TOKEN = credentials('sonarqube-credential')
            }
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                sonar-scanner -Dsonar.projectKey=pipeline1 ^
                -Dsonar.sources=. ^
                -Dsonar.host.url=http://localhost:9000 ^
                -Dsonar.token=%SONAR_TOKEN%
                '''
            }
        }
    }
    post {
        success {
            echo 'Build Succeeded!'
        }
        failure {
            echo 'Build Failed'
        }
    }
}

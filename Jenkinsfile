pipeline {
    agent any
    
    environment {
        // Define the SonarQube credentials environment variable
        SONARQUBE_CREDENTIALS = credentials('sonarqube-credentials') // Replace with your SonarQube credentials ID
    }
    
    stages {
        stage('Checkout SCM') {
            steps {
                // Checkout the code from the Git repository
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install necessary dependencies (e.g., Python dependencies)
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    // Run SonarQube analysis
                    withSonarQubeEnv('SonarQube') {
                        // Replace 'SonarQube' with the name of your configured SonarQube server
                        sh 'mvn clean verify sonar:sonar -Dsonar.login=$SONARQUBE_CREDENTIALS_USR -Dsonar.password=$SONARQUBE_CREDENTIALS_PSW'
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                // Wait for SonarQube quality gate status
                script {
                    def qualityGate = waitForQualityGate()
                    if (qualityGate.status != 'OK') {
                        error "Pipeline aborted due to SonarQube Quality Gate failure: ${qualityGate.status}"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                // Deployment steps (e.g., deploy to a server)
                echo 'Deploying application...'
            }
        }
    }

    post {
        always {
            // Any steps to run after the pipeline finishes
            echo 'Pipeline finished.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}

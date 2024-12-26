pipeline{
  agent any
  environment{
    PYTHON_PATH='C:\Users\Yashu Kun\AppData\Local\Programs\Python\Python312';'C:\Users\Yashu Kun\AppData\Local\Programs\Python\Python312\Scripts'
  }
  stages{
    stage('Checkout'){
      steps{
        checkout sum
      }
    }
    stage('Build'){
      steps{
        bat '''
        set PATH=%PYTHON_PATH%;%PATH%
        pip install -r requirements.txt
        '''
      }
    }
    stage('SonarAnalysis'){
      environment{
        SONAR_TOKEN=credentials('sonarqube-credentials')
      }
      steps{
        bat '''
        set PATH=%PYTHON_PATH%;%PATH%
        sonar-scanner ^
        -Dsonar.projectKey=pipeline1 ^
        -Dsonar.projectName=pipeline1 ^
        -Dsonar.sources=. ^
        -Dsonar.host.url=http://localhost:9000 ^
        -Dsonar.token=sqp_4b98b9332396c286d2af87f1860d0cf3fcca4cf7
        '''
      }
    }
  }
  post{
    success{
      echo "Went Well and Good"
    }
    failure{
      echo "Something went wrong"
    }
  }
}

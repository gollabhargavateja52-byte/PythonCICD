pipeline{
    agent any 
    stages{
        stage('Checkout'){
            steps{
                bat 'python --version'
            }
        }
        stage("Install requirements"){
            steps{
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }
        stage("Run tests"){
            steps{
                bat 'pyinstaller --onefile app.py'
            }
        }
    }
    post{
        success{
            echo "Build and tests completed successfully."
        }
        failure{
            echo "Build or tests failed."
        }
    }
}
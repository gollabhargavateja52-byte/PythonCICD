pipeline {
    agent any

    stages {

        stage('Python Version') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Install Requirements') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Application') {
            steps {
                sh 'pyinstaller --onefile app.py'
            }
        }
    }

    post {

        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}
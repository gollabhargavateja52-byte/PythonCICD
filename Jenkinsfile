pipeline {
    agent any

    stages {

        stage('Git Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/bhargavateja001/python-app.git'
            }
        }

        stage('Python Version') {
            steps {
                bat 'python --version'
            }
        }

        stage('Upgrade pip') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip --version'
            }
        }

        stage('Install Requirements') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Install PyInstaller') {
            steps {
                bat 'pip install pyinstaller'
            }
        }

        stage('Run Unit Test') {
            steps {
                bat 'python -m unittest test_app.py'
            }
        }

        stage('Create EXE') {
            steps {
                bat 'pyinstaller --onefile app.py'
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
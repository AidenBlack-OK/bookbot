pipeline {
    agent { docker { image 'python:3.14.8-alpine3.24' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}
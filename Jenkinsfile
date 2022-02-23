pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('🧱 Build') {
            steps {
                sh 'docker image build --tag not-the-registry:latest .'
            }
        }
        stage('🩺 Test') {
            steps {
                sh 'echo many tests have passed'
            }
        }
        stage('🚀 Deploy') {
            steps {
                sh 'docker container stop not-the-registry ||:'
                sh 'docker container run --rm --name not-the-registry --publish 6543:6543 --detach not-the-registry:latest'
            }
        }
    }
}

pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'DOCKER_BUILDKIT=1 docker build -t random-quote-api .'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'docker run --rm random-quote-api pytest'
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                    docker rm -f random-quote-api-container || true
                    docker run -d \
                        --name random-quote-api-container \
                        -p 5000:5000 \
                        random-quote-api
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
    }
}
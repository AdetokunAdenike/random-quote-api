pipeline {
    agent any

    environment {
        IMAGE_NAME = 'random-quote-api'
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    DOCKER_BUILDKIT=1 docker build \
                        -t ${IMAGE_NAME}:${IMAGE_TAG} \
                        .
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    docker run --rm \
                        ${IMAGE_NAME}:${IMAGE_TAG} \
                        pytest
                '''
            }
        }
    }

    post {
        success {
            echo "CI pipeline completed successfully!"
            echo "Docker image: ${IMAGE_NAME}:${IMAGE_TAG}"
        }

        failure {
            echo 'CI pipeline failed. Check the logs for details.'
        }
    }
}
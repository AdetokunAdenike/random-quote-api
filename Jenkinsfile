pipeline {
    agent any

    environment {
        IMAGE_NAME = 'random-quote-api'
        IMAGE_TAG = "${BUILD_NUMBER}.0"
        TEST_IMAGE = "${IMAGE_NAME}:test-${BUILD_NUMBER}"
    }

    stages {

        stage('Build Test Image') {
            steps {
                sh '''
                    docker build \
                        --pull \
                        --target test \
                        -t ${TEST_IMAGE} .
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    docker run --rm \
                        ${TEST_IMAGE} \
                        pytest
                '''
            }
        }

        stage('Build Production Image') {
            steps {
                sh '''
                    docker build \
                        --pull \
                        --target production \
                        -t ${IMAGE_NAME}:${IMAGE_TAG} .
                '''
            }
        }

        stage('Security Scan') {
            steps {
                sh '''
                    trivy image \
                        --severity HIGH,CRITICAL \
                        --exit-code 1 \
                        ${IMAGE_NAME}:${IMAGE_TAG}
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
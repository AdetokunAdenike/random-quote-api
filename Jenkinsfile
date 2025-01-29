pipeline {
    agent any // Run on any available Jenkins agent

    stages {
        stage('Checkout Code') {
            steps {
                // Clone the repository from GitHub using stored credentials
                git branch: 'master', url: 'https://github.com/AdetokunAdenike/random-quote-api.git',
                credentialsId: 'github-credentials'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build a Docker image using BuildKit for better performance
                sh 'DOCKER_BUILDKIT=1 docker build -t random-quote-api .'
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Run unit tests inside a temporary Docker container
                sh 'docker run --rm random-quote-api pytest'
            }
        }

        stage('Deploy Application') {
            steps {
                // Deploy the application by running the container in detached mode
                sh 'docker run -d -p 5000:5000 random-quote-api'
            }
        }
    }

    post {
        success {
            // Message displayed when the pipeline completes successfully
            echo 'Pipeline executed successfully!'
        }
        failure {
            // Message displayed if any stage fails
            echo 'Pipeline failed. Check logs for details.'
        }
    }
}

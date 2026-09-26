# Containerized CI/CD Pipeline & AWS Infrastructure Automation

A containerized Python REST API used to demonstrate a practical DevOps workflow involving Docker, Jenkins CI, container security scanning, AWS infrastructure provisioning, and Infrastructure as Code with Terraform.

The project is being developed as a reproducible cloud deployment pipeline, with the application and infrastructure managed through version control.

## Architecture

```text
Developer
   │
   │ Git Push
   ▼
GitHub Repository
   │
   ▼
Jenkins
   │
   ├── Build Test Image
   ├── Run Pytest
   ├── Build Production Image
   └── Trivy Security Scan
   │
   ▼
Docker Image
   │
   ▼
Amazon ECR
   │
   ▼
AWS Infrastructure
   │
   ├── VPC
   ├── Public Subnet
   ├── Internet Gateway
   ├── Route Table
   └── ECS Task Security Group
   │
   ▼
ECS/Fargate
   └── Deployment stage — in progress
```

## Technologies

- Python
- Flask
- Pytest
- Docker
- Jenkins
- Groovy / Jenkins Pipeline
- Trivy
- Git & GitHub
- Terraform
- AWS
  - Amazon ECR
  - Amazon VPC
  - Subnets
  - Internet Gateway
  - Route Tables
  - Security Groups
  - Amazon ECS/Fargate (planned)

## Application

The application is a simple REST API that provides random quotes.

### Endpoints

```text
GET /
GET /api/quotes
GET /api/quotes/random
GET /api/quotes/<id>
```

## Docker

The application is containerized using Docker.

The Docker configuration uses a multi-stage build to separate the testing environment from the production image.

### Test image

```bash
docker build --target test -t random-quote-api:test .
```

Tests can then be executed inside the container:

```bash
docker run --rm random-quote-api:test pytest
```

### Production image

```bash
docker build --target production -t random-quote-api:latest .
```

The production container runs the application using Gunicorn.

## Jenkins CI Pipeline

Jenkins is used to automate the Continuous Integration workflow.

The current pipeline performs:

```text
Source Checkout
      ↓
Build Test Image
      ↓
Run Tests
      ↓
Build Production Image
      ↓
Trivy Security Scan
```

### Build Test Image

Jenkins builds the Docker image using the test stage.

### Run Tests

The test image is executed and the application's Pytest test suite is run inside the container.

### Build Production Image

After the tests pass, Jenkins builds the production Docker image.

Images are tagged using the Jenkins build number.

Example:

```text
random-quote-api:6.0
```

### Security Scan

Trivy scans the production Docker image for HIGH and CRITICAL vulnerabilities.

The Jenkins pipeline is configured to fail if vulnerabilities meeting the configured severity threshold are detected.

## Amazon ECR

Amazon Elastic Container Registry (ECR) is used as the container image registry for the application.

The ECR repository is provisioned through Terraform.

Configuration includes:

- Mutable image tags
- Scan-on-push enabled

Repository:

```text
random_quote_api
```

## Infrastructure as Code

AWS infrastructure is provisioned using Terraform.

The Terraform configuration is maintained under:

```text
terraform/
```

The infrastructure is managed through a dedicated Git branch:

```text
terraform-deployment
```

This keeps the infrastructure work separate from the application's main development branch.

## AWS Infrastructure Provisioned

### Amazon ECR Repository

Stores Docker images produced by the CI pipeline.

Terraform resource:

```text
aws_ecr_repository.random_quote_api
```

### VPC

A custom VPC is created for the application:

```text
CIDR: 10.0.0.0/16
```

### Public Subnet

A single public subnet is currently used:

```text
Availability Zone: eu-north-1a
CIDR: 10.0.1.0/24
```

A single Availability Zone is intentional for this learning project to keep the infrastructure simple and minimize unnecessary AWS resources.

### Internet Gateway

An Internet Gateway provides internet connectivity for resources in the public subnet.

### Route Table

A public route table is configured with:

```text
0.0.0.0/0 → Internet Gateway
```

### ECS Task Security Group

A security group has been created for the future ECS task.

Current rules:

```text
Inbound:
TCP 5000 from 0.0.0.0/0

Outbound:
All traffic
```

Port `5000` matches the port exposed by the application container.

## Terraform Workflow

Infrastructure changes are managed using the standard Terraform workflow:

```bash
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
```

Terraform state files are excluded from Git:

```text
*.tfstate
*.tfstate.*
```

The Terraform provider lock file is committed to version control:

```text
.terraform.lock.hcl
```

## Current Progress

### Completed

- [x] Python REST API
- [x] Automated tests with Pytest
- [x] Docker containerization
- [x] Multi-stage Docker build
- [x] Jenkins CI pipeline
- [x] Automated Docker image builds
- [x] Trivy container security scanning
- [x] Amazon ECR repository
- [x] Terraform initialization
- [x] Custom AWS VPC
- [x] Public subnet
- [x] Internet Gateway
- [x] Public route table
- [x] ECS task security group
- [x] AWS infrastructure managed through Terraform

### In Progress

- [ ] ECS cluster
- [ ] ECS Fargate task definition
- [ ] ECS service
- [ ] Deploy container to ECS/Fargate
- [ ] Connect Jenkins CI pipeline to ECR
- [ ] Automated deployment workflow
- [ ] Application deployment verification

## Project Goals

The goal of this project is to demonstrate a reproducible DevOps workflow:

```text
Code
 ↓
Git
 ↓
Jenkins CI
 ↓
Automated Tests
 ↓
Docker Build
 ↓
Security Scan
 ↓
Amazon ECR
 ↓
Terraform Infrastructure
 ↓
ECS/Fargate Deployment
```

# DevOps Projects Portfolio

This repository contains **three beginner-friendly DevOps projects** demonstrating Python development, cloud infrastructure, Docker, and CI/CD concepts. You can download the zip files to explore the code.

---

## 1️⃣ DevOps Flask Web App

* **Technologies:** Python, Flask, Docker, GitHub Actions (CI/CD)
* **Description:** A simple Flask web application containerized with Docker and configured with a CI/CD pipeline using GitHub Actions.
* **File:** `devops-flask-app.zip`
* **Resume bullet idea:** Built a containerized Python Flask app with automated CI/CD pipeline using Docker and GitHub Actions.
* **Quick start:**

```bash
docker run -p 5000:5000 devops-flask-app
```

---

## 2️⃣ Cloud Infrastructure Automation

* **Technologies:** AWS, Terraform, Ansible
* **Description:** A demo project showing infrastructure as code with Terraform to provision an EC2 instance and Ansible to configure Nginx.
* **File:** `cloud-infra-automation.zip`
* **Resume bullet idea:** Automated AWS infrastructure provisioning using Terraform and server configuration with Ansible.

---

## 3️⃣ Python CLI Utility with Docker

* **Technologies:** Python, Docker, GitHub Actions
* **Description:** A command-line Python application that counts lines in a log file. The application is packaged into a Docker container and has a GitHub Actions workflow to automate Docker image build and push.
* **File:** `python-cli-docker.zip`
* **Resume bullet idea:** Developed a Python CLI tool, containerized it with Docker, and implemented CI/CD to Docker Hub using GitHub Actions.
* **Quick start:**

### Run Locally

```bash
cd python-cli-docker/cli_tool
python log_analyzer.py ../sample.log
```

### Run with Docker

```bash
docker build -t python-cli-docker .
docker run --rm -v $(pwd):/data python-cli-docker /data/sample.log
```

---

## How to Use

1. Download the zip files from this repo.
2. Extract each project folder.
3. Follow the README inside each zip for instructions on running locally or in Docker.

---

### Optional Tips

* Add badges for Python version, Docker build, GitHub Actions CI status (can be added later).
* Add Preview/Screenshot section once the Flask app is deployed or infrastructure is set up.

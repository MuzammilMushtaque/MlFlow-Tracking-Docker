# MLflow Tracking with Docker

![MLflow Logo](mlflow-logo.png)

## Overview

MLflow is an open-source platform designed to manage the end-to-end machine learning lifecycle. With MLflow, you can track experiments, package code into reproducible runs, and share and deploy models. This project demonstrates how to use MLflow Tracking to log experiments, metrics, parameters, and artifacts using Docker for a seamless environment setup.

## Features

- **Experiment Tracking**: Easily log and compare multiple runs with different models and hyperparameters.
- **System Metrics**: Log system metrics like CPU and memory usage during model training.
- **Model Management**: Log and manage trained models along with their performance metrics.
- **Artifact Storage**: Store generated artifacts such as confusion matrices for easy retrieval and analysis.

## Getting Started

### Prerequisites

- Docker installed on your machine.
- Basic knowledge of machine learning and Python.

### Project Structure

- **Dockerfile**: Instructions to build the Docker image.
- **MLFlow_2.py**: Python script containing the model training and MLflow tracking logic.
- **requirements.txt**: List of Python packages required for the project.
- **README.md**: Project documentation.

## Running the Project

### Step 1: Build the Docker Image

Open a terminal, navigate to your project directory, and run:
```bash
docker build -t mlflow-tracking-1 .
```

### Step 2: Run the Docker Container

Run the container and map port 5000 from the container to port 5000 on your host machine:
```bash
docker run -p 5000:5000 mlflow-tracking-1
```

## MLflow UI

Once the container is running, open your web browser and navigate to `http://localhost:5000` to access the MLflow UI. Here, you can:

- **Track Experiments**: View all runs, compare their performance, and analyze metrics.
- **Visualize Metrics**: Generate and view various plots to understand model performance.
- **Inspect Artifacts**: Examine generated artifacts such as confusion matrices and model files.

## Importance of MLflow

MLflow simplifies the process of managing machine learning experiments. It ensures that experiments are reproducible, models are easy to manage, and results are straightforward to compare. By using MLflow, you can focus more on developing models and less on the operational challenges of managing them.

## Conclusion

The code used in this demonstration is provided in the description below. It works within a Docker environment, so please check it out and modify it to suit your needs. Thank you!

---

### Tags

![Python](https://img.shields.io/badge/Python-3.9-blue)
![MLflow](https://img.shields.io/badge/MLflow-1.14.0-blue)
![Docker](https://img.shields.io/badge/Docker-19.03.12-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-0.24.2-orange)
![matplotlib](https://img.shields.io/badge/matplotlib-3.4.2-red)
![seaborn](https://img.shields.io/badge/seaborn-0.11.2-green)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


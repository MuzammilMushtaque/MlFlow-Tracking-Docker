FROM continuumio/miniconda3

WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies
RUN conda env create -f conda.yaml

# Activate the environment
RUN echo "source activate wine-env" > ~/.bashrc
ENV PATH /opt/conda/envs/wine-env/bin:$PATH

# Install MLflow
RUN pip install mlflow

pip install -r requirements.txt

# Expose port for MLflow UI
EXPOSE 5000

# Command to run the project
# CMD mlflow run . -P n_estimators=100 -P max_depth=3

# Command to run the project (new)
CMD ["bash", "-c", "mlflow run ."]
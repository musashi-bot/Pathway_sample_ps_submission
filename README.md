#   Overview
This repository contains two independent tasks:

- **Task 1:** Setting up a Dockerized environment for a Pathway-based data pipeline application.
- **Task 2:** Building and evaluating an LSTM model for Bitcoin price prediction using historical data and technical indicators.

---

##   Task 1 – Docker Setup for Pathway Application

###  Description
The goal of Task 1 was to containerize a **Pathway** application and ensure it runs consistently in any environment.  
The application processes data streams and writes results to a JSON file.

###  Key Components
- **Pathway**: Stream processing and incremental computation framework.  
- **Docker**: Used to isolate dependencies and create a reproducible runtime environment.  
- **Output file:** `output.json`

###  Steps Implemented
1. **Create a `Dockerfile`** to install:
   - **Python 3**
   - **Pathway** library
   - All required dependencies from `requirements.txt`

2. **Copy the Pathway application code** into the container.

3. **Set up the container entrypoint** so that running the image automatically executes the Pathway script.

4. **Build and run the container** using the following commands:

   ```bash
   docker build -t pathway_test .
   docker run --rm -v ${PWD}:/app pathway_test

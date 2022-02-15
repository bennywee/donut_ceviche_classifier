# donut_ceviche_classifier
Classification model for donut and ceviche images.

# Create development environment
Change working directory to donut_ceviche_classifier. Run the below command to build the docker image.

```console
docker build . -t 'classifier_dev'
```

Run container and mount repo files.

```console
docker run -v "$PWD":/classifier -p 8888:8888 -it 'classifier_dev' /bin/bash
```

To run jupyter lab, execute `jupyter lab --ip=0.0.0.0 --allow-root` in the terminal inside the container. Copy the URL into the browser (should be the last link with the access token).

# Copy (unzipped) data into the data folder
To run the code, you will need to copy the unzipped donut and ceviche folders into the `data/` directory. The data directory should look like this:

```
├── data
│   ├── ceviche
│   │   ├── 1006106.jpg
│   │   └── 1013481.jpg
│   │   └── ...
│   ├── donuts
│   │   ├── 100076.jpg
│   │   └── 1000576.jpg
│   │   └── ...
```

# Main analysis
`analysis/exploratory_analysis.ipynb` is the main notebook which contains all the exploratory data analysis and design decisions when completing this challenge. It is broken down into these parts:

1) Data quality check
    + Understanding the raw data and checking for any issues
    + Taking a sample of the daw data and having a look at the files
    
2) Data preprocessing
    + Prepare the data for feature extraction
    
3) Feature Engineering
    + Feature extraction and prepartion before applying classification model
    
4) Train Classifcation Model
    + Split data into training and test set
    + Apply gridsearch and cross validation to select best hyperparameters on training set
    + Pick best model based on best evaluation metric
    
5) Final Model Performance
    + Take the best model and evaluate it on test data
    + Compare precision, recall and f1 metrics and view the raw classification in a confusion matrix.

# Train model
To run the code which produces a trained classification model, execute the following command:

```console
python train.py
```
This will produce a pickle model object in the `model/` directory. The choice of algorithm is baseed on the analysis in `analysis/exploratory_analysis.ipynb`. This object is currently in the model directory and running `python train.py` will reproduce the same model.

# Model scoring
Running `python predict.py` loads the model object from the `model/` directory and predicts on an arbitrary image. The prediction will be printed to the terminal or console.

# Unit tests
Pytest is used for unit testing. To run unit tests:

```console
pytest tests
```

## Unit test coverage
Use `coverage` library to check unit test coverage. Coverage can be used to run unit tests by running `coverage run -m pytest tests`.

To view coverage report, run `coverage report`.

```
Name                       Stmts   Miss  Cover
----------------------------------------------
src/__init__.py                0      0   100%
src/preprocess.py             22      3    86%
tests/test_preprocess.py      24      0   100%
----------------------------------------------
TOTAL                         46      3    93%
```

# Proof of Concept: Deploying into staging environment
Deployment to a staging enironment depends on the use case of the model and the available tech stack. Generally there are two ways to deploy a model: on-demand (online) inference or batch inference. Batch inference is done offline and performs predictions on a batch of input data. This is typically done on a schedule (daily, weekly, monthly) and has the benfit of making a large amount of predictions while managing compute resources. On-demand on the other hand allows for near real time predictions. This involves deploying the model on a web or cloud service while exposing the model via an API call. 

As a proof of concept, suppose a product feature requires close to real time classification of donuts and ceviche images. One potential workflow we could follow is:

1) Train a model in a development environment (what I did in this challenge)

2) Expose the model via a API to be called on a web or cloud service

3) Create another docker container (call it staging) which contains the trained model and the python code to serve the API

4) Deploy the container in the staging environment (perform A/B tests or shadow tests, integration tests, expose it to a subset of production data)

5) Monitor tests or performance metrics before deploying into production

6) Monitor model performance in production

A simple way to do this is to create a API using Flask to be hosted in the staging container. We can create the staging container by writing a new Dockerfile or extending the existing one as a multi stage build.
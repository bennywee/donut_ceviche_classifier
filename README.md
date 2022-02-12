# dounut_ceviche_classifier
Classification model for dounut and ceviche images.

## Create development environment
Change working directory to dounut_ceviche_classifier. Run the below command to build docker image.
`docker build . -t 'classifier_dev'`

Run container and mount local files.
`docker run -v "$PWD":/classifier -p 8888:8888 -it 'classifier_dev' /bin/bash`

Optional - To run jupyter lab, execute `jupyter lab --ip=0.0.0.0 --allow-root` in the bash terminal inside the container. Copy the URL into the browser (should be the last link with the access token).

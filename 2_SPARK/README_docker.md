# build the image
docker-compose build dev

# run a container and attach a bash session 
docker-compose run dev bash

# run py script in image
docker-compose run dev python <file>.py

# run web server apps
docker-compose up



# version checks
cat /etc/os-release
pyspark --version
python --version
kedro info
pip freeze
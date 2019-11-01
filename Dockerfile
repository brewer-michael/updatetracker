#Dockerfile

FROM python:3.6

# make the folder "application" available to the container and set it as the working directory
RUN mkdir /application
WORKDIR "/application"

#Upgrade pip
RUN pip install --upgrade pip

# Update
RUN apt-get update \
  && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

  # move files from the local directory the container is run from to the container's /application directory
  ADD requirements.txt /application/
  ADD currenttext.txt /application/
  ADD src/updatetracker.py /application/

  # pip will install all libraries listed in requirements.txt
  RUN pip install -r /application/requirements.txt

  # environment provisioned in the container now run the program
  CMD [ "python", "updatetracker.py"]

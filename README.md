# updatetracker
Python script to scrape a website daily and check for changes

# Docker Support
Designed to run in a Docker container for ease of use. For more information about Docker, visit https://www.docker.com/

# Prerequisites
Using Docker:
Install Docker

Running Directly:
Python 3.6

Python Libraries:
Beautiful Soup
Requests
Smtplib
Difflib


SMTP server credentials (I use Gmail)

# Installation
- Clone repository
- Fill in the various URLs and credentials you will need in /src/updatetracker.py
- Build your Docker image
- Run the image using the instructions for first run in updatetracker.py
- Once you have a valid currenttext.txt file, running the container will either tell you there are no changes, or will email a notice that there are changes and output the changes into the console

# Example
- Uncomment the lines from /app/updatetracker.py for first run, and make sure you have entered all the needed information
- Run ``docker build -t updatetracker .``
- Run the docker container from the image you just built ``docker run -v ~/{app folder}/updatetracker/data:/data -t updatetracker``
This allows the file in the container's /data folder to be preservered in the /data folder of your app directory after the container finishes
- You should get the console output of the scraped section of the site, within the div specified in /app/updatetracker.py
/data/currenttext.txt will be populated with that output
- Move the contents of the first scrape to the app directory: ``cp data/currenttext.txt currenttext.txt``
- Comment first run lines in /app/updatetracker.py
- From the app directory:  ``docker build -t updatetracker . ``
- Run the image: ``docker run -t updatetracker``
- Set up a cronjob to run the docker container daily: ``crontab -e``
- Type the following: ``0 13 * * * docker run -t updatetracker > ~/dockercron.log 2>&1`` and save your file
This will run the container once daily at 1:00 PM

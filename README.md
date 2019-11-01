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


<div align="center">

  <h1>Daily Update</h1>
  
  <p>
    Start your day right with daily email updates!
  </p>
  
  <!-- Badges -->
  ![GitHub contributors](https://img.shields.io/github/contributors/Myan02/Daily-Update)
  ![GitHub last commit](https://img.shields.io/github/last-commit/Myan02/Daily-Update)
  ![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Myan02/Daily-Update)
  ![GitHub License](https://img.shields.io/github/license/Myan02/Daily-Update)
</div>

<!-- Table of Contents -->
## :mag: Table of Contents

- [Project Details](#envelope-project-details)
- [Getting Started](#toolbox-getting-started)
- [Docker and Automation](#whale2-docker-and-automation)
- [License](#warning-license)
- [Contact](#speech_balloon-contact)


<!-- About the Project -->
## :envelope: Project Details

### Description

Daily Update is a simple tool used to setup and format informational emails. The current configurations allow the user to send emails containing a summary of the weather and a fun fact. What makes this project truly <em>shine</em> is its semi-modular structure and easy-to-read code. 

Don't care about fun facts (lame btw), just don't use the fun fact function and delete it from the payload. 
Want to update the weather to your location, just update the coordinates and timezone. 
  
Here's a list of things you can do with Daily Update:
 
- Retrieve any information you want from the internet (must find a public API) and send it to others in an email</li>
- Set up a scheduler on a device (using something like cron) to get a daily update about the day</li>
- Containerize using Docker for easy building and execution</li>

### Public APIs Used

This project uses two public apis:
```
# For facts
https://api.api-ninjas.com/v1

# For weather
https://api.open-meteo.com/v1/forecast
```

You can use these endpoints for your environment variables. The functions found under api/fetch.py use these two apis. If you'd want to use other public APIs, feel free
to add your functions here and update your environment variables accordingly. For APIs that require data parsing and formatting, refer to weather_configs.py for an example 
utilizing pandas and numpy to organize weather data. 


<!-- Usage -->
## :toolbox: Getting Started

### Installing Files

Clone the repository and cd into the main directory

```bash
git clone https://github.com/Myan02/Daily-Update.git
cd Daily-Update
```
<br>

**Optional but highly recommend:** create a virtual environment in the app directory

```powershell
# Powershell
python -m venv app\venv
app\venv\Scripts\activate
```

```bash
# Linux/Mac
python -m venv app/venv
source ./app/venv/bin/activate
```
<br>

Install required packages

```bash
pip install -r requirements.txt
```

### Configurations

Environmental variables (**NEVER SHARE OR COMMIT API KEYS TO YOUR REPOSITORY**):
- Rename *.env_template* to *.env*
- Fill in variables with your personal information. E.G. API_URL_BASE_WEATHER=https://api.open-meteo.com/v1/forecast

<br>

Other variables:
- Edit *Daily-Update/app/config.py*
- Update *latitude*, *longitude*, and *timezone* at the bottom of the file with info of your choice

### Run Locally

Run the main.py file!

```bash
cd app
python main.py
```

<!-- Automating with Docker -->
## :whale2: Docker and Automation

### Building with Docker

To containerize the project, make sure you have docker installed on your device. For more support, refer to the official docs: https://docs.docker.com/desktop/.
CD into the main directory:
```bash
cd Daily-Update
```

Make sure you have a dockerfile, .dockerignore, requirements.txt, and .env file all in the directory. Run docker build:
```bash
docker build -t daily-update:latest .
```

To start the container and run the program, use docker run:
```bash
docker run --rm --env-file .env daily-update:latest
```

*Note:* the container will run and close when the program terminates making it portable and easily managable. 

### Automation

If you have an unused device, like a raspberry pi, you can save the docker image locally and run the container on a schedule using your os's scheduling tools.
There are many scheduling services; I use Cron for Linux machines; Launchd is native to Mac and preferred over Cron; and Task Scheduler on Windows which used a GUI. 

```bash
# To open crontab in linux
crontab -e
```

```bash
# Add this to your crontab to run the container every day at 9 am and log all errors in cron.log
0 9 * * * docker run --rm --env-file /home/{your home directory}/daily-update/.env daily-update:latest >> /home/{your home directory}/daily-update/cron.log 2>&1
```

## :warning: License

Distributed under the MIT licence. Reference LICENCE for more info.

## :speech_balloon: Contact

If you like this project, please contribute. Fork the repo and make it better. Email me if you'd like to share your contributions or ask me anything:
```
Email: baburyanmichael@gmail.com
```

### Thanks for reading :heart:






  

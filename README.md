
<div align="center">

  <h1>Daily Update</h1>
  
  <p>
    Start your day strong with daily email updates!
  </p>

  
<!-- Badges -->
![GitHub contributors](https://img.shields.io/github/contributors/Myan02/Daily-Update)
![GitHub last commit](https://img.shields.io/github/last-commit/Myan02/Daily-Update)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Myan02/Daily-Update)
![GitHub License](https://img.shields.io/github/license/Myan02/Daily-Update)
</div>

<br>

<!-- Table of Contents -->
# :mag: Table of Contents

- [Project Details](#envelope-project-details)
- [Getting Started](#toolbox-getting-started)
- [License](#warning-license)
- [Contact](#handshake-contact)


<!-- About the Project -->
## :envelope: Project Details

  <p>Daily Update is a simple tool used to setup and format informational emails. The current configurations allow the user to send emails containing a summary of the weather and a fun fact. 
    What makes this project truly <em>shine</em> is its semi-modular structure and easy-to-read code. 
  </p>
  
  <p>Don't care about fun facts (lame btw), just don't use the fun fact function and delete it from the payload.
    Want to update the weather to your location, just update the coordinates and timezone. 
  </p>

  <p>
    Here's a list of things you can do with Daily Update:
  </p>
  <ul>
    <li>Retrieve any information you want from the internet (must find a public API) and send it to others in an email</li>
    <li>Set up a scheduler on a device (using something like cron) to get a daily update about the day</li>
    <li>Containerize using Docker for easy building and execution</li>
  </ul>


<!-- Usage -->
## :toolbox: Getting Started

Clone the repository and go in the main directory

```bash
git clone https://github.com/Myan02/Daily-Update.git
cd Daily-Update
```
<br>

!Highly Recommended! create a virtual environment in the app directory

*Windows*
```powershell
python -m venv app\venv
app\Scripts\activate
```

*Linux/Mac*
```bash
python -m venv app/venv
source ./app/venv/bin/activate
```
<br>

Install required packages

```bash
pip install -r requirements.txt
```

<br>

Create and populate a .env file

```Bash
touch .env
```

*format to populate*
```txt
API_URL_BASE_WEATHER=
API_KEY_FACT=
API_URL_BASE_FACT=

SENDER=
RECIPIENTS=*recipient 1*, *recipient 2*, etc.
PASSWORD=
HOST=*smtp.gmail.com*, *smtp.outlook.com*, etc
PORT=
```




  

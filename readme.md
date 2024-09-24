# FINANCIAL NEWS BLOG -> ALx Portfolio project
## Description
- This project aims to help people to have easy access to quality news around the world such as:
    1. financial news,
    2. global trends,
    3. and economy news.

## Table of content
- [Description](#description)
- [Installation](#installation)
- [usage](#usage)
- [Features](#features)
- [License](#license)
- [Contact](#contact)

## Installation
1. Clone the repository `git clone https://github.com/balo7773/KEO.git`
2. make sure you have your **venv** (virtual environment) activated in the directory you cloned the repo,
    if not follow the instructions below:
  -  for window users run the command
    - **if using command prompt**
    ```
        venv\Scripts\activate
    ```
    - **if using powershell**
    ```
        venv\Scripts\Activate.ps1
    ```
  -  for mac and Linux OS users
    - **in your shell terminal**
    ```
        source venv/bin/activate
    ```
    - **to deactivate for all users**
    ```
        deactivate
    ```
***NOTE: WHEN RUNNING THIS COMMANDS MAKE SURE YOU ARE IN THE DIRECTORY WHERE YOU CLONED THE REPO ***

3. After that make sure you download the packages from `requirements.txt` using the command:
```
    pip install -r requirements.txt
```
***NOTE: requirements.txt IS INCLUDED IN THE REPOSITORY. MAKE SURE YOU CLONE IT, AND ALL PACKAGES USED WERE UPDATED AS OF 23RD SEPTEMBER, 2024.***

## Usage
- Run main.py either directly or through wsgi if familiar with it:
```
python3 main.py
```
- once running, access the web app through `http://localhost:5000`
***NOTE: TO ENSURE SMOOTH FUNCTIONALITY, MAKE SURE ALL DEPENDENCIES FROM requirements.txt ARE INSTALLED. ***

## Features
- Simple signup with strong authentication features.
- Real-time financial data is available through the ticker as you navigate.
- Latest news is always available on the homepage.
- A search bar allows for personalized news retrieval.
- Easy access to financial, global, and economic news.

## License
- This is a portfolio project created as part of the ALX Software Engineering program.  
It is not intended for commercial use or distribution. The code is provided for educational and demonstration purposes only.

## Contact
- open to new ideas and collaboration, feel free to contact me at: `balogunabdulmalik04@gmail.com`

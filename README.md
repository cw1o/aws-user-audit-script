# Account Audit Script

## Prerequisites
- [Python 3](https://www.python.org/downloads/)
- [pip](https://www.w3schools.com/python/python_pip.asp)
- [pipenv](https://pipenv.pypa.io/en/latest/)
- [awscli](https://aws.amazon.com/cli/)

## Installation and Usage

Install Pipenv. Instructions to install can be found [here](https://pipenv.pypa.io/en/latest/)

This script uses the AWS boto3 SDK, information on how to configure credentials for use with boto can be found [here](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration)

This script ouputs the below to the working dir:
- console-access-audit.csv
- programmatic-access-audit.csv

### Linux / MacOS

- Clone this repostiory
- Navigate to the Repository's directory
- Check pipenv has been installed correctly `pipenv --version`
- Install dependenciies with `pipenv sync`
- Run the script with `pipenv run python main.py`

### Windows

- Clone this repostiory
- Navigate to the Repository's directory
- Check pipenv has been installed correctly `py -m pipenv --version`
- Install dependenciies with `py -m pipenv sync`
- Run the script with `py -m pipenv run python main.py`
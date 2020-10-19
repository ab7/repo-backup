# Repo Backup Script

Simple Python script to sync repositories between service providers.

### Supported providers

* Github
* Bitbucket

### Requires

* Python 3.8.x or higher
* Command shell

## Setup

* Create a virtual environment:

    ```
    python3 -m venv venv && . venv/bin/activate && pip install --upgrade pip
    ```

* Install the Python dependencies:

    ```
    pip install -r requirements.txt
    ```

* Create a file named `.env` in the root directory. If you have 2FA setup with your service provider it is recomended to use an app password. Enter the following fields into the `.env` file (with items in the brackets replaced with your credentails):

    ```
    BITBUCKET_USERNAME=<username>
    BITBUCKET_PASSWORD=<password>
    GITHUB_USERNAME=<username>
    GITHUB_PASSWORD=<password>
    ```

## Usage

```
python backup.py
```

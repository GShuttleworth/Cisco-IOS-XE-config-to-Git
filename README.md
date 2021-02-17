# Track Cisco IOS-XE config in a Git repository

## Introduction

This is an example python script to demonstrate programmatically collecting current running config from a Cisco IOS-XE device and storing the config in a Git repo.

This allows you to monitor for configuration changes and track changes to over time.

![alt text](/readme_images/git_diff.png "Git diff on IOS-XE config")

## Prerequisites

1. [Python](https://www.python.org/) - this has been tested with Python 3.8.6.
2. [Git](https://git-scm.com/) installed on your computer.
3. A remote Git repository. This has been tested against remote [GitHub](https://github.com/) repositories.
4. A Bash (or Bash compatible) terminal - the python script runs Git Bash commands directly in a terminal instance using `subprocess`.
5. Access to an IOS-XE device - see below for instructions on using a virtual DevNet Sandbox.

### Use a virtual Cisco IOS-XE Device from DevNet Sandbox

You can get a virtual instance of a Cisco IOS-XE device from the [DevNet Sandbox](https://devnetsandbox.cisco.com/) if you don't want to try this against a physical device.

> This is optional

1. Go to DevNet Sandbox https://devnetsandbox.cisco.com/
2. Reserve an IOS-XE Sandbox. This will take a few minutes to start.
3. Once it starts you will be emailed some VPN connection details, connect to the VPN.

![alt text](/readme_images/ios_sandbox.png "IOS-XE DevNet Sandbox")

## Getting started

### Clone this Git Repository

```bash
git clone https://github.com/GShuttleworth/Cisco-IOS-XE-config-to-Git
```

Open new Git repo folder in terminal

```bash
cd Cisco-IOS-XE-config-to-Git
```

### Setup Python virtual environment

It is good practice to run Python scripts in a virtual environment.

Create virtual environment

```bash
python3 -m venv venv
```

Open the virtual environment

```bash
source venv/bin/activate
```

Install Python dependencies

```bash
pip install -r requirements.txt
```

## Edit Python file

The `cisco_ios_to_git.py` Python script has some variables you need to define.

Edit `host`, `username` and `password` to match your device. By default the connection details are for the DevNet IOS-EX Sandbox mentioned above.

```python
# Cisco IOS-XE connection details
device = {
    "device_type": "cisco_ios",
    "host": "10.10.20.48",
    "username": "developer",
    "password": "C1sco12345",
}
```

Edit `git_repo_url` to match your Git repository URL.

Optional - edit `commit_message` to specify what Git should use as the message for each commit.

```python
# Git repository details
git_repo_url = "https://github.com/your_repo_url"
commit_message = "Automatic config update"
```

## Run the Python script

To run the Python script

```bash
python cisco_ios_to_git.py
```

## Check the result

The script automatically deletes all created files after the Git push is complete. This means there's nothing to see locally after it has ran.

Go to your remote Git repository and you should see your config uploaded.

If you make changes to the switch config and re-run the Python script, you will see Git track the changes between the new config and the old config. Check the changes by viewing the most recent Git commit!

## Troubleshooting

If you have problems running the script, it is likely that the Git installed on your computer hasn't authenticated with the remote Git repository. The Python script relies on connection authentication credentials being cached on your computer.

To fix, manually clone the repository, and if prompted, enter authentication details.

```bash
git clone <git_repo_url>
```

You may need to use an access token rather than a password. Check [here](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) for details on creating access tokens if you're using GitHub

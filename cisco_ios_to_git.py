import tempfile
import subprocess
from netmiko import ConnectHandler

# Cisco IOS-XE connection details
device = {
    "device_type": "cisco_ios",
    "host": "10.10.20.48",
    "username": "developer",
    "password": "C1sco12345",
}
# Git repository details
git_repo_url = "https://github.com/your-repository"
commit_message = "Automatic config update"


# ------ Connect to device and get device config ------

# Connect to IOS-XE device
net_connect = ConnectHandler(**device)

# Run show command on device
device_config = net_connect.send_command("show run")

# Disconnect from Device
net_connect.disconnect()


# ------ Clone git repo in temporary directory, replace files with new config file and push changes back to git repo  ------

# Create temporary directory
temporary_folder = tempfile.TemporaryDirectory()

# Clone Git Repo
subprocess.call(
    f"cd {temporary_folder.name} && git clone {git_repo_url} . && rm *.*", shell=True
)

# Write all config to file
with open(f"{temporary_folder.name}/{device['host']}_config.txt", "w") as outfile:
    outfile.write(device_config)

# Git commit all changes
subprocess.call(
    f"cd {temporary_folder.name} && git add -A && git commit -a -m '{commit_message}' && git push",
    shell=True,
)

# Delete temporary directory
temporary_folder.cleanup()

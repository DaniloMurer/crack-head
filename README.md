# Crack Head

CLI program for some common penetration testing tasks like port scanning or banner grabbing.
Other features like simple brute force attacks are also an option.

## Installation & Setup

The first step is to clone the repository, this can be done using following command:
```shell
git clone https://github.com/DaniloMurer/crack-head.git
```
After cloning the repository you can navigate into the created directory.

The next step is to activate the virtual environment, this can be achieved using following command:
```shell
# Windows
venv/Scripts/activate

# Linux
source venv/Scripts/activate
```

Now you need to install the required packages, this can be done with following command:
```shell
pip install -r requirements.txt
```

To test if everything was set up correctly, run following command:
```shell
python main.py -h
```

If everything works fine you should get an output similar to this:
```shell
usage: main.py [-h] [-pS PORT_SCAN] [-e EXPORT] [-fS FULL_SCAN]
               [-sBF SSH_BRUTE_FORCE] [-uPwL USE_PASSWORD_LIST]

Crack Head Hacking Tool

optional arguments:
  -h, --help            show this help message and exit
  -pS PORT_SCAN, --port-scan PORT_SCAN
                        Port scan with target host
  -e EXPORT, --export EXPORT
                        Export result as Excel
  -fS FULL_SCAN, --full-scan FULL_SCAN
                        Execute full scan of target
  -sBF SSH_BRUTE_FORCE, --ssh-brute-force SSH_BRUTE_FORCE
                        Start SSH Brute Force attack
  -uPwL USE_PASSWORD_LIST, --use-password-list USE_PASSWORD_LIST
                        User Password list for Brute Force attacks
```

## Examples

Here is an example for a simple port scan:
```shell
python main.py -pS example.com -e "C:/Path/To/ExportFile/excel.xlsx"
```

This should export the port scan result as an excel file to the specified target.
<br>
<br>
For more information about the target, a full scan can be launched which also includes banner grabbing:
```shell
python main.py -fS example.com -e "C:/Path/To/ExportFile/excel.xlsx"
```

And if you want to perform a SSH brute force attack, use following command:
```shell
python main.py -sBF example.com
```

You can also use a password list for the SSH brute force attack, crack head provides a list from [Pwdb-Public](https://github.com/ignis-sec/Pwdb-Public/blob/master/wordlists/ignis-100K.txt):
```shell
python main.py -sBF example.com -uPwL "C:/Path/To/Crack/Head/assets/pwlist.txt"
```
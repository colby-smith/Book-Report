# Book-Report
## About
A simple program that takes a text file and creates a report on it, utilising loops, dictionaries, lists and other Python functions. Any text file can be used to produce a report by simply following the usage instructions. It can outpu the total wordcount in the report, as well as list (in decending order) how many times a character has been used.

## Prerequisites
To use this program effectively make sure you have installed:
* Python 3.12.2
* bash or zsh

## Installing WSL (Windows Subsystem for Linux)

1. Open PowerShell as administrator.

2. Copy and paste the code below and hit enter.
```
wsl --install
```
3. Wait for the downloads to be complete, then restart your computer.

4. After restarting your computer, you should see an "Ubuntu" Window open automatically once you log back in. If you don't, search for the "Ubuntu" or "WSL" program in the start menu and launch it.

5. The window will prompt you to enter a username and password. Make sure you remember these! These are the credentials for your Linux user.

## Installing python 3.12.2
If you're on Linux, there are some dependencies you'll need before installing pyenv. Run these commands to install them:

1. Only run these if you're using a Linux system.
```
sudo apt update
sudo apt install -y build-essential zlib1g-dev libssl-dev
sudo apt install -y libreadline-dev libbz2-dev libsqlite3-dev libffi-dev

```
2. Run this to install pyenv with webi.
```
curl -sS https://webi.sh/pyenv | sh
```
3. Open your ~/.bashrc file in VS Code. You can do so by typing:
```
code ~/.bashrc
```
If you're using a Mac.
```
code ~/.zshrc
```
4. Add these lines to the bottom of the file in this order:
```
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

5. Finally close and reopen your terminal.

## Usage
To use this simple tool simply follow the instructions below:

1. Change into the repository directory in your shell.

2. Create a folder called **books**.

3. Create a .txt file called **text**.

4. Save the changes using *ctrl+S* for windows and *command+S* on mac.

5. Finally run the program by typing **python main.py** and hitting enter, if an error occurs run **python3 main.py** instead.

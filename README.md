## Setup

1. create virtual environment `python -m venv ./venv`
2. activate virtual environment `. ./venv/bin/activate`
3. when using vscode python plugin set as active workspace interpreter: click a
   star near that environment
4. install dependencies `pip install -r requirements.txt`

## Run

`python projekt-final.py`

## Build executable

There are multiple ways to
[build standalone executable](https://packaging.python.org/en/latest/overview/#bringing-your-own-python-executable).
For that project we are using [pyInstaller](https://pyinstaller.org) with the
following operations:

1. install `pip install -U pyinstaller`
2. build executable `pyinstaller projekt-final.py`. The executable files can be
   found in `./dist` folder.

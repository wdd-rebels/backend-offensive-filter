# backend-offensive-filter

## To run locally
- Make sure pip3, python3 and virtualenv are installed (all are available on Homebrew).
- The below commands assume you've created your virtualenv in a directory called `venv` and that you're on a Unix-based OS.
```sh
source ./venv/bin/activate
pip3 install -r requirements.txt
FLASK_APP=index.py FLASK_ENV=development flask run
```

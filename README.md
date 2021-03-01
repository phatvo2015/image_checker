## Running Locally

### Requirements:
- Make sure you have Python 3.8 at least
- Install the dlib library by following this instruction: https://github.com/davisking/dlib


```sh
$ git clone https://github.com/phatvo2015/image_checker.git
$ cd image_checker


$ python3 -m venv getting-started
$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

```


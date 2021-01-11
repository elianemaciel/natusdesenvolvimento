# natusdesenvolvimento


## Compile css

    - cd stylesheets
    - `compass compile`

## Deploy (it's automatic)

    - `heroku login`
    - `heroku git:remote -a natus-desenvolvimento`
    - `heroku run python manage.py migrate`

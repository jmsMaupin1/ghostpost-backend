This project is the back end portion of [ghostpost-frontend](https://github.com/jmsMaupin1/ghostpost-frontend).

## Ghost Post Machine

The purpose of this project is to build a React front end that interfaces with a Django Rest Framework back end running on the same machine.

The GhostPost Machine™ is a website where people can anonymously post Boasts or Roasts of whatever they want. Like Twitter, there is a character limit: 280 characters. We are deliberately not dealing with logins, as that is outside the scope of the project (and beyond our time constraints).

## Getting started

Make sure you have [Poetry](https://github.com/python-poetry/poetry) installed

run `poetry install` followed by `poetry shell`

### when youre inside the  poetry shell

run `python manage.py runserver`
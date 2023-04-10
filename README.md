# Recipe Vault

### A place to store all the family recipes.

## By: David Corvaglia  

### Submitted to MLH Bon Hackétit Hackathon

#### https://organize.mlh.io/participants/events/9350-bon-hacketit

# Update

## I won the Grandma's Kitchen Award. :) The Devpost submission is here: https://devpost.com/software/recipe-vault-unp73h

## Install
1. Clone the repo.
2. cd into Recipe-Vault
3. run <code>pip3 install -r requirements.txt</code>
4. cd into recipevault
5. Change the secret key in settings.py to something random.
6. run <code>python manage.py makemigrations</code>
7. run <code>python manage.py migrate</code>
8. run <code>python manage.py createsuperuser</code>
9. run <code>python manage.py runserver</code>
10. You're all set :)

## Video
https://youtu.be/0Xq3HhWJEeE
# Project Story

## Inspiration
Our family has very diverse roots from where we come from, so it is safe to say that we have a lot of recipes that have been handed down by generations. But sometimes it gets hard to keep track of all of then. So I came up with the idea of a recipe bank to store the family recipes locally for fast and easy access.
## What it does
I allows for the family to access a webpage in which the recipes can be viewed, sorted, edited, and created all on one place and very fast since it is hosted on the local network.
## How I built it
I built this app using Django for the backend and used Bootstrap Studio to build the frontend.
## Challenges I ran into
I spent a lot of time fixing bugs with Django's html template processing system since I was not very familiar with it. I also ran into challenges with CSS in terms that there was a lot of tweaking to get things right so that the backend and frontend would interact.
## Accomplishments that I'm proud of
I am very proud of how long it took me to make this application even though I had not had much experience with Django. I am also proud of how the app looks and that it functions great.
## What I learned
I have learned a great deal about Django, Python, SQLite, CSS, Bootstrap. Suffice it to say, this was a great learning experience especially since this was my first time really dealing with a website backend.
## What's next for Recipe Vault
I think that the next step would be to expand the application so that there would be greater filtering and sorting on the home and search page.

# Stager
ID 259: HiPerCiC (Fall 2017)

Luke Zimmerman, Hugo Valent, Deepak Shah

## Views
#### start
The start view displays the login template.
Either a Google account or Django admin access are required.

#### index
The index view displays the planner template.
There are three main sections/panels in the workspace:

 - Navigation: displays navigation options for different in the workspace
 - Actions: displays the different action for a show
 - Visualization: multi-purpose panel used for adding actions, displaying action properties, and visualizing the theater


#### show

The show view specifies new shows for theater designers.
Designers may add new shows are edit existing shows.

#### AJAX
There are a large number of AJAX URLs in the urls.py file. The most noteworthy are:

 - getAction: retreives all actions in the database
 - createAction: creates an action

## Local Development
#### Database

Stager uses Postgres, so local development requires a local installation of Postgres.

#### local_settings
Use a local_settings.py file to store setting for your local installation of Postgres.
For example:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hiper_theater',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
where the `USER` and `PASSWORD` fields contain your Postgres username and password.

`SITE_ID` should also be stored in local_settings.py.
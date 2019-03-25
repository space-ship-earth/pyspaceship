# PySpaceship #

A python implementation of [Spaceship Earth](python.spaceshipearth.org).

## Installation ##

We are expecting that you already have `pyenv` and `pyenv-virtualenvwrapper` installed.
If you haven't done that already, see how Igor does it in [his dotfiles](https://github.com/igor47/dotfiles/blob/264092d5314e3a83039554731a62c77ecd7d62ce/bashrc#L254-L270).

### Set up virtualenv

Create the virtualenv:

```
$ mkvirtualenv pyspaceship
```

Then, install some basic tooling:

```
$ pip install -r requirements.txt
```

Now, you can see all the tasks we have defined:

```
$ inv --list
```

## Running ##

Run the website like so:

```
$ inv run.flask
```

To run via the gunicorn server, you can do:

```
$ inv run.gunicorn
```

The site will be accessible on localhost port 9876 (it's a countdown!).

## MySQL ##

This app expects a MySQL database on port 9877.
If you have `docker-compose` set up, you can bring one up like so:

```
$ inv run.mysql
```

## Migrations ##

First, you need to create the migration.
You can do this through `migration-prep`:

```
$ inv run.migration-prep "my migration description"
```

This will generate your migration in `migrations/versions`.
You should edit this migration and commit it to the git repo.

Next, you can run your migration:

```
$ inv run.upgrade
```

If you need to back down again, run `inv run.downgrade`.

## Manual steps in production

You have to do these by hand:
* set up a mysql database
  * give it a `spaceship-app` account
  * create a `spaceship` database
* create an ssl cert

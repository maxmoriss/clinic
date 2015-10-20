from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm
import StringIO


project_dir = '/var/www/clinic'
virtual_env = '. ~/envs/clinic/bin/activate'
settings = 'settings_production.py'
env.hosts = ['']
env.port = 57576
# env.shell = '/bin/zsh'
env.user = 'maxmoriss'
env.roledefs = {
    'production': ['clinic'],
}


""" Helpers
"""
# cd & workon wrapper
def workwrap(original_function):
    def new_function(*args, **kwargs):
        with cd(project_dir):
            with prefix(virtual_env):
                original_function(*args, **kwargs)
    return new_function


# reload gunicorn
def _supervisor_reload():
    run('sudo supervisorctl restart clinic')


# shortcut to django manage.py
def _dm(command):
    return run('./manage.py %s' % command)


def pull():
    run('git pull origin master')


""" Commands
"""
@roles('production')
@workwrap
def deploy(full=False):
    # publish master branch
    # run('git reset db.sqlite3')
    pull()
    if full:
        run('pip install -r req.txt')
        _dm('migrate')
    _dm('collectstatic --noinput')
    _supervisor_reload()
    return True


@roles('production')
@workwrap
def gpull():
    pull()


@roles('production')
@workwrap
def reload():
    # reload supervisor
    _supervisor_reload()


@roles('production')
@workwrap
def checkout():
    # checkout
    run('git checkout .')


@roles('production')
@workwrap
def install():
    # install new packages
    pull()
    run('pip install -r req.txt')


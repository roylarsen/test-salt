import click
from test_salt.interfaces import start as vagrant_start

@click.group()
def run():
  pass

# This is the main workhorse
# This will run the tests
@run.command()
def start():
  try:
    open('./Vagrantfile')
    click.echo('starting...')
    box = vagrant_start()
    print box.ssh_config()
  except IOError:
    print "No Vagrantfile in PWD"

# This will provision the machine and set up work environment
@run.command()
def create():
  click.echo('creating...')

# Environment teardown
@run.command()
def kill():
  click.echo('Killing...')

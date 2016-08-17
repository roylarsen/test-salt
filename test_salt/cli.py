import click


@click.group()
def run():
  pass

# This is the main workhorse
# This will run the tests
@run.command()
def start():
  click.echo('starting...')

# This will provision the machine and set up work environment
@run.command()
def create():
  click.echo('creating...')

# Environment teardown
@run.command()
def kill():
  click.echo('Killing...')

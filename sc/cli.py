import click
import os
import sys
from sc.configmanager import Config

# from dockercli import DockerCli

# from ._version import __version__



class Settings(object):
    def __init__(self, home=None, debug=False):
        self.home = os.path.abspath(home or '.')
        self.debug = debug

config_file = Config()

@click.group()
@click.version_option()
@click.pass_context
def cli(ctx):
    """Smartcontainers for software and data preservation.
    Smartcontainers provides a mechanism to add metadata to Docker
    containers as a JSON-LD label. The metadata is contextualized using
    W3C recommended PROV-O and ORCID IDs to capture provenance information.
    The sc command wraps the docker commandline interface and passes any
    docker command line parameters through to docker. Any command that changes
    the state of the container is recorded in a prov graph and attached to the resultant
    image.
    """

    # We require python 3.5 or greater now.
    if sys.version_info < (3, 5):
        sys.exit('sc requires Python 3.5+')

@cli.group()
@click.option('--config', '-c', help='Run configure command')
def config(config):
    """Configure smartcontainers. Run sc config to get subcommand options for configuring

    :param config: string
    """

    pass


# We may have to manually handle --help and pass it to docker
@cli.command(context_settings=dict(ignore_unknown_options=True))
@click.argument('command', nargs=-1, type=click.UNPROCESSED)
def docker(command):
    """Execute a docker command.
    Example: sc docker run <container id>

    :param command: string
    """
    cmd = ""
    for i in range(len(command)):
        cmd += command[i] + " "

    # processdocker = DockerCli()
    # processdocker.do_command(cmd)


@cli.command()
@click.argument('image')
def search(image):
    """Search for information in docker metadata.

    :param image: string
    """
    pass


@cli.command()
@click.argument('image')
def printlabel(image):
    """Print Metadata label from container."""
    # processdocker = DockerCli("info")
    # this_label = processdocker.get_label(image)
    print(this_label)


@cli.command()
@click.argument('image')
def publish(image):
    """Publish a image to a public repository.

    :param image: string
    """
    pass


@cli.command()
def preserve():
    """Preserve workflow to container."""
    pass

@cli.command()
@click.argument('image')
def infect(image):
    """Provenance should be contagious. Create smartcontainer image from
    existing image. """
    # processdocker = DockerCli()
    # processdocker.infect(image)



#  End Orcid  ###############################
if __name__ == '__main__':
    cli()

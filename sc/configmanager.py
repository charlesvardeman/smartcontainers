# -*- coding: utf-8 -*-
"""Configuration manager for reading and writing SC configuration files.

This module is responsible for managing the local smartcontainers configuration
file that is stored in the user directory. The format of the configuration file
is YAML and an example of valid keys can be found in the examples directory. If
no local configuration file exists, the option to generate one will be given walking
the user through the minimum information needed for smartcontainers.

Todo:
    * Configuration files under windows.
    * Additional Organizational Information

"""

import json
import os
import click
from ruamel.yaml import YAML

__author__ = 'charlesvardeman'

# noinspection PyBroadException,PyBroadException
class Config(object):
    """ Configuration File Creator """

    def __init__(self):
        """Initialize Configuration. Agent config objects correspond to
        FOAF:Person, schema:Person and Prov:Person
        Note that because a proper family name suffix is not supported,
        FRAPO is imported.
        https://github.com/SPAROntologies/frapo
        http://www.sparontologies.net/ontologies/frapo
        @prefix frapo: <http://purl.org/cerif/frapo/> .

        Parameters
        ----------
        :param none

        Returns
        -------
        :returns: ConfigManager object
        """
        self.filename = "sc.yaml"
        self.givenName  = ""
        self.familyName = ""
        # "honorificPrefix": "http://schema.org/honorificPrefix",
        self.honorificPrefix = ""
        # honorificSuffix": "http://schema.org/honorificSuffix",
        self.honorificSuffix = ""
        # @prefix frapo: <http://purl.org/cerif/frapo/> .
        self.hasFamilialSuffix = ""
        self.ORCID = ""
        self.W3ID = ""

        # Autogenerate FOAF:name
        self.name = self.honorificPrefix + self.givenName + self.honorificPrefix + self.hasFamilialSuffix

        if os.environ.get('SC_HOME'):
            self.config_path = os.getenv('SC_HOME')
        else:
            os.environ['SC_HOME'] = os.environ['HOME'] + '/.sc/'
            self.config_path = os.getenv('SC_HOME')

        # Sanity check that config file exists, if not offer to create a file
        if os.path.exists(self.config_path + self.filename):
            data = self.read_config()
            agent = data['Agent']
            if 'givenName' in agent.keys():
                self.givenName = agent['givenName']
            if 'familyName' in agent.keys():
                self.familyName = agent['familyName']
            if 'hasFamilialSuffix' in agent.keys():
                self.hasFamilialSuffix = agent['hasFamilialSuffix']
            if 'honorificPrefix' in agent.keys():
                self.honorificPrefix = agent['honorificPrefix']
            if 'honorificSuffix' in agent.keys():
                self.honorificSuffix = agent['honorificSuffix']
        else: # generate a config
            self.gen_config()

    def write_config(self):
        """Write the configuration file
        Writes the configuration file to the SC directory, or program home directory

        Parameters
        ----------
        :param: None

        Returns
        -------
        :returns: none
        """
        if os.path.exists(self.config_path):
            # Open existing file, read and write
            ctgfile = open(self.config_path + self.filename, 'w+')
        else:
            # Create config file, write
            os.mkdir(self.config_path)
            ctgfile = open(self.config_path + self.filename, 'w')

        try:
            # Write YAML file from config
            # ctgfile.write(str(self.config_obj))
            # ctgfile.write(json.dumps(self.config_obj, indent=4, sort_keys=True))
            ctgfile.close()
            print('The configuration file has been created.')
        except:
            print('An unexpected error has occurred.  The configuration file could not be created.')
            ctgfile.close()

    def read_config(self, filepath=None):
        """Read the yaml configuration file.
        Parameters
        ----------
        :param: filepath direcory where sc.yaml is located.

        Returns
        -------
        :returns message: string
            If the configuration file does not exist, return error string
        """
        if filepath == None:
            filepath = self.config_path

        if not os.path.exists(filepath):
            # If the directory does not exist, we cannot read it.
            return 'Configuration directory does not exist.'
        elif not os.path.exists(filepath + self.filename):
            # If the file does not exist, we cannot read it.
            return 'Configuration does not exist.'
        else:
            try:
                # Open existing file, read and write
                ctgfile = open(filepath + self.filename, 'r')
                loader = YAML(typ='safe')
                data = loader.load(ctgfile)
                self.config_object = data
                ctgfile.close()
                # self.graph.parse(data=self.config_object, format='n3')
                return data
            except:
                ctgfile.close()
                return 'Configration could not be read or parsed correctly'

    def gen_config(self):

        print("Please provide some basic information:")
        self.givenName = click.prompt(
                'Please enter a first name', default='',
                show_default=False)
        self.familyName = click.prompt(
                'Please enter a last name', default='',
                show_default=False)
        if click.confirm('Do you have an ORCID?'):
            self.ORCID = click.prompt(
                'Please enter your ORCID', default='',
                show_default=False)
        if click.confirm('Do you have an W3ID?'):
            self.ORCID = click.prompt(
                'Please enter your W3ID', default='',
                show_default=False)
        # config_file.write_config()

# configmanager = ConfigManager()
# configmanager.read_config()

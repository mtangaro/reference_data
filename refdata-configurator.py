"""
this macro ...

"""

import datetime as dt
import logging
import sys
import time

from argparse import ArgumentParser

import yaml

from bioblend.galaxy import GalaxyInstance
from bioblend.galaxy.client import ConnectionError
from bioblend.galaxy.toolshed import ToolShedClient
from bioblend.toolshed import ToolShedInstance

MTS = 'https://toolshed.g2.bx.psu.edu/'  # Main Tool Shed



def get_galaxy_instance(url=None, api_key=None):
    """
    Get an instance of the `GalaxyInstance` object. If the arguments are not
    provided, load the default values using `load_input_file` method.
    """
    if not (url and api_key):
        tl = load_input_file()
        url = tl['galaxy_instance']
        api_key = tl['api_key']
    return GalaxyInstance(url, api_key)


def get_tool_shed_client(gi=None):
    """
    Get an instance of the `ToolShedClient` on a given Galaxy instance. If no
    value is provided for the `galaxy_instance`, use the default provided via
    `load_input_file`.
    """
    if not gi:
        gi = galaxy_instance()
    return ToolShedClient(gi)

def get_tool()


def check_tool_installation(url=None, api_key=None):
    tool = {"bowtie2","devteam"}
    gi = get_galaxy_instance(url, api_key)
    tsc = get_tool_shed_client(gi)
    tsc_repos = tsc.get_repositories()
    for it in tsc_repos:
       if (tool['name'] == it['name']) and (it['owner'] == tool['owner']):
            if it['status'] not in ['Installed', 'Error']:
                return False
    return True

def __main__():

    # options
    parser = ArgumentParser(usage="usage: python %(prog)s <options>")
    parser.add_argument("-g", "--galaxy", dest="galaxy_url", help="Target Galaxy instance URL/IP address (required if not defined in the tools list file)",)
    parser.add_argument("-a", "--apikey", dest="api_key", help="Galaxy admin user API key (required if not ""defined in the tools list file)",)
    args = parser.parse_args()

    return check_tool_installation(args.galaxy_url, args.api_key)


if __name__ == "__main__":
    __main__()

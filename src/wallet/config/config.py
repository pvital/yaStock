#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# yaStock - yet another Stock Wallet Tracking.
# Copyright (c) 2021 Paulo Vital <paulo@vital.eng.br>
#

import os

from configparser import ConfigParser


__version__ = 1
__release__ = None


def get_version() -> str:
    """
    get_version - Return the version of the API web service.

    Returns:
        str: API version number, with release numnber contactenated if exists
    """
    if __release__:
        return '-'.join([__version__, __release__])
    else:
        return f'{__version__}'


class Paths(object):
    """
    Paths class - represents all necessary paths to execute the service.
    """

    def __init__(self):
        """
        Define Paths class.
        """
        self.prefix = self.get_prefix()
        self.containerized = (os.path.exists('/.dockerenv'))

        if self.containerized:
            self.src_dir = '/app'
            self.conf_dir = self.add_prefix('config')
            self.db_dir = self.add_prefix('db')
        else:
            self.src_dir = self.add_prefix('wallet')
            self.conf_dir = self.add_prefix('wallet/config')
            self.db_dir = self.add_prefix('wallet/db')

    def __repr__(self):
        values = {
            'prefix': self.prefix,
            'containerized': self.containerized,
            'src_dir': self.src_dir,
            'conf_dir': self.conf_dir,
            'db_dir': self.db_dir,
        }
        return f'Paths({values})'

    def get_prefix(self) -> str:
        """
        Return the correct path prefix for the location of the service
        execution.

        Returns:
            str: absulote path.
        """
        # Get the base dir path of this file
        if __file__.startswith('/'):
            base = os.path.dirname(__file__)
        else:
            base = os.path.dirname(f'./{__file__}')

        # Check if user is authorized to access the config file
        if os.access(f'{base}/../../wallet/config/config.py', os.F_OK):
            return os.path.abspath(f'{base}/../../')
        else:
            return '/app'

    def add_prefix(self, subdir: str) -> str:
        """
        Add to the self.prefix the given content.

        Args:
            subdir (str): path to be added to self.prefix.
        
        Returns:
            str: path with self.prefix and the given content.
        """
        return os.path.join(self.prefix, subdir)


paths = Paths()


def _get_config() -> ConfigParser:
    """
    "private" method to return a ConfigParser instance with all configuration
    setup.

    Returns:
        ConfigParser
    """
    config = ConfigParser()

    # Set database (sqlite3) configuration as db
    config.add_section('db')
    config.set('db', 'db_name', 'wallet.db')

    config_file = os.path.join(paths.conf_dir, 'wallet.conf')
    if os.path.exists(config_file):
        config.read(config_file)
    return config


config = _get_config()


if __name__ == '__main__':
    print(paths)
    conf = {}
    for section in config.sections():
        conf[section] = config.items(section)
    print(f'Config({conf})')

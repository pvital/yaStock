#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# yaStock - yet another Stock Wallet Tracking.
# Copyright (c) 2021 Paulo Vital <paulo@vital.eng.br>
#

import os

from config.config import config, paths
from db.db_setup import setup_db_tables


def main():
    wallets = []
    print(f'Currently you have {len(wallets)} wallets.')


if __name__ == '__main__':
    database = paths.db_dir + '/' + \
        config.get('db', 'db_name', fallback=None)

    if not os.path.exists(database):
        try:
            setup_db_tables()
        except:
            print(f'ERROR: could not setup DB tables.')
            exit(1)

    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# yaStock - yet another Stock Wallet Tracking.
# Copyright (c) 2021 Paulo Vital <paulo@vital.eng.br>
#

import os
import sqlite3

from config.config import config, paths


def create_connection(db_file: str) -> sqlite3.Connection:
    '''
    Create a connection to the SQLite DB specified by db_file.

    Args:
        db_file: str    DB file
    
    Returns:
        sqlite3.Connection
    '''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        raise e

    return conn


def create_table(conn: sqlite3.Connection, create_table_sql: str) -> None:
    '''
    Create a table from the create_table_sql statement.

    Args:
        conn: sqlite3.Connection    Connection object
        create_table_sql:str        a CREATE TABLE statement

    Returns:
        None
    '''
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        raise e


def setup_db_tables() -> None:
    '''
    Main function to create the necessary DB tables.

    Returns:
        None
    '''
    sql_create_wallet_table = ''' CREATE TABLE IF NOT EXISTS wallet (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text NOT NULL,
                                        end_date text
                                    ); '''

    sql_create_assets_table = '''CREATE TABLE IF NOT EXISTS assets (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    type integer NOT NULL,
                                    amount integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text,
                                    wallet_id integer NOT NULL,
                                    FOREIGN KEY (wallet_id) REFERENCES wallet (id)
                                );'''
    
    sql_create_transactions_table = '''CREATE TABLE IF NOT EXISTS transactions (
                                    id integer PRIMARY KEY,
                                    date text NOT NULL,
                                    type integer NOT NULL,
                                    amount integer NOT NULL,
                                    value real NOT NULL,
                                    asset_id integer NOT NULL,
                                    FOREIGN KEY (asset_id) REFERENCES assets (id)
                                );'''

    # create a database connection
    conn = create_connection(
        paths.db_dir + '/' + config.get('db', 'db_name', fallback=None))

    # create tables
    with conn:
        try:
            # create wallet table
            create_table(conn, sql_create_wallet_table)

            # create assets table
            create_table(conn, sql_create_assets_table)

            # create transactions table
            create_table(conn, sql_create_transactions_table)
        except:
            print('Error! cannot create the DB tables.')


if __name__ == '__main__':
    setup_db_tables()

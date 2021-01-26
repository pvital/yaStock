#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# yaStock - yet another Stock Wallet Tracking.
# Copyright (c) 2021 Paulo Vital <paulo@vital.eng.br>
#

import datetime

from typing import Union


class Wallet(object):
    '''
    Wallet class.
    '''

    def __init__(self, name: str, begin_date: str, end_date: Union[str, None]) -> None:
        '''
        Define Wallet class.

        Args:
            name: str       Name for the wallet
            begin_date: str Date when the wallet is created
            end_date: str   Date when the wallet is closed. None if the wallet is still open/valid.

        Returns:
            None
        '''
        self.name = name
        self.begin_date = begin_date
        self.end_date = end_date

    def __str__(self):
        if not self.end_date:
            return f'The wallet {self.name} was created on {self.begin_date} and is open.'
        else:
            return f'The wallet {self.name} was created on {self.begin_date} and was closed on {self.end_date}.'

    def __repr__(self):
        values = {
            'name': self.name,
            'begin_date': self.begin_date,
            'end_date': self.end_date,
        }
        return f'{self.__class__.__name__}({values})'
    
    def is_open(self) -> bool:
        '''
        Return if the wallet is open (valid or in operation).

        Returns:
            bool    True if self.end_date of wallet is None, False otherwise.
        '''
        return True if not self.end_date else False

    def update_wallet(self, new_name: str) -> None:
        '''
        Update the wallet's name.

        Args:
            new_name: str   New name for the wallet.
        '''
        self.name = new_name

    def close_wallet(self) -> None:
        '''
        Close (make it invalid) the wallet.
        '''
        self.end_date = datetime.datetime.utcnow().isoformat()


if __name__ == '__main__':
    my_wallet = Wallet(
        'Test1', 
        datetime.datetime.utcnow().isoformat(),
        None)

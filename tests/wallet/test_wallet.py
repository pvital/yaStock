#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# yaStock - yet another Stock Wallet Tracking.
# Copyright (c) 2021 Paulo Vital <paulo@vital.eng.br>

import datetime
import unittest

import src.wallet.model.wallet as wallet


class TestWallet(unittest.TestCase):
    '''
    Test Cases for Wallet.
    '''

    def setUp(self):
        self.my_wallet1 = wallet.Wallet(
            'Test1',
            datetime.datetime.utcnow().isoformat(),
            None)
        self.my_wallet2 = wallet.Wallet(
            'Test2',
            datetime.datetime(2019, 5, 18, 15, 17, 8, 132263).isoformat(),
            datetime.datetime.utcnow().isoformat())

    def test_is_open(self):
        self.assertTrue(self.my_wallet1.is_open())
        self.assertFalse(self.my_wallet2.is_open())

    def test_update_wallet(self):
        self.my_wallet1.update_wallet('NewTest1')
        self.assertEqual(self.my_wallet1.name, 'NewTest1')

    def test_close_wallet(self):
        self.my_wallet1.close_wallet()
        self.assertFalse(self.my_wallet1.is_open())

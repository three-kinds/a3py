# -*- coding: utf-8 -*-
import unittest

from a3py.improved import readable


class T(unittest.TestCase):
    def test__get_readable_size__success(self):
        self.assertEqual(readable.get_readable_size(10000), "9.77KB")

    # ------------------------------------------------------------------ #
    #  get_readable_duration                                              #
    # ------------------------------------------------------------------ #

    def test__get_readable_duration__zero(self):
        self.assertEqual(readable.get_readable_duration(0), "0s")

    def test__get_readable_duration__seconds_less_than_60(self):
        self.assertEqual(readable.get_readable_duration(1), "1s")
        self.assertEqual(readable.get_readable_duration(59), "59s")

    def test__get_readable_duration__boundary_seconds_to_minutes(self):
        """60 seconds -> 1 minute"""
        self.assertEqual(readable.get_readable_duration(60), "1.0m")

    def test__get_readable_duration__minutes(self):
        self.assertEqual(readable.get_readable_duration(61), "1.02m")
        self.assertEqual(readable.get_readable_duration(3599), "59.98m")

    def test__get_readable_duration__boundary_minutes_to_hours(self):
        """3600 seconds -> 1 hour"""
        self.assertEqual(readable.get_readable_duration(3600), "1.0h")

    def test__get_readable_duration__hours(self):
        self.assertEqual(readable.get_readable_duration(3601), "1.0h")
        self.assertEqual(readable.get_readable_duration(7200), "2.0h")
        self.assertEqual(readable.get_readable_duration(86399), "24.0h")

    def test__get_readable_duration__boundary_hours_to_days(self):
        """86400 seconds -> 1 day"""
        self.assertEqual(readable.get_readable_duration(86400), "1.0d")

    def test__get_readable_duration__days(self):
        self.assertEqual(readable.get_readable_duration(86401), "1.0d")
        self.assertEqual(readable.get_readable_duration(172800), "2.0d")
        self.assertEqual(readable.get_readable_duration(2592000), "30.0d")

    def test__get_readable_duration__custom_round_number(self):
        self.assertEqual(readable.get_readable_duration(61, 0), "1.0m")
        self.assertEqual(readable.get_readable_duration(61, 3), "1.017m")
        self.assertEqual(readable.get_readable_duration(61, 4), "1.0167m")
        self.assertEqual(readable.get_readable_duration(86400, 0), "1.0d")
        self.assertEqual(readable.get_readable_duration(86400, 4), "1.0d")

    def test__get_readable_duration__large_values(self):
        self.assertEqual(readable.get_readable_duration(86400 * 365), "365.0d")
        self.assertEqual(readable.get_readable_duration(86400 * 365 * 10), "3650.0d")

    def test__get_readable_duration__float_seconds(self):
        self.assertEqual(readable.get_readable_duration(0.5), "0.5s")
        self.assertEqual(readable.get_readable_duration(30.5), "30.5s")
        self.assertEqual(readable.get_readable_duration(90.5), "1.51m")

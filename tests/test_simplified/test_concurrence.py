# -*- coding: utf-8 -*-
import sys
import unittest
import time
from threading import Thread
from a3py.simplified import concurrence


class T(unittest.TestCase):

    def test__run_threads_until_any_exits__success(self):
        class TestThread(Thread):

            def __init__(self, seconds: int, *args, **kwargs):
                self.seconds = seconds
                super().__init__(*args, **kwargs)

            def run(self):
                time.sleep(self.seconds)

        thread_list = [
            TestThread(1),
            TestThread(2),
            TestThread(3),
            TestThread(4)
        ]

        start_tick = time.time()
        concurrence.run_threads_until_any_exits(thread_list)
        duration_seconds = time.time() - start_tick
        self.assertTrue(1 < duration_seconds < 2)

    def test__run_threads_until_any_exits__with_exit(self):
        class TestThread(Thread):

            def __init__(self, seconds: int, *args, **kwargs):
                self.seconds = seconds
                super().__init__(*args, **kwargs)

            def run(self):
                time.sleep(self.seconds)
                sys.exit(-1)

        thread_list = [
            TestThread(1),
            TestThread(2),
            TestThread(3),
            TestThread(4)
        ]

        start_tick = time.time()
        concurrence.run_threads_until_any_exits(thread_list)
        duration_seconds = time.time() - start_tick
        self.assertTrue(1 < duration_seconds < 2)

    def test__run_threads_until_any_exits__with_exception(self):
        class TestThread(Thread):

            def __init__(self, seconds: int, *args, **kwargs):
                self.seconds = seconds
                super().__init__(*args, **kwargs)

            def run(self):
                time.sleep(self.seconds)
                raise TypeError("xxx")

        thread_list = [
            TestThread(1),
            TestThread(2),
            TestThread(3),
            TestThread(4)
        ]

        start_tick = time.time()
        concurrence.run_threads_until_any_exits(thread_list)
        duration_seconds = time.time() - start_tick
        self.assertTrue(1 < duration_seconds < 2)

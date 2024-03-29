# -*- coding: utf-8 -*-
import os
import signal
import sys
import unittest
import time
from threading import Event, Thread
from a3py.simplified import concurrence


class T(unittest.TestCase):

    def test__set_exit_signals__success(self):
        pid = os.getpid()
        exit_event = Event()
        concurrence.set_exit_signals(exit_event)
        target_list = [1, 2, 3]

        def _wait():
            exit_event.wait()
            target_list.clear()

        wait_thread = Thread(target=_wait)
        wait_thread.start()

        def _kill():
            os.kill(pid, signal.SIGINT)

        kill_thread = Thread(target=_kill)
        kill_thread.start()
        wait_thread.join()
        self.assertTrue(len(target_list) == 0)

    def test__force_exit_from_threads__success(self):
        import os
        os._exit = sys.exit

        with self.assertRaises(SystemExit):
            concurrence.force_exit_from_threads(reason="reason")

    def test__run_threads_until_any_exits__success(self):
        exit_event = Event()

        class TestThread(concurrence.GracefulExitThread):

            def __init__(self, seconds: int, *args, **kwargs):
                self.seconds = seconds
                super().__init__(*args, **kwargs)

            def run(self):
                time.sleep(self.seconds)

        thread_list = [
            TestThread(1, exit_event=exit_event),
            TestThread(2, exit_event=exit_event),
            TestThread(3, exit_event=exit_event),
            TestThread(4, exit_event=exit_event)
        ]

        start_tick = time.time()
        concurrence.run_threads_until_any_exits(thread_list, exit_event)
        duration_seconds = time.time() - start_tick
        self.assertTrue(duration_seconds >= 4)

    def test__run_threads_until_any_exits__with_exit(self):
        exit_event = Event()

        class TestThread(concurrence.GracefulExitThread):

            def __init__(self, seconds: int, *args, **kwargs):
                self.seconds = seconds
                super().__init__(*args, **kwargs)

            def run(self):
                time.sleep(self.seconds)
                sys.exit(-1)

        thread_list = [
            TestThread(1, exit_event=exit_event),
            TestThread(2, exit_event=exit_event),
            TestThread(3, exit_event=exit_event),
            TestThread(4, exit_event=exit_event)
        ]

        start_tick = time.time()
        concurrence.run_threads_until_any_exits(thread_list, exit_event)
        duration_seconds = time.time() - start_tick
        self.assertTrue(duration_seconds >= 4)

    def test__run_threads_until_any_exits__with_exception(self):
        exit_event = Event()

        class TestThread(concurrence.GracefulExitThread):

            def __init__(self, seconds: int, *args, **kwargs):
                self.seconds = seconds
                super().__init__(*args, **kwargs)

            def run(self):
                time.sleep(self.seconds)
                raise TypeError("xxx")

        thread_list = [
            TestThread(1, exit_event=exit_event),
            TestThread(2, exit_event=exit_event),
            TestThread(3, exit_event=exit_event),
            TestThread(4, exit_event=exit_event)
        ]

        start_tick = time.time()
        concurrence.run_threads_until_any_exits(thread_list, exit_event)
        duration_seconds = time.time() - start_tick
        self.assertTrue(duration_seconds >= 4)

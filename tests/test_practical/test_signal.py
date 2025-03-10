# -*- coding: utf-8 -*-
import os
import unittest
import time
import signal
from multiprocessing import Process, Event
from a3py.practical.signal import PrioritizedSignalHandlerManager, exit_0_handler


class T(unittest.TestCase):
    def setUp(self):
        PrioritizedSignalHandlerManager().clear_handlers(signal.SIGTERM)

    def test__PrioritizedSignalHandlerManager__add_handler(self):
        PrioritizedSignalHandlerManager().add_handler(signal.SIGTERM, exit_0_handler, priority=100)
        self.assertEqual(len(PrioritizedSignalHandlerManager().get_handlers(signal.SIGTERM)), 1)
        PrioritizedSignalHandlerManager().add_handler(signal.SIGTERM, exit_0_handler, priority=200)
        self.assertEqual(len(PrioritizedSignalHandlerManager().get_handlers(signal.SIGTERM)), 2)

    def test__PrioritizedSignalHandlerManager__remove_handler(self):
        PrioritizedSignalHandlerManager().add_handler(signal.SIGTERM, exit_0_handler, priority=100)
        self.assertEqual(len(PrioritizedSignalHandlerManager().get_handlers(signal.SIGTERM)), 1)
        PrioritizedSignalHandlerManager().remove_handler(signal.SIGTERM, exit_0_handler)
        self.assertEqual(len(PrioritizedSignalHandlerManager().get_handlers(signal.SIGTERM)), 0)

    def test__PrioritizedSignalHandlerManager__clear_handlers(self):
        PrioritizedSignalHandlerManager().add_handler(signal.SIGTERM, exit_0_handler, priority=100)
        PrioritizedSignalHandlerManager().add_handler(signal.SIGTERM, exit_0_handler, priority=200)
        self.assertEqual(len(PrioritizedSignalHandlerManager().get_handlers(signal.SIGTERM)), 2)
        PrioritizedSignalHandlerManager().clear_handlers(signal.SIGTERM)
        self.assertEqual(len(PrioritizedSignalHandlerManager().get_handlers(signal.SIGTERM)), 0)

    def test__exit_0_handler(self):
        class _Process(Process):
            def __init__(self, event: Event, *args, **kwargs):
                self._event = event
                super().__init__(*args, **kwargs)

            def run(self):
                PrioritizedSignalHandlerManager().add_handler(signal.SIGTERM, exit_0_handler, priority=100)
                self._event.set()
                while True:
                    time.sleep(1)

        e = Event()
        p = _Process(e)
        p.start()

        e.wait(1)
        self.assertEqual(p.is_alive(), True)
        os.kill(p.pid, signal.SIGTERM)
        p.join()
        self.assertEqual(p.is_alive(), False)
        self.assertEqual(p.exitcode, 0)

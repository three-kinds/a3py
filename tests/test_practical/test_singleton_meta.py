# -*- coding: utf-8 -*-
import unittest

from a3py.practical import singleton_meta


class T(unittest.TestCase):
    def test__success(self):
        class A:
            pass

        class B(metaclass=singleton_meta.SingletonMeta):
            pass

        a1 = A()
        a2 = A()
        b1 = B()
        b2 = B()
        self.assertNotEqual(id(a1), id(a2))
        self.assertEqual(id(b1), id(b2))

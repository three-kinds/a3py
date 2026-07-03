# -*- coding: utf-8 -*-
import unittest

from a3py.practical import dynamic
from tests.test_practical.dynamic import Animal, Bird, Cat, Dog, Eagle
from tests.test_practical import dynamic as test_dynamic


class T(unittest.TestCase):
    def test__find_all_subclasses__success(self):
        animal_class_list = dynamic.find_all_subclasses("tests.test_practical.dynamic", Animal)
        self.assertTrue(Animal not in animal_class_list)
        self.assertTrue(Dog in animal_class_list)
        self.assertTrue(Cat in animal_class_list)
        self.assertTrue(Bird in animal_class_list)
        self.assertTrue(Eagle in animal_class_list)

        bird_class_list = dynamic.find_all_subclasses("tests.test_practical.dynamic", Bird)
        self.assertTrue(Animal not in bird_class_list)
        self.assertTrue(Dog not in bird_class_list)
        self.assertTrue(Cat not in bird_class_list)
        self.assertTrue(Bird not in bird_class_list)
        self.assertTrue(Eagle in bird_class_list)

        another_animal_class_list = dynamic.find_all_subclasses(test_dynamic, Animal)
        self.assertTrue(Animal not in another_animal_class_list)
        self.assertTrue(Dog in another_animal_class_list)
        self.assertTrue(Cat in another_animal_class_list)
        self.assertTrue(Bird in another_animal_class_list)
        self.assertTrue(Eagle in another_animal_class_list)

    def test__import_string(self):
        klass = dynamic.import_string("tests.test_practical.dynamic.Animal")
        self.assertTrue(klass is Animal)

        with self.assertRaises(ImportError):
            dynamic.import_string("test_dynamic")

        with self.assertRaises(ImportError):
            dynamic.import_string("tests.test_practical.dynamic.WangZai")

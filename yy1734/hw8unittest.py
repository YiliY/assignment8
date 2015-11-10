# -*- coding: utf-8 -*-
from hw8input import *
from unittest import TestCase

class test(unittest.TestCase):
    def input_test(self):
        self.assertEqual(positiveInt("1,10,100"),[1,10,100])
        
        self.assertRaises(NonPositiveIntException,positiveInt,"a")
        self.assertRaises(NonPositiveIntException,positiveInt,"0")
        self.assertRaises(NonPositiveIntException,positiveInt,"-1")
        self.assertRaises(NonPositiveIntException,positiveInt,"a,-1")
        self.assertRaises(NonPositiveIntException,positiveInt,"1;3;2")
        
    def revenue_test(self):
        self.assertTrue(revenue(10) <= 1 and revenue(10)>= 1)
        self.assertTrue(revenue(100) <= 1 and revenue(10)>= 1)
        
                
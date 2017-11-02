'''
Created on 24 Nov 2016

@author: Lilian
'''
import unittest
from QTree import BoundingBox


class Test(unittest.TestCase):


    def testContainsPoints(self):
        "contains"
        box = BoundingBox(10, 10, 10, 10)
        self.assertTrue((11,11) in box)
        self.assertTrue((10,10) in box)
        self.assertTrue((19,19) in box)
        self.assertFalse((20,20) in box)

    def testContainsBox(self):
        "contains"
        box = BoundingBox(10, 10, 10, 10)
        self.assertTrue(BoundingBox(10,10,10,10) in box)
        self.assertTrue(BoundingBox(11,13,5,5) in box)
        self.assertFalse(BoundingBox(9,13,5,5) in box)
        self.assertFalse(BoundingBox(13,9,5,5) in box)
        self.assertFalse(BoundingBox(13,13,5,10) in box)
        self.assertFalse(BoundingBox(13,5,10,5) in box)

    def testEqualsBox(self):
        "contains"
        box = BoundingBox(10, 10, 10, 10)
        box1 = BoundingBox(10, 10, 10, 10)
        self.assertEqual(box, box1)
        box2 = BoundingBox(10, 10, 11, 10)
        self.assertNotEqual(box, box2)
        box3 = BoundingBox(10, 10, 10, 11)
        self.assertNotEqual(box, box3)
        box4 = BoundingBox(11, 10, 10, 10)
        self.assertNotEqual(box, box4)
        box5 = BoundingBox(10, 11, 10, 10)
        self.assertNotEqual(box, box5)
        
    def testIntersect(self):
        box = BoundingBox(10, 10, 10, 10)
        box1 = BoundingBox(10, 10, 10, 10)
        self.assertTrue(box.intersect(box1))
        box2 = BoundingBox(5, 5, 10, 30)
        self.assertTrue(box.intersect(box2))
        box3 = BoundingBox(15, 5, 10, 30)
        self.assertTrue(box.intersect(box3))
        box4 = BoundingBox(5, 5, 30, 10)
        self.assertTrue(box.intersect(box4))
        box5 = BoundingBox(5, 15, 30, 10)
        self.assertTrue(box.intersect(box5))
        box6 = BoundingBox(11, 11, 5, 5)
        self.assertTrue(box.intersect(box6))

    def testNotIntersect(self):
        box = BoundingBox(10, 10, 10, 10)
        box1 = BoundingBox(20, 10, 10, 10)
        self.assertFalse(box.intersect(box1))
        box2 = BoundingBox(5, 5, 10, 5)
        self.assertFalse(box.intersect(box2))
        box3 = BoundingBox(5, 5, 5, 30)
        self.assertFalse(box.intersect(box3))
        box4 = BoundingBox(5, 20, 30, 10)
        self.assertFalse(box.intersect(box4))
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
#!/usr/bin/python3
"""
Test Module
"""

import unittest
import contextlib
import pep8
import io
import os
import json
import inspect
from models.rectangle import Rectangle
from models.base import Base
"""from models import rectangle"""


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class"""

    @classmethod
    def setUpClass(cls):
        """Sets and defines before running tests"""
        cls.r1 = Rectangle(1, 2)
        cls.r2 = Rectangle(2, 3)
        cls.r3 = Rectangle(4, 5, 6, 7, 10)

    def test_id(self):
        """Tests id of instance"""
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 10)

    def test_height(self):
        """Tests if attribute was initialized"""
        self.assertEqual(self.r1.height, 2)

    def test_width(self):
        """Tests if attribute was initialized"""
        self.assertEqual(self.r1.width, 1)

    def test_x(self):
        """Tests if attribute was initialized"""
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r3.x, 6)

    def test_y(self):
        """Tests if attribute was initialized"""
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r3.y, 7)

    def test_zero_args(self):
        """Tests missing two required arguments"""
        with self.assertRaises(TypeError):
            r4 = Rectangle()

    def test_one_arg(self):
        """Tests missing one required argument"""
        with self.assertRaises(TypeError):
            r4 = Rectangle(1)

    def test_width_type_err(self):
        """Tests proper validation"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r4 = Rectangle("hello", 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r4 = Rectangle(True, 3)

    def test_height_type_err(self):
        """Tests proper validation"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r4 = Rectangle(4, "hello")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r4 = Rectangle(5, False)

    def test_x_type_err(self):
        """Tests proper validation"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r4 = Rectangle(6, 7, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r4 = Rectangle(8, 9, True)

    def test_y_type_err(self):
        """Tests proper validation"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r4 = Rectangle(1, 2, 3, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r4 = Rectangle(4, 5, 6, False)

    def test_width_value_err(self):
        """Tests proper validation"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r4 = Rectangle(-2, 3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r4 = Rectangle(0, 1)

    def test_height_value_err(self):
        """Tests proper validation"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r4 = Rectangle(2, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r4 = Rectangle(3, 0)

    def test_x_value_err(self):
        """Tests proper validation"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r4 = Rectangle(3, 2, -1)

    def test_y_value_err(self):
        """Tests proper validation"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r4 = Rectangle(3, 2, 0, -1)

    def test_area(self):
        """Tests the area"""
        self.assertEqual(self.r3.area(), 20)

    def test_area_arg(self):
        """Tests the function with unneeded argument"""
        with self.assertRaises(TypeError):
            x = self.r1.area(3)

    def test_display(self):
        """Tests the simple display"""
        with io.StringIO() as text, contextlib.redirect_stdout(text):
            self.r1.display()
            result = text.getvalue()
            self.assertEqual(result, ("#" * 1 + "\n") * 2)

    def test_display_adv(self):
        """Tests the advanced display"""
        with io.StringIO() as text, contextlib.redirect_stdout(text):
            self.r3.display()
            result = text.getvalue()
            self.assertEqual(result, "\n" * 7 + (" " * 6 + "#" * 4 + "\n") * 5)

    def test_display_args(self):
        """Tests function with unneeded argument"""
        with self.assertRaises(TypeError):
            self.r1.display(3)

    def test_str(self):
        """Tests the string representation"""
        self.assertEqual(str(self.r2), "[Rectangle] (2) 0/0 - 2/3")
        self.assertEqual(str(self.r3), "[Rectangle] (10) 6/7 - 4/5")

    def test_update_args(self):
        """Tests udpate with *args"""
        r5 = Rectangle(7, 7, 7, 7, 7)
        r5.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r5), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_args_set(self):
        """Tests update usage of setters with *args"""
        r = Rectangle(1, 1, 0, 0, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(1, "hello")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(1, 1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(1, 1, 1, 1, "hello")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 1, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(1, 1, 1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(1, 1, 1, 1, -1)

    def test_update_extra_args(self):
        """Tests update with too many args"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(2, 2, 2, 2, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (2) 2/2 - 2/2")

    def test_update_no_args(self):
        """Tests update without args"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")

    def test_update_kwargs(self):
        """Tests update with **kwargs"""
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(height=10)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/10")
        r.update(width=11, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/0 - 11/10")
        r.update(y=3, width=4, x=5, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 5/3 - 4/10")
        r.update(x=6, height=7, y=8, width=9)
        self.assertEqual(str(r), "[Rectangle] (89) 6/8 - 9/7")

    def test_update_kwargs_set(self):
        """Tests update usage of setters with **kwargs"""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.update(width="hello")
        with self.assertRaises(TypeError):
            r.update(height="hello")
        with self.assertRaises(TypeError):
            r.update(x="hello")
        with self.assertRaises(TypeError):
            r.update(y="hello")
        with self.assertRaises(ValueError):
            r.update(width=-1)
        with self.assertRaises(ValueError):
            r.update(width=0)
        with self.assertRaises(ValueError):
            r.update(height=-1)
        with self.assertRaises(ValueError):
            r.update(height=0)
        with self.assertRaises(ValueError):
            r.update(x=-1)
        with self.assertRaises(ValueError):
            r.update(y=-1)

    def test_mixed_update(self):
        """Tests update with mixed *args and **kwargs"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(2, 2, 2, 2, 2, width=3, height=3, x=3, y=3, id=3)
        self.assertEqual(str(r), "[Rectangle] (2) 2/2 - 2/2")

    def test_random_kwargs(self):
        """Tests for unexpected **kwargs"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(hello=2)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")

    def test_to_dict(self):
        """Tests to_dictionary method"""
        r5 = Rectangle(11, 12, 13, 14, 20)
        d4 = r5.to_dictionary()
        self.assertEqual({"id": 20, "width": 11, "height": 12, "x": 13,
                          "y": 14}, d4)
        self.assertTrue(type(d4) is dict)
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(**d4)
        self.assertEqual(str(r), str(r5))
        self.assertNotEqual(r, r5)

    def test_save_to_file(self):
        """Tests save_to_file method"""
        r1 = Rectangle(1, 1, 1, 1, 1)
        r2 = Rectangle(2, 2, 2, 2, 2)
        l = [r1, r2]
        Rectangle.save_to_file(l)
        with open("Rectangle.json", "r") as f:
            ls = [r1.to_dictionary(), r2.to_dictionary()]
            self.assertEqual(json.dumps(ls), f.read())

    def test_savetofile_empty(self):
        """Tests function with empty list"""
        l = []
        Rectangle.save_to_file(l)
        with open("Rectangle.json", "r") as f:
            self.assertEqual('[]', f.read())

    def test_savetofile_None(self):
        """Tests function with None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual('[]', f.read())

    def test_create(self):
        """Tests create method"""
        r1 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        r2 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        r1c = Rectangle.create(**r1)
        r2c = Rectangle.create(**r2)
        self.assertEqual("[Rectangle] (2) 4/0 - 2/3", str(r1c))
        self.assertEqual("[Rectangle] (9) 7/8 - 5/6", str(r2c))
        self.assertIsNot(r1, r1c)
        self.assertIsNot(r2, r2c)
        self.assertNotEqual(r1, r1c)
        self.assertNotEqual(r2, r2c)

    def test_loadfromfile_nofile(self):
        """Tests load_from_file with non existing file"""
        try:
            os.remove("Rectangle.json")
        except:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_loadfromfile_emptyfile(self):
        """Tests load_from_file with empty file"""
        try:
            os.remove("Rectangle.json")
        except:
            pass
        open("Rectangle.json", 'a').close()
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file(self):
        """Tests load_from_file"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        li = [r1, r2]
        Rectangle.save_to_file(li)
        lo = Rectangle.load_from_file()
        self.assertTrue(type(lo) is list)
        self.assertEqual(len(lo), 2)
        r1c = lo[0]
        r2c = lo[1]
        self.assertTrue(type(r1c) is Rectangle)
        self.assertTrue(type(r2c) is Rectangle)
        self.assertEqual(str(r1), str(r1c))
        self.assertEqual(str(r2), str(r2c))
        self.assertIsNot(r1, r1c)
        self.assertIsNot(r2, r2c)
        self.assertNotEqual(r1, r1c)
        self.assertNotEqual(r2, r2c)


class TestRectangleDocs(unittest.TestCase):
    """Tests the Rectangle class' style and documentation"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.rect_funcs = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_pep8_conformance_rectangle(self):
        """Test that models/rectangle.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_rectangle(self):
        """Test that tests/test_models/test_rectangle.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.rect_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)

#!/usr/bin/python3
"""
Tests classes and functions in the BaseModel class
"""
from models.base_model import BaseModel
from datetime import datetime
import os
from time import sleep
import unittest

class TestBaseModel(unittest.TestCase):
    """Tests the correct initiation of the BaseModel class"""
    
    def test_iniation_no_kwargs(self):
        cls = BaseModel()
        self.assertIsInstance(cls, BaseModel)

    def test_iniation_kwargs(self):
        cls = BaseModel(id="NO_name", age=15)
        self.assertIsInstance(cls, BaseModel)


class TestBaseNoKwargs(unittest.TestCase):
    """Tests the existance of public attributes"""
    def assertDateTimeAlmostEqual(self, time1, time2):
        self.assertEqual(time1.year, time2.year)
        self.assertEqual(time1.month, time2.month)
        self.assertEqual(time1.day, time2.day)
        self.assertEqual(time1.hour, time2.hour)
        self.assertEqual(time1.minute, time2.minute)

    def setUp(self):
        self.cls1_creation = datetime.today()
        self.cls1 = BaseModel()

        self.cls2 = BaseModel()

        self.cls3 = BaseModel()
        self.cls3.name = "Random Name"
        self.cls3.number = 444
        self.cls3_obj = self.cls3.to_dict()

        self.cls4 = BaseModel()

    def test_id_exists(self):
        self.assertIn("id", self.cls1.__dict__.keys())
        self.assertIn("id", self.cls2.__dict__.keys())
        self.assertIn("id", self.cls3.__dict__.keys())

    def test_id_type(self):
        self.assertIsInstance(self.cls1.id, str)
        self.assertIsInstance(self.cls2.id, str)

    def test_id_uniquness(self):
        NUMOFTESTS = 100
        cls_id_lst = [BaseModel().id for x in range(NUMOFTESTS)]
        for x in range(NUMOFTESTS):
            for y in range(x + 1, NUMOFTESTS):
                self.assertNotEqual(cls_id_lst[x], cls_id_lst[y])

    def test_time_exists(self):
        self.assertIn("created_at", self.cls1.__dict__.keys())
        self.assertIn("created_at", self.cls2.__dict__.keys())
        self.assertIn("created_at", self.cls3.__dict__.keys())

        self.assertIn("updated_at", self.cls1.__dict__.keys())
        self.assertIn("updated_at", self.cls2.__dict__.keys())
        self.assertIn("updated_at", self.cls3.__dict__.keys())

    def test_time_type(self):
        self.assertIsInstance(self.cls1.created_at, datetime)
        self.assertIsInstance(self.cls2.created_at, datetime)
        self.assertIsInstance(self.cls3.created_at, datetime)

        self.assertIsInstance(self.cls1.updated_at, datetime)
        self.assertIsInstance(self.cls2.updated_at, datetime)
        self.assertIsInstance(self.cls3.updated_at, datetime)

    def test_time(self):
        self.assertDateTimeAlmostEqual(self.cls1_creation,
                                       self.cls1.created_at)

        self.assertDateTimeAlmostEqual(self.cls1.created_at,
                                       self.cls1.updated_at)

        self.cls1_update = datetime.today()
        self.cls1.id = "Random string has been set to be the id"
        self.assertDateTimeAlmostEqual(self.cls1_update, self.cls1.updated_at)

    def test_str(self):
        returned = self.cls1.__str__()
        expected = "[{}] ({}) {}".format(self.cls1.__class__.__name__,
                                         self.cls1.id, self.cls1.__dict__)
        self.assertEqual(returned, expected)

    def test_save_exist(self):
        self.assertIn("save", self.cls2.__dir__())

    def test_save(self):
        self.cls2_update = datetime.today()
        self.cls2.save()
        self.assertDateTimeAlmostEqual(self.cls2_update, self.cls2.updated_at)

    def test_to_dict_exists(self):
        self.assertIn("to_dict", self.cls3.__dir__())

    def test_to_dict_keys(self):
        self.assertIn("updated_at", self.cls3_obj.keys())
        self.assertIn("created_at", self.cls3_obj.keys())

    def test_to_dict(self):
        self.assertEqual(self.cls3_obj["updated_at"],
                         self.cls3.updated_at.isoformat())
        self.assertEqual(self.cls3_obj["created_at"],
                         self.cls3.created_at.isoformat())

        self.cls3_dic = {
            "name": "Random Name",
            "number": 444,
            "id": self.cls3.id,
            "updated_at": str(self.cls3.updated_at.isoformat()),
            "created_at": str(self.cls3.created_at.isoformat()),
            "__class__": self.cls3.__class__.__name__,
        }
        self.assertDictEqual(self.cls3_dic, self.cls3_obj)

class TestBaseKwargs(unittest.TestCase):
    """Tests the existance of public attributes"""
    
    def assertDateTimeAlmostEqual(self, time1, time2):
        self.assertEqual(time1.year, time2.year)
        self.assertEqual(time1.month, time2.month)
        self.assertEqual(time1.day, time2.day)
        self.assertEqual(time1.hour, time2.hour)
        self.assertEqual(time1.minute, time2.minute)

    def setUp(self):
        self.some_time = str(datetime(1290, 2, 15, 12, 34, 56, 11).isoformat())

        self.cls1 = BaseModel(id="id")
        self.cls1_obj = self.cls1.to_dict()
        self.cls2 = BaseModel(updated_at=self.some_time)
        self.cls2_obj = self.cls2.to_dict()

        self.cls3 = BaseModel(created_at=self.some_time)
        self.cls3.name = "Random Name"
        self.cls3.number = 444
        self.cls3_obj = self.cls3.to_dict()

        self.cls4 = BaseModel(created_at=self.some_time, id="Nones")
        self.cls4_obj = self.cls4.to_dict()

    def test_id_type(self):
        self.assertIsInstance(self.cls1.id, str)

    def test_time(self):
        TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
        self.assertDateTimeAlmostEqual(
            datetime.strptime(self.some_time, TIME_FORMAT),
            self.cls2.updated_at)
        self.assertDateTimeAlmostEqual(
            datetime.strptime(self.some_time, TIME_FORMAT),
            self.cls3.created_at)

class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_contains_added_attributes(self):
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 98
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)

class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

if __name__ == "__main__":
    unittest.main()

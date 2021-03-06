import os
import unittest

from PIL import Image
from templatestorage import Store


class TemplateStoreTest(unittest.TestCase):
    def test_adding_images(self):
        # make test store
        store_path = "tests/assets/TestStoreAdd"
        if os.path.exists(store_path):
            os.remove(store_path)
        ts = Store(store_path)
        # define template dict and open images
        tns = ["big_building", "big_tree", "cathedral", "fireworks", "hdr", ]
        td = {tn: Image.open("tests/assets/"+tn+".png") for tn in tns}
        # save template dict to store
        ts.add_templates(td)
        # read images from store and compare
        for name in td:
            # if image is not the same as in original dict, fail
            self.assertTrue(td[name] == ts.get_template(name))
        # pass if no fails
        self.assertTrue(True)

    def test_removing_images(self):
        # make test store
        store_path = "tests/assets/TestStoreRemove"
        if os.path.exists(store_path):
            os.remove(store_path)
        ts = Store(store_path)
        # define template dict and open images
        tns = ["big_building", "big_tree", "cathedral", "fireworks", "hdr", ]
        td = {tn: Image.open("tests/assets/"+tn+".png") for tn in tns}
        # save template dict to store
        ts.add_templates(td)
        # remove template from store and list
        ts.remove_templates(["cathedral", "hdr"])
        td.pop("cathedral")
        td.pop("hdr")
        # read images from store and compare
        for name in td:
            # if image is not the same as in original dict, fail
            self.assertTrue(td[name] == ts.get_template(name))
        # pass if no fails
        self.assertTrue(True)

    def test_compression(self):
        # make test store
        store_path = "tests/assets/TestStoreCompression"
        if os.path.exists(store_path):
            os.remove(store_path)
        ts = Store(store_path)
        # define template images
        tns = next(
            os.walk("tests/assets"),
            (None, None, [])
        )[2]
        tns = [tn for tn in tns if tn.endswith('.png')]
        # build template dictionary
        td = {tn: Image.open("tests/assets/"+tn) for tn in tns}
        # save template dict to store
        ts.add_templates(td)
        # compare sizes of files
        tp_size = sum([os.path.getsize("tests/assets/"+tn)
                       for tn in tns])
        ts_size = os.path.getsize(store_path)
        print(f"Compression Ratio: {tp_size/ts_size}", end=". ")
        self.assertTrue(ts_size < tp_size)

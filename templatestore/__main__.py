"""
Module for template-store.

Can be imported, or ran from comandline
"""
import argparse
import bz2
import pickle
from copy import deepcopy
from io import BufferedReader

from PIL import Image


class TemplateStore:
    """
    This class handles interactions with the template store.

    Templates will be stored as a compressed pickle to reduce application size.
    """

    def __init__(self, store_name="store"):
        """Templatestore init.

        Args:
            store_name (str, optional): name of store file. Defaults to "store".
        """
        self.store_name = store_name
        self.template_store = self.open_store()

    def add_templates(self, template_dict: dict[str, Image.Image]):
        """Add templates to the store.

        Args:
            template_dict (dict[str, Image]): a dictionary of strings and PIL Images
        """
        # make template store if none
        if self.template_store is None:
            self.template_store = deepcopy(template_dict)
            self.save_store()
        else:
            # update store with new dict
            self.template_store.update(template_dict)
            self.save_store()

    def remove_template(self, template_name):
        """Remove a template from the store by name.

        Args:
            template_name (str): name of template to remove
        """
        if self.template_store is not None:
            # remove element from dict and update store
            try:
                self.template_store.pop(template_name)
            except KeyError:
                print(f"Template, {template_name} not found in store.")
            self.save_store()

    def open_store(self):
        """Open a store file and returns the contents.

        Returns:
            dict[str, Image]: a dictionary of strings and PIL Images
        """
        try:
            with open(self.store_name, "rb") as store_file:
                return self.decompress_pickle(store_file)
        except:
            return None

    def save_store(self):
        """Write template_dict to store file."""
        self.compressed_pickle(self.store_name, self.template_store)

    def get_template(self, template_name):
        """Get template from store.

        Args:
            template_name (str): the name of the template

        Returns:
            Image: the template image
        """
        if self.template_store is not None:
            return self.template_store[template_name]
        else:
            return None

    def compressed_pickle(self, title, data: dict):
        """Save data as a pickle and compresses.

        Args:
            title (str): name of pickle
            data (Any): data to store
        """
        with bz2.BZ2File(title, "w") as f:
            pickle.dump(data, f)

    def decompress_pickle(self, file: BufferedReader):
        """Open and decompresse a pickle.

        Args:
            file (BufferedReader): a file to decompress

        Returns:
            Any: the stored data
        """
        data = bz2.BZ2File(file, "rb")
        data = pickle.load(data)
        return data


def run_parser():
    """Parse arguments.

    Returns:
        Namespace: populated namespace from arguments
    """
    parser = argparse.ArgumentParser(
        description="Import images into a template store")
    parser.add_argument(
        "-s",
        "--storepath",
        dest="store_path",
        help="store file to update or create, defaults to 'store'",
    )
    parser.set_defaults(store_path="store")
    parser.add_argument(
        "-l", "--list", dest="list", action="store_true", help="list templates in store"
    )
    parser.set_defaults(list=False)
    parser.add_argument(
        "-f",
        "--files",
        dest="files",
        nargs="+",
        help="a file or list of files to add, ie 'img1.png img2.png'",
    )
    parser.add_argument(
        "-r",
        "--remove",
        dest="remove",
        nargs="+",
        help="a file or list of files to remove, ie 'img1.png img2.png'",
    )
    args = parser.parse_args()
    return args


def main():
    """Create or update a template store."""
    # parse args
    args = run_parser()
    # open template store
    ts = TemplateStore(args.store_path)

    # list files
    if args.list and ts.template_store is not None:
        for entry in ts.template_store:
            print(entry, end=", ")
    else:
        # add files to template store
        if args.files is not None:
            td = {}
            for file in args.files:
                td.update({file.split(".")[0]: Image.open(file)})
            ts.add_templates(td)
        # remove files from template store
        if args.remove is not None:
            td = {}
            for file_to_remove in args.remove:
                ts.remove_template(file_to_remove)


if __name__ == "__main__":
    main()
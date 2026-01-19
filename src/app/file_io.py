# file_io.py
import os
import base64


def encode_file(path):
    """Encode a file as a base64 string.

    Args:
        path (str): The path to the file to encode.

    Returns:
        str: The base64-encoded string representation of the file.
    """
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def list_files(dirpath):
    """List all files in a directory.

    Args:
        dirpath (str): The path to the directory to list.

    Yields:
        tuple: A tuple containing the file name and path for each file.
    """
    for name in os.listdir(dirpath):
        path = os.path.join(dirpath, name)
        if os.path.isfile(path):
            yield name, path

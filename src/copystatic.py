import os
import shutil


def copy_static(source, destination):
    """
    Recursively copy all files and directories from source to destination.
    """

    # Remove the destination directory if it exists.
    if os.path.exists(destination):
        shutil.rmtree(destination)

    # Create the destination directory.
    os.mkdir(destination)

    # Walk through everything in the source directory.
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isfile(source_path):
            print(f"Copying file: {source_path} -> {destination_path}")
            shutil.copy(source_path, destination_path)
        else:
            print(f"Entering directory: {source_path}")
            copy_static(source_path, destination_path)

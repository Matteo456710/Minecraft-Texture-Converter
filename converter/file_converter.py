import os
import shutil


def convert_file(source, destination):
    """
    Converts or copies a single file.
    """

    file_extension = os.path.splitext(source)[1].lower()

    os.makedirs(
        os.path.dirname(destination),
        exist_ok=True
    )

    if file_extension == ".png":
        handle_png(source, destination)

    elif file_extension == ".json":
        handle_json(source, destination)

    elif file_extension == ".mcmeta":
        handle_mcmeta(source, destination)

    else:
        shutil.copy2(
            source,
            destination
        )


def handle_png(source, destination):
    """
    PNG textures are copied directly.
    """

    shutil.copy2(
        source,
        destination
    )


def handle_json(source, destination):
    """
    JSON conversion will be added later.
    """

    shutil.copy2(
        source,
        destination
    )


def handle_mcmeta(source, destination):
    """
    Java animation files are handled later.
    """

    pass
import zipfile
import os


def extract_zip(zip_path, output_folder):
    with zipfile.ZipFile(zip_path, "r") as zip_file:
        zip_file.extractall(output_folder)


def create_zip(folder_path, output_zip):
    with zipfile.ZipFile(output_zip, "w") as zip_file:

        for root, dirs, files in os.walk(folder_path):

            for file in files:
                filepath = os.path.join(root, file)

                zip_file.write(
                    filepath,
                    os.path.relpath(filepath, folder_path)
                )
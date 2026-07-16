import os

from converter.mappings import JAVA_TO_BEDROCK_PATHS
from converter.file_converter import convert_file


def convert_textures(java_texture_folder, bedrock_texture_folder):
    """
    Copies textures while translating known folder names.
    """

    for root, dirs, files in os.walk(java_texture_folder):

        relative_path = os.path.relpath(root, java_texture_folder)

        parts = relative_path.split(os.sep)

        if parts[0] in JAVA_TO_BEDROCK_PATHS:
            parts[0] = JAVA_TO_BEDROCK_PATHS[parts[0]]

        destination_folder = os.path.join(
            bedrock_texture_folder,
            *parts
        )

        os.makedirs(destination_folder, exist_ok=True)

        for file in files:
            source = os.path.join(root, file)
            destination = os.path.join(destination_folder, file)

            convert_file(
                source,
                destination
            )
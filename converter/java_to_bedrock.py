import os
import shutil

from converter.zip_utils import extract_zip, create_zip
from converter.bedrock_utils import create_manifest
from converter.mappings import JAVA_TO_BEDROCK_PATHS


def convert_java_to_bedrock(input_path, output_path):
    """
    Basic Java Resource Pack to Bedrock Texture Pack conversion.
    """

    temp_folder = "temp_conversion"

    if os.path.exists(temp_folder):
        shutil.rmtree(temp_folder)

    os.makedirs(temp_folder)

    # ZIP entpacken
    extract_zip(input_path, temp_folder)

    bedrock_folder = os.path.join(
        temp_folder,
        "bedrock_pack"
    )

    os.makedirs(bedrock_folder)

    textures_folder = os.path.join(
        bedrock_folder,
        "textures"
    )

    os.makedirs(textures_folder)

    java_texture_folder = os.path.join(
        temp_folder,
        "assets",
        "minecraft",
        "textures"
    )

    if os.path.exists(java_texture_folder):

        shutil.copytree(
            java_texture_folder,
            textures_folder,
            dirs_exist_ok=True
        )
    create_manifest(
        bedrock_folder
    )
    
    create_zip(
        bedrock_folder,
        output_path
    )

    shutil.rmtree(temp_folder)

    return output_path
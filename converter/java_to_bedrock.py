import os
import shutil

from converter.zip_utils import extract_zip, create_zip
from converter.bedrock_utils import create_manifest
from converter.texture_converter import convert_textures
from converter.icon_converter import convert_icon
from converter.java_utils import read_pack_metadata
from converter.animation_converter import convert_animations


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

        convert_textures(
            java_texture_folder,
            textures_folder
        )
        convert_animations(
            java_texture_folder,
            textures_folder
        )
    convert_icon(
        temp_folder,
        bedrock_folder
    )    
    metadata = read_pack_metadata(
        temp_folder
    )
    create_manifest(
        bedrock_folder,
        metadata
    )
    create_zip(
        bedrock_folder,
        output_path
    )

    shutil.rmtree(temp_folder)

    return output_path
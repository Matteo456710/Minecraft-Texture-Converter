import os
import shutil


def convert_icon(java_folder, bedrock_folder):
    """
    Converts Java pack.png to Bedrock pack_icon.png.
    """

    java_icon = os.path.join(
        java_folder,
        "pack.png"
    )

    if os.path.exists(java_icon):

        bedrock_icon = os.path.join(
            bedrock_folder,
            "pack_icon.png"
        )

        shutil.copy2(
            java_icon,
            bedrock_icon
        )
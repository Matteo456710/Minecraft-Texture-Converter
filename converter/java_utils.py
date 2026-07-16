import json
import os


def read_pack_metadata(java_folder):
    """
    Reads pack.mcmeta from a Java Resource Pack.
    """

    mcmeta_path = os.path.join(
        java_folder,
        "pack.mcmeta"
    )

    default_data = {
        "name": "Converted Texture Pack",
        "description": "Converted from Java Resource Pack"
    }

    if not os.path.exists(mcmeta_path):
        return default_data

    try:
        with open(
            mcmeta_path,
            "r",
            encoding="utf-8"
        ) as file:
            data = json.load(file)

    except (json.JSONDecodeError, UnicodeDecodeError):
        return default_data

    pack_data = data.get(
        "pack",
        {}
    )

    description = pack_data.get(
        "description",
        default_data["description"]
    )

    return {
        "name": description,
        "description": description
    }
import json


def read_pack_metadata(pack_file):

    with open(pack_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    pack = data.get("pack", {})

    return {
        "description": pack.get(
            "description",
            "Converted Texture Pack"
        )
    }
import os


def read_java_pack_structure(java_folder):
    """
    Detects available parts of a Java Resource Pack.
    """

    structure = {
        "pack_mcmeta": False,
        "textures": False,
        "models": False,
        "blockstates": False
    }

    if os.path.exists(
        os.path.join(java_folder, "pack.mcmeta")
    ):
        structure["pack_mcmeta"] = True


    assets_folder = os.path.join(
        java_folder,
        "assets",
        "minecraft"
    )


    textures_folder = os.path.join(
        assets_folder,
        "textures"
    )

    if os.path.exists(textures_folder):
        structure["textures"] = True


    models_folder = os.path.join(
        assets_folder,
        "models"
    )

    if os.path.exists(models_folder):
        structure["models"] = True


    blockstates_folder = os.path.join(
        assets_folder,
        "blockstates"
    )

    if os.path.exists(blockstates_folder):
        structure["blockstates"] = True


    return structure
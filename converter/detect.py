import zipfile


def detect_pack_type(filepath):
    """
    Detects, if it's a Bedrock or an Java Texture Pack.
    """

    with zipfile.ZipFile(filepath, "r") as zip_file:

        files = zip_file.namelist()

        # Java Resource Pack are known for pack.mcmeta
        if "pack.mcmeta" in files:
            return "Java Resource Pack"

        # Bedrock Packs have manifest.json
        if "manifest.json" in files:
            return "Bedrock Texture Pack"

        return "Unknown format"
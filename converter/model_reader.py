import json
import os


def read_models(java_folder):
    """
    Reads all Java model JSON files.
    Returns a dictionary:
    {
        "item/diamond_sword": {...},
        "block/stone": {...}
    }
    """

    models = {}

    models_folder = os.path.join(
        java_folder,
        "assets",
        "minecraft",
        "models"
    )

    if not os.path.exists(models_folder):
        return models

    for root, dirs, files in os.walk(models_folder):

        for file in files:

            if not file.endswith(".json"):
                continue

            file_path = os.path.join(root, file)

            relative_path = os.path.relpath(
                file_path,
                models_folder
            )

            model_name = relative_path.replace("\\", "/")
            model_name = model_name[:-5]  # .json entfernen

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as f:

                models[model_name] = json.load(f)

    return models
import json
import uuid
import os


def create_manifest(output_folder, metadata):

    manifest = {
        "format_version": 2,
        "header": {
            "name": metadata["name"],
            "description": metadata["description"],
            "uuid": str(uuid.uuid4()),
            "version": [1, 0, 0],
            "min_engine_version": [1, 16, 0]
        },
        "modules": [
            {
                "type": "resources",
                "uuid": str(uuid.uuid4()),
                "version": [1, 0, 0]
            }
        ]
    }

    manifest_path = os.path.join(
        output_folder,
        "manifest.json"
    )

    with open(manifest_path, "w", encoding="utf-8") as file:
        json.dump(
            manifest,
            file,
            indent=4
        )
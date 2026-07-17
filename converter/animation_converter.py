import json
import os


DEFAULT_ANIMATIONS = {
    "water_still.png.mcmeta": "water_still",
    "lava_still.png.mcmeta": "lava_still",
    "fire_0.png.mcmeta": "fire",
    "portal.png.mcmeta": "portal"
}


def convert_animations(java_texture_folder, bedrock_texture_folder):
    """
    Converts common Java animations to Bedrock flipbook format.
    """

    animations = []

    for root, dirs, files in os.walk(java_texture_folder):

        for file in files:

            if file in DEFAULT_ANIMATIONS:

                animation_name = DEFAULT_ANIMATIONS[file]

                animations.append({
                    "flipbook_texture": animation_name,
                    "ticks_per_frame": 1
                })

    if animations:
        create_flipbook_file(
            bedrock_texture_folder,
            animations
        )


def create_flipbook_file(folder, animations):

    path = os.path.join(
        folder,
        "flipbook_textures.json"
    )

    data = {
        "flipbook_texture": animations
    }

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )
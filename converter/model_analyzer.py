def analyze_models(models):
    """
    Analyzes loaded Java model files.
    """

    analyzed = {}

    for name, model in models.items():

        analyzed[name] = {
            "parent": model.get("parent"),
            "textures": model.get("textures", {}),
            "elements": model.get("elements", []),
            "display": model.get("display", {}),
            "overrides": model.get("overrides", [])
        }

    return analyzed
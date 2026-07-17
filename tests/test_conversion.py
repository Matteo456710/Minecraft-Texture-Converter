from converter.java_to_bedrock import convert_java_to_bedrock
from converter.java_pack_reader import read_java_pack_structure
from converter.model_reader import read_models
from converter.model_analyzer import analyze_models

input_file = "uploads/test_java_pack.zip"

output_file = "output/converted_bedrock_pack.zip"

convert_java_to_bedrock(
    input_file,
    output_file,
)

structure = read_java_pack_structure(
    "uploads/test_java_pack"
)
print(structure)

models = read_models(
    "uploads/test_java_pack"
)
print(models.keys())

models = read_models(
    "uploads/test_java_pack"
)

analyzed = analyze_models(models)

for name, model in analyzed.items():

    print(name)
    print(model)

print("Conversion finished")
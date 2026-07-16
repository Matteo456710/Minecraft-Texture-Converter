from converter.java_to_bedrock import convert_java_to_bedrock


input_file = "uploads/test_java_pack.zip"

output_file = "output/converted_bedrock_pack.zip"


convert_java_to_bedrock(
    input_file,
    output_file
)

print("Conversion finished")
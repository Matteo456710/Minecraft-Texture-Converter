from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Minecraft Texture Converter lauft!"

if __name__ == "__main__":
    app.run(debug=True)
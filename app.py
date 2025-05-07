from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ Home Route
@app.route("/", methods=["GET"])
def home():
    return "Welcome to AI PDF Reader API"

# ✅ Upload PDF Route
@app.route("/upload", methods=["POST"])
def upload_pdf():
    return jsonify({"message": "Upload endpoint working"})

# ✅ Ask AI Route
@app.route("/ask", methods=["POST"])
def ask_question():
    return jsonify({"message": "Ask endpoint working"})

if __name__ == "__main__":
    app.run(debug=True)

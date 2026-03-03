from flask import Flask, request, jsonify

app = Flask(__name__)

notes = []

@app.route("/")
def home():
    return {"message": "Secure Notes API running"}

@app.route("/notes", methods=["POST"])
def add_note():
    data = request.json
    note = data.get("note")
    notes.append(note)
    return jsonify({"message": "Note added", "note": note}), 201

@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify({"notes": notes})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
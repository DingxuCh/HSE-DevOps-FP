from flask import Flask, request, jsonify
from sympy import sympify

app = Flask(__name__)

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    try:
        expr = data.get("expression", "")
        result = sympify(expr).evalf()
        return jsonify({"result": float(result)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

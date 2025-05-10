from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    expr = data.get("expression", "")
    try:
        allowed = set("0123456789+-*/.() ")
        if not all(char in allowed for char in expr):
            raise ValueError("非法字符")
        result = eval(expr, {"__builtins__": None})
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

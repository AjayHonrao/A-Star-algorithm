from flask import Flask, request, jsonify, render_template
from mat import find_path_and_modify_matrix  # Import your function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_matrix', methods=['POST'])
def process_matrix():
    data = request.get_json()
    matrix = data.get('matrix')
    if matrix:
        modified_matrix = find_path_and_modify_matrix(matrix)
        return jsonify(modified_matrix)
    else:
        return jsonify({"error": "No matrix provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)

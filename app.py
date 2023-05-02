from flask import Flask, render_template
from flask import request, jsonify
import ast
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


@app.route('/')
def hello_world():
    return render_template('prototype.html')

@app.route('/description')
def description():
    return render_template('description.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

def semantic_analysis(program):
    errors = []

    # Parse the Python program
    try:
        parsed_program = ast.parse(program)
    except SyntaxError as e:
        errors.append(f"Syntax error: {e}")
        return errors

    # Traverse the AST and check for semantic errors
    for node in ast.walk(parsed_program):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute):
                if node.func.attr == 'append':
                    if isinstance(node.func.value, ast.Name) and node.func.value.id == 'list':
                        errors.append(f"Using 'list.append' is not recommended, use the '+' operator instead. Line {node.lineno}")
            elif isinstance(node.func, ast.Name):
                if node.func.id == 'print':
                    errors.append(f"Using 'print' is not recommended, use logging instead. Line {node.lineno}")

    return errors

@app.route('/analyze', methods=['POST'])
def analyze():
    app.logger.info("Got req")
    input_data = request.json
    app.logger.info(input_data)
    output_data = semantic_analysis(input_data)
    response = {'result': output_data}
    return jsonify(response)


if __name__=="main":
    app.run(debug=True)

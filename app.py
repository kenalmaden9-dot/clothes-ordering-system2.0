from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Example ordering route
@app.route('/order', methods=['POST'])
def order():
    item = request.form.get('item')
    quantity = request.form.get('quantity')
    return f"You ordered {quantity} of {item}!"

# Run locally (not needed on PythonAnywhere, but useful if you test elsewhere)
if __name__ == '__main__':
    app.run(debug=True)

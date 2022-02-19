from flask import Flask, render_template, redirect, request
# import pyautogui


app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
        buttons=[("/but/0", "but02222222"), ("/but/2", "but2")],
    )

@app.route('/addButton/<int:id>/<int:step>/<int:type>')
def addButton(id, step, type=0):
    control = [0, 0, 0, 0, 0]
    control[step] = 1
    return render_template(
        'addButton.html',
        id=id,
        type=type,
        control=control,
    )

@app.route('/addGroup')
def addGroup():
    return render_template('addGroup.html')

@app.route('/add', methods=["POST"])
def add():
    request.form.get("id")
    request.form.get("type")
    request.form.get("name")
    request.form.get("x")
    request.form.get("y")
    request.form.get("duration")
    request.form.get("text")
    request.form.get("y")

    return redirect("/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

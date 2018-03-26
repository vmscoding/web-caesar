from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <form method="POST">
                <label>Rotate by:
                    <input name="rot" type="text" value="0"/>
                </label>
                <textarea name='text'>{0}</textarea>
                <input type="submit" value="Submit" />
            </form> 
        </body>
    </html>
"""
@app.route('/')
def index():
    return form.format('')

@app.route('/', methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    new_str = rotate_string(text, rot)
    return form.format(new_str)

app.run()
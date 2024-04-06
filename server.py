from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_info = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    return render_template("html_table.html", user_info = user_info)

@app.route('/success')
def success():
    return "Success"

@app.route('/lists')
def render_lists():
 
    
    return render_template("list.html")
if __name__ == "__main__":
    app.run(debug=True, port = 5001)

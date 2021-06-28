from db_config import table
from flask import Flask, render_template, request
from app import app

table_data = table

@app.route('/', methods=['POST', 'GET'])
def table():
    return render_template('table.html', table_data = table_data)



if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port='1300',
        debug=True,
        threaded=True
    )

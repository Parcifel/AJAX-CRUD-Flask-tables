from itertools import filterfalse
from db_config import table
from flask import Flask, render_template, request, redirect
from app import app

table_data = table

@app.route('/', methods=['POST', 'GET'])
def table():
    return render_template('table.html', table_data = table_data)


@app.route('/saveData', methods=['POST', 'GET'])
def saveData():
    if request.method == 'POST':
        isDataSame = False 

        data = request.form.get('data')
        idName = request.form.get('id')

        for i in range( len(idName) ):
            try: 
                int(idName[i])
                break
            except:
                nothing = None

        columnName = idName[:i]
        rowNum = int(idName[i:])

        for row in table_data:
            if row[columnName] == data:
                isDataSame = True

        if isDataSame == False:
            print(data)
            print('columnt: ' + columnName)
            print('row: ' + str(rowNum))
            return('new value: ' + data)
        elif isDataSame == True:
            print('value did not change')
            print('columnt: ' + columnName)
            print('row: ' + str(rowNum))
            return('value did not change')

        return('dataSaved: ' + data)
    return redirect('/')



if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port='1300',
        debug=True,
        threaded=True
    )

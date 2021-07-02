from itertools import filterfalse
from db_config import table
from flask import Flask, render_template, request, redirect
from app import app

table_data = table

# Default route
@app.route('/', methods=['POST', 'GET'])
def table():
    return render_template('table.html', table_data = table_data)


# Save Data route to catch AJAX
@app.route('/saveData', methods=['POST', 'GET'])
def saveData():
    # Only if request is POST
    if request.method == 'POST':
        isDataSame = False 

        # Get variables send by AJAX
        data = request.form.get('data')
        idName = request.form.get('id')

        # Devide element id into column name and row number
        for i in range( len(idName) ):
            try: 
                int(idName[i])
                break
            except:
                nothing = None # Just something to fill the except condition, this is useless, but needed

        # Create variables for column name and row number
        columnName = idName[:i]
        rowNum = int(idName[i:])

        # Verify that value has changed, dont want to send unnecessary queries to database
        for row in table_data:
            if row[columnName] == data:
                isDataSame = True

        # Just some console feedbacks as no actual database is connected
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

    # If request is not POST redirect to '/'
    return redirect('/')



if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port='1300',
        debug=True,
        threaded=True
    )

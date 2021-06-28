from app import app
# from flaskext.mysql import MySQL
# import pymysql


# Connecting to MySQL database
'''
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'username'      # Default: None 
app.config['MYSQL_DATABASE_PORT'] = '3306'          # Default: 3306
app.config['MYSQL_DATABASE_HOST'] = 'localhost'     # Default: Localhost
app.config['MYSQL_DATABASE_PASSWORD'] = 'p455w0rd'  # Default: None
app.config['MYSQL_DATABASE_DB'] = 'text_db'         # Default: None
app.config['MYSQL_DATABASE_CHARSET'] = 'utf-8'      # Default: 'utf-8'


SELECT * FROM test
+------+------------+-----------+-------------+
| id   | first_name | last_name | city        |
+------+------------+-----------+-------------+
|    1 | Tony       | Stark     | New York    |
|    2 | Peter      | Parker    | Queens      |
|    3 | Bruce      | Banner    | Washington  |
|    4 | Steve      | Rogers    | Brooklyn    |
|    5 | Stephen    | Strange   | New York    |
+------+------------+-----------+-------------+

# Connect to MySQL Database 
conn = mysql.connect()
mycursor = conn.cursor(pymysql.cursor.DictCursor)

sqlQuery = ('SELECT * FROM test')
mycursor.execute( sqlQuery )

table = mycursor.fetchall()
'''


# when getting data from MySQL ... fetchall()
#  data will be returned in a list of dictionaries
#  The list is the table, and dictionaries the rows in the table
table = [

    # 1
    {
        'id': 1,
        'first_name': 'Tony',
        'last_name': 'Stark',
        'city': 'New York'
    },

    # 2 
    {
        'id': 2,
        'first_name': 'Peter',
        'last_name': 'Parker',
        'city': 'Queens'
    },

    # 3
    {
        'id': 3,
        'first_name': 'Bruce',
        'last_name': 'Banner',
        'city': 'Washington'
    },

    # 4
    {
        'id': 4,
        'first_name': 'Steve',
        'last_name': 'Rogers',
        'city': 'Brooklyn'
    },

    # 5
    {
        'id': 5,
        'first_name': 'Stephen',
        'last_name': 'Strange',
        'city': 'New York'
    }
]
# AJAX-CRUD-Flask-tables
============================================================================

This app is a prototype for loading database tables from mySQL , and
displaying them in an web page through Flask and constructing the table with 
Jinja.
The web table has in-place-edits with AJAX to send the item to the Flask
server for processing and updating the mySQL database.

============================================================================

## in-place-edit:

In place edit refer to editing some data in the place it is, without another
page/ form being needed.
In this example it has been done, so you can click on a cell of a table, and 
edit the data of that cell, save it and it being saved to a database without 
the page being reloaded.

============================================================================

## Files:

```
.
├── app
│   ├── static
│   │   └── edits.js
│   │
│   ├── templates
│   │   └── table.html
│   │
│   ├── app.py
│   ├── main.py
│   └── db_config.py
│
├── README.md
└── requirements.txt
```

============================================================================
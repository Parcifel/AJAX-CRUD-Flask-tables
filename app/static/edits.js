console.log('edit_table.js started successfully');

class in_place_edits{
    // Get the tbody of the table inputted
    constructor(table){ 
        this.tbody = table.querySelector('tbody');
    }
    

    init() {
        this.tds = this.tbody.querySelectorAll('td'); // Create nodelist of all <td> elsements in the tbody ... note <th> (table header) will not be chosen
        // Loop through each <td> in tds
        this.tds.forEach(td => {
            td.setAttribute('contenteditable', true); // Make each cell editable

            // Adds click event on each cell
            td.addEventListener('click', (ev) => {
                // Only adds event if cell is not already in editing mode
                if(!this.inEditing(td)) { 
                    this.startEditing(td);
                };
            });
        });
    }

    // When cell is clicked on
    startEditing(td) {

        // Find any other cells that are already in-editing mode
        const activeTD = this.findEditing();
        if(activeTD) {
            this.cancelEditing(activeTD); // If an cell is already in-editing mode it cancels the editing mode
        };


        td.classList.add('in-editing'); // Adds 'in-editing' to className as cell is being edited 
        td.setAttribute('data-old-value', td.innerHTML); // Creates new attribute, to hold old value, for use when process is canceled
        this.createButtonToolbaar(td); // Created <div> with button toolbar
    }

    // Cancel process, reverts cell to previous state
    cancelEditing(td) {
        // Resets the data in the cell to the original
        //   Assumes you wanted to cancel the operation
        td.innerHTML = td.getAttribute('data-old-value');

        // Removes 'in-editing' from className as cell is no linger being edited
        td.classList.remove('in-editing');
    }

    // Saves data
    finishEditing(td) {
        // Reverts cell back with new data
        td.classList.remove('in-editing');
        this.removeToolbar(td);

        // Sends data to flask server
        var data = td.textContent;
        this.sendData(td, data);
    }

    // Find the element that contains 'in-editing' as a className
    inEditing(td) {
        return td.classList.contains('in-editing')
    }

    // Created <div> with toolbar
    createButtonToolbaar(td) {
        // Save button
        const saveBtn = document.createElement('button'); // Created element: for save button
        saveBtn.className = 'saveBtn'; // Sets the className of saveBtn
        saveBtn.textContent = 'Save'; // Text of btn

        // Cancel Button
        const cancelBtn = document.createElement('button'); // Created element: for cancel button
        cancelBtn.className = 'cancelBtn'; // Sets the className of cancelBtn
        cancelBtn.textContent = 'Cancel'; // Text of btn

        // Div to hold buttons
        const divBtn = document.createElement('div'); // Created element: for div to contain buttons
        divBtn.className = 'button-wrapper'; // Sets the className of div => button-wrapper

        // Div toolbar
        const toolbar = document.createElement('div'); // Created element: for the whole toolbar
        toolbar.className = 'button-toolbar'; // Sets the className of div => button-toolbar 
        toolbar.setAttribute('contenteditable', false); // So no content in the toolbar can be edited


        // Append buttons to div in order displayed (left to right)
        divBtn.appendChild(cancelBtn);
        divBtn.appendChild(saveBtn);

        // Append button-wrapper to button-toolbar
        toolbar.appendChild(divBtn);

        // Append button-toolbar to the cell
        td.appendChild(toolbar);

        // Selects the specific 2 buttons that were appended ... NOTE: not the elements created!! (saveBtn, cancelBtn)
        const btnSave = toolbar.querySelector('.saveBtn'); 
        const btnCancel = toolbar.querySelector('.cancelBtn');

        // Adds clock event to button
        btnSave.addEventListener('click', (ev) => {
            ev.stopPropagation(); // Does not trigget the click event of cell, only that of the button
            this.finishEditing(td); // Save teh edited data
        });

        btnCancel.addEventListener('click', (ev) => {
            ev.stopPropagation(); // DOes not trigger the click event of cell, only that of the button
            this.cancelEditing(td); // Converts cell back to previous state
        });
    }

    // Removes toolbar from cell
    removeToolbar(td) {
        const toolbar = td.querySelector('.button-toolbar'); // Gets toolbar <div>
        toolbar.remove(); // Removes it from cell
    }

    // Find element that is in editing mode
    findEditing() {
        // find()
        //     find element in array this.tds that sattisfies the function
        // call()
        //     calls the function with a this value
        return Array.prototype.find.call(this.tds, td => this.inEditing(td));
    }

    // With AJAX, send data to Flask server
    sendData(td, newData) { 
        // Creates XHR object
        var xhr = new XMLHttpRequest();

        // When finif=shed, just console.log response
        xhr.onload = function() {
            console.log(xhr.responseText);
        }


        xhr.open('POST', '/saveData', true); // Activates //SaveData route and saveData() function 
        xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded'); // Set request header
        xhr.send(`data=${newData}&id=${td.id}`); // 2 Variables passed with AJAX

    }
}


const tableElement = document.querySelector('table'); // Get the table as a variable
const editing = new in_place_edits(tableElement); // Connect table to class
editing.init(); // trigger init() function on class in_place_edits
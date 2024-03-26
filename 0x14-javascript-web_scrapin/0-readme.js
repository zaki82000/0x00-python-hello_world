#!/usr/bin/node

const fs = require('fs');

// Function to read and print file content
function printFileContent(filePath) {
    // Read file asynchronously
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            // Check if the error is due to file not found
            if (err.code === 'ENOENT') {
                console.error("{ Error: ENOENT: no such file or directory, open 'doesntexist'\n at Error (native) errno: -2,\n code: 'ENOENT',\n syscall: 'open', \n path: 'doesntexist'}");
            } else {
                // Print other errors
                console.error('Error reading the file:', err);
            }
        } else {
            // Print file content if read successfully
            console.log(data);
        }
    });
}

// Check if a file path is provided as an argument
if (process.argv.length < 3) {
    console.error('Please provide the file path as an argument.');
} else {
    // Get the file path from the command line arguments
    const filePath = process.argv[2];
    // Call the function to print file content
    printFileContent(filePath);
}

1)Password Manager
A simple desktop password manager built with Python and Tkinter.
This application allows you to generate, store, and search passwords for different websites using a graphical interface.

2)Features
Generate secure random passwords
Save website, email/username, and password
Search saved credentials by website name
Data stored locally in a JSON file
Uses environment variables for configuration:
    PATH=password_file.json #the name of the data file
    MAIL=mail   #determine the name of the key where mail is saved in your json
    PASSWORD=password #determine the name of key wher the password is saved in your json


3)How it works
Passwords are stored in a local JSON file.
The app can generate a random password.
You can search for saved credentials by entering the website name.

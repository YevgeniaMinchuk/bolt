# Retrieval-Based Chatbot
This project is a simple retrieval-based chatbot application built using Python, Flask, HTML, CSS, and a JSON file for knowledge storage. 
The chatbot can answer questions based on the provided knowledge and can learn new responses through user interactions.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Structure](#structure)
- [Technologies Used](#technologies-used)
- [Contact](#contact)

## Features
- User Interaction: Users can ask questions and get answers based on the knowledge base
- Knowledge Expansion: Users can teach the chatbot new responses if it doesn't know an answer
- Simple Web Interface: The application has a user-friendly interface built with HTML and CSS
- JSON Knowledge Base: The chatbot uses a JSON file to store questions and answers

## Getting Started
### Prerequisites
Install the following applications:
- Python (version 3.x)
- Visual Studio Code (VS Code) or another coding platform

## Installation
Follow these steps to set up the project in VS Code or another coding platform:
1. **Clone the repository**

  git clone https://github.com/yourusername/chatbot.git
  
  cd chatbot
  
  Alternatively, download the code as a ZIP file and open it in Visual Studio Code (VS Code)
  
2. **Set Up Environment in VS Code**
- Open the project folder in VS Code.
- Open the Command Palette (View > Command Palette or Ctrl+Shift+P).
- Select the Python: Create Environment command to create a virtual environment in your workspace. Choose venv and the Python environment you want to use. Select the "requirements.txt" file as a dependency.
- After creating the virtual environment, run Terminal: Create New Terminal (Ctrl+Shift+ ``) from the Command Palette, which creates a terminal and automatically activates the virtual environment.
  
3. **Activate the Virtual Environment**
  py -3 -m venv venv

  venv\Scripts\activate   # On Windows

  source venv/bin/activate # On macOS/Linux
  
4. **Install Required Packages**
  pip install flask
5. **Set the FLASK_APP Environment Variable**
  Make sure that you are in the Bolt directory (cd Bolt)

  set FLASK_APP=algo.py   # On Windows

  export FLASK_APP=algo.py # On macOS/Linux
  
6. **Run the Flask Application**
  flask run

7. **Access the Application**
Left-click on the address shown in the terminal (usually http://127.0.0.1:5000/) to open the application in your web browser.

## Structure
- algo.py: The main Flask application script.
- templates/: Directory containing the HTML templates for the web interface.
- static/: Directory containing CSS and other static files.
- knowledge.json: JSON file containing the knowledge base (questions and answers).

## Technologies Used
- Flask: Web framework used for the project
- Python
- HTML
- CSS
- JSON

## Contact
Yevgenia Minchuk - minchuky@msu.edu

See my portfolio - https://portfolio-yevgeniaminchuk.netlify.app

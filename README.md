#Project Name
web application for sharing FRC team info

##Getting Started
These instructions will get your project up and running on your Windows machine for development and testing purposes.

###Prerequisites
Python 3.8 or higher
pip (Comes installed with Python if you select the option during Python installation)
###Installing
Follow these steps to set up your development environment:

###Clone the Repository
Clone the project repository to your local machine using Git Bash or Command Prompt:

bash
Copy code
git clone https://yourprojectrepository.com/project.git
cd project
Set up a Python Virtual Environment
Using the Command Prompt, navigate to your project directory and create a virtual environment. This isolates your project dependencies:

Copy code
python -m venv myenv
Activate the Virtual Environment
Activate the virtual environment by running:

Copy code
myenv\Scripts\activate
Your command prompt should now show the name of your virtual environment, indicating that it is active.

Install Project Dependencies
With the virtual environment activated, use pip to install the project dependencies:

Copy code
pip install -r requirements.txt
This will install Django and any other dependencies defined in your requirements.txt file.

Run the Development Server
Once all dependencies are installed, you can start the Django development server:

Copy code
python manage.py runserver
You can now access the application at http://127.0.0.1:8000/ in your web browser.

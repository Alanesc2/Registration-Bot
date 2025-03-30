# ASU Registration-Bot
Automated bot for ASU's course registration portal

##About
Registering for the next semester's courses is essential, as one of the main priorities is getting a flexible schedule and academic requirements. However, due to lack of reminders and enroll opening during the peak of a semester, students often forget to enroll or fail to enroll with time (regardless if off by seconds). Most of the class registrations occur at 6 AM, an inconvenient time for many students. This leads to students forced to take classes outsie of their schedule or not be able to enroll in a required class. Due to my personal struggle and my peers' continuous struggles with enrolling, I became driven to learn webscraping/automation using Python.

##Program
First, it will check to see if the necessary Chrome driver for Selenium is within the directory. If undefined, it will grab the driver from their repositories.

The user will be asked to provide:
- Username
- Password
- Registration Time
- Semester to enroll in

From here, the script will use Selelium and Time libraries to enroll in the classes already in the shopping cart immediately once registration time comes. 

By using the registration time, the script will not commence 5 minutes before the registration time, however, it will run from when you start the program until then (Do not run it more than a day before registration)

##Instructions
1. Make sure you have selected the classes you want to enroll in, and double check they are actually in the cart in the registration portal.
2. For this programm, Google Chrome browser is needed. If not installed, make sure to install before running. If installed, make sure it is updated accordingly.
3. To use this program, open up a terminal and type: <br> 'git clone https://github.com/Alanesc2/Registration-Bot.git' </br>
(Make sure to have git downloaded before cloning or download ZIP folder)
4. In a terminal, navigate to directory and type: pip install -r requirements.txt
5. Run code by typing: python/python3 enroll.py
6. Make sure you have inputted the correct information, and you should be ready to enroll in your ideal schedule.

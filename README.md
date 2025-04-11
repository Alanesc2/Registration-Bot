# University Registration Bot

Automated bot for ASU's course registration portal.

## About
Registering for next semester's courses is crucial to securing a flexible schedule and fulfilling academic requirements. However, many students forget to enroll on time due to a lack of reminders or the inconvenient early morning registration times (often at **6 AM**). Missing registration by even a few seconds can force students into less desirable class times or prevent them from enrolling in required courses.

This bot was developed to automate the registration process, inspired by my own struggles and those of my peers. It utilizes **Python, Selenium, and Web Scraping** to enroll in classes instantly when registration opens.

## How It Works
1. Checks for the necessary **Chrome driver** for Selenium. If not found, it downloads the correct version automatically.
2. Prompts the user for:
   - ASU **Username**
   - ASU **Password**
   - **Registration Time**
   - **Semester** to enroll in
3. Waits until **5 minutes before** the registration time and then actively monitors until the exact moment to register.
4. Automatically logs in and submits the enrollment request for the classes **already in your shopping cart**.

## Prerequisites
- **Google Chrome** (must be installed and up-to-date)
- **Python** (3.7 or later)
- **Git** (for cloning the repository)

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Alanesc2/Registration-Bot.git
cd Registration-Bot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Program
```bash
python enroll.py  # Use 'python3' if needed
```

## Important Notes
- **Before running the bot, ensure that your desired classes are already in the shopping cart** on the ASU registration portal.
- The program will wait until 5 minutes before your specified registration time to begin the automation process.
- **DUO Authentication is still required** if prompted
- Do **not** run the bot more than **a day before** registration.

## Troubleshooting
- If the bot is not working correctly, ensure that:
  - Google Chrome is installed and up to date.
  - All required Python packages are installed (`pip install -r requirements.txt`).
  - You have entered the correct login credentials and registration time.

## Disclaimer
This bot is intended for **personal use only**. Use responsibly and ensure compliance with ASU's registration policies.

---

### Future Improvements
- **Error Handling Enhancements**: Improve handling of website structure changes.
- **Virtual Environment**: Allow users to schedule enrollment in more than one day advance without having to run program locally.
- **Autonomous Authentication**: Allow bot to be fully automated without requiring authentication from user.
- **GUI Interface**: Create a user-friendly graphical interface for ease of use.

---

Developed by **Alan Escudero**

---

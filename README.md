# BTES - Booking Tickets Events System

BTES (Booking Tickets Events System) is a web-based application designed to allow users to easily view, search, and book tickets for various events. It provides a user-friendly interface for managing event bookings and includes features like refunds, payment processing, and admin event management.

## Prerequisites

Before you begin, make sure you have the following software installed:

- **Python 3.12.0**: get last version by `python.exe -m pip install --upgrade pip`
- **Django**: `pip install django`
- **JavaScript**:already exists in browsers, for some dynamic in page
- **HTML and CSS**:already supported in browsers, for graphic user interface

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mmsbah191/BTES.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd BTES
   ```
3. **Activate the virtual environment**:

   - **On Windows powershell**:
     ```bash
     venv\Scripts\activate
     ```
   - **On macOS and Linux**:
     ```bash
     source venv/bin/activate
     ```

5. **Install the required Python packages**:
   ```bash
   pip install django
   or
   pip install -r requirements.txt
   ```

## Usage & run in browser

1. **Navigate to the project directory**:
   ```bash
   cd BTES
   ```

2. **Run the Django development server**:
   from btes directory
   ```bash
   python manage.py runserver
   ```
3. Open a web browser and go to:
   ```
   http://127.0.0.1:8000
   ```
   This will open the application on your local web server.

## Features

- User registration and login
- Event search and filtering
- Ticket booking with integrated payment systems
- Refund processing (within 24 hours for logged-in users)
- Admin panel for managing events and viewing summaries
Here's a more detailed guide for the **Contributing** section, explaining step-by-step how to use Git and GitHub for collaboration:

## Contributing

Follow these steps to contribute to the project:

### 1. Fork the Repository
- First, click on **Fork** in the top-right corner to create a copy of the repository under your GitHub account.
  
### 2. Clone the Repository
- Clone your forked repository to your local machine by running the following command:
  ```bash
  git clone https://github.com/mmsbah191/BTES.git
  ```
### 3. Navigate to the Project Directory
- Move into the project directory:
  ```bash
  cd path/Btes
  ```

### 4. Set Upstream to Original Repository
- To keep your forked repository in sync with the original, add the original repository as the upstream remote:
  ```bash
  git remote add upstream https://github.com/mmsbah191/BTES.git
  ```

### 5. Create a New Branch
- Create a new branch to work on a specific feature or fix:
  ```bash
  git checkout -b feature/YourFeatureName
  ```

### 6. Start Coding
- Make changes or add new code. As you work, you can check the status of modified files using:
  ```bash
  git status
  ```

### 7. Stage and Commit Changes
- Once you’re ready to save your changes, stage the files you want to commit:
  ```bash
  git add .
  ```
- Commit your changes with a descriptive message:
  ```bash
  git commit -m "Add a description of what you did"
  ```

### 8. Push Changes to Your Branch
- Push your changes to the branch on your forked GitHub repository:
  ```bash
  git push origin feature/YourFeatureName
  ```

### 9. Pull Updates from the Original Repository (Upstream)
- Before submitting a pull request, make sure your branch is up-to-date with the original repository by fetching and merging any changes:
  ```bash
  git fetch upstream
  git checkout main
  git merge upstream/main
  ```
- Then, rebase your feature branch on the updated `main` branch to avoid conflicts:
  ```bash
  git checkout feature/YourFeatureName
  git rebase main
  ```

### 10. Submit a Pull Request
- After pushing all your changes, go to your forked repository on GitHub, and you’ll see an option to submit a pull request (PR). Follow the prompts to create the PR to the original repository’s main branch.

## Contributors

- **Mohamed Mesbah Ibrahim**  
- **Mai Mokhtar Al-Galayi**

## Acknowledgments

Special thanks to Dr. Ali AbuRas for his guidance and support in CS315.

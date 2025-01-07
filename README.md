# Password Tool
A Python-based tool for evaluating password strength and generating secure, random passwords.

# Features
- **Passowrd Strength Checker**:
  - Determines the strength of a given password using the 'zxcvn' Python library.
  - Provides feedback (if applicable) to improve weak passwords.
  - Warns against common vulnerabilities and patterns in passwords.
- **Secure Password Generator**:
  - Creates a 20-character password using uppercase, lowercase, numbers, and special characters.
  - Ensures the password is secure using the 'secrets' module

# Setup Instructions & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/b-getz/PasswordTool.git
2. Navigate to the project folder:
   ```bash
   cd PasswordTool
3. Create a virtual environment:
   ```bash
   python -m venv venv
4. Activate the virtual environment:
   - On Windows:
   ```bash
   ven\Scripts\activate
  - On macOS/Linux:
    ```bash
    source venv/bin/activate
5. Install dependencies:
   ```bash
   pip install zxcvbn
3. Run the program:
   ```bash
   python password_tool.py


# 🎓 Grade Calculator

A simple, modern, and interactive **Grade Calculator web application** built using **Python and Streamlit**.

The application allows users to enter a mark between **0 and 100** and instantly calculates the corresponding **letter grade**, along with a performance message.

---

## ✨ Features

- 🎓 Clean and modern user interface
- 📊 Accepts marks from **0 to 100**
- ⚡ Instantly calculates the letter grade
- 📈 Dynamic progress bar showing the entered mark
- 🏆 Displays the calculated result clearly
- 💬 Provides grade-specific performance messages
- 🎨 Different colors for different grades
- 📋 Displays the complete grading scale
- 🔄 Result remains visible after Streamlit reruns using session state
- 📱 Responsive Streamlit layout
- 💻 Beginner-friendly Python project

---

## 📊 Grading System

| Mark Range | Grade | Performance |
|------------|-------|-------------|
| 90 – 100 | **A** | Excellent performance 🎉 |
| 80 – 89 | **B** | Great job! 👏 |
| 70 – 79 | **C** | Good effort! 💪 |
| 60 – 69 | **D** | Passed – keep working hard 📚 |
| Below 60 | **E** | Keep learning and try again 🌟 |

---

## 🖥️ Application Preview

The application provides:

1. A mark input field
2. A progress indicator
3. A **Calculate Grade** button
4. A result section showing:
   - Mark
   - Letter grade
   - Performance message
5. A grading scale section

---

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **HTML**
- **CSS**

### Python Libraries

```text
streamlit
```

---

## 📁 Project Structure

```text
Grade-Calculator/
│
├── Grade_Calculator.py
├── README.md
├── requirements.txt
└── .gitignore
```

> Replace `Grade_Calculator.py` with your actual Python filename if it is different.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Grade-Calculator.git
```

Navigate into the project directory:

```bash
cd Grade-Calculator
```

---

### 2. Create a Virtual Environment

It is recommended to use a virtual environment for the project.

```bash
python -m venv venv
```

Activate the virtual environment on Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, you can use Command Prompt instead:

```cmd
venv\Scripts\activate
```

---

### 3. Install Dependencies

Install Streamlit using:

```bash
pip install streamlit
```

Or, if a `requirements.txt` file is included:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application with:

```bash
streamlit run Grade_Calculator.py
```

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open the URL in your browser to use the application.

---

## 🧮 How It Works

The application uses conditional statements to determine the appropriate grade based on the entered mark.

The basic logic is:

```python
if mark >= 90:
    grade = "A"
elif mark >= 80:
    grade = "B"
elif mark >= 70:
    grade = "C"
elif mark >= 60:
    grade = "D"
else:
    grade = "E"
```

The calculated grade and result information are stored using **Streamlit Session State**, allowing the result to remain visible during application reruns.

---

## 🎨 User Interface

The application includes custom CSS to provide:

- Gradient background
- Centered application layout
- Modern cards and containers
- Styled buttons
- Grade-specific colors
- Large grade display
- Responsive spacing and typography

---

## 🚀 Future Improvements

Some possible improvements for future versions include:

- 👤 Add student name input
- 📚 Support multiple subjects
- 🧮 Calculate total and average marks
- 📊 Display performance charts
- 🏅 Add GPA calculation
- 💾 Export results as PDF
- 📄 Generate student report cards
- 🌙 Add dark mode
- 📱 Improve mobile-specific styling

---

## 🎯 Learning Objectives

This project demonstrates the basics of:

- Python conditional statements
- Streamlit application development
- Streamlit widgets
- Session state management
- Custom CSS styling
- User input validation
- Building interactive web applications with Python

---

## 📦 Requirements

Create a `requirements.txt` file containing:

```text
streamlit
```

Then install the dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🔐 .gitignore

If you are using a virtual environment, add the following to `.gitignore`:

```text
venv/
__pycache__/
*.pyc
.env
```

---

## 🤝 Contributing

Contributions are welcome!

If you would like to improve this project:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/improvement
```

3. Make your changes
4. Commit your changes

```bash
git add .
git commit -m "Improve grade calculator"
```

5. Push the branch

```bash
git push origin feature/improvement
```

6. Open a Pull Request

---

## 📄 License

This project is open-source and available for educational and personal use.

---

## 👨‍💻 Author

**Jaya Praveen K**

Built with ❤️ using **Python & Streamlit**.

---

⭐ If you found this project useful, consider giving the repository a **star**!
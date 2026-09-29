# Morse Code Converter 📡

A simple, interactive command-line application written in Python to convert plain text into Morse code and translate Morse code back into readable text.

---

## 📋 Features

- **Text to Morse Code**: Encodes alphanumeric characters (A–Z, 0–9) into standard Morse code.
- **Morse Code to Text**: Decodes space-separated Morse code back into plain text.
- **Interactive CLI Menu**: An easy-to-use menu system running in a loop.
- **Case-Insensitive**: Works seamlessly regardless of input casing.

---

## 🛠️ Prerequisites & Installation

Follow these steps to set up the necessary tools before running the project.

### 1. Install Git & Python (with `pip`)

#### 🪟 Windows
1. **Python & pip**:
   - Download the Python installer from [python.org](https://www.python.org/downloads/).
   - **Important**: Make sure to check the box **"Add python.exe to PATH"** during installation.
   - `pip` comes bundled automatically with standard Python installations.
2. **Git**:
   - Download and run the Git for Windows installer from [git-scm.com](https://git-scm.com/download/win).

#### 🍎 macOS
Open Terminal and install via Homebrew:
```bash
# Install Homebrew if you don't have it (https://brew.sh)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python and Git
brew install python git
```

#### 🐧 Linux (Ubuntu / Debian)
Open your terminal and run:
```bash
sudo apt update
sudo apt install python3 python3-pip git -y
```

---

## 🚀 Getting Started

### 1. Clone the Repository
Clone this project directly to your local machine(command prompt):
open command prompt and type

```bash
git clone https://github.com/surjithh26bhi10007-droid/vityarthi-project.git
cd vityarthi-project
```

### 2. Run the Converter
Launch the application using Python:

```bash
python "morse code conventer.py"
```
*(On macOS/Linux, use `python3 "morse code conventer.py"`)*

---

## 🎮 How to Use

When you run the script, an interactive menu will display:

```text
==============================|
      MORSE CODE CONVERTER    |
==============================|
1. Text to Morse Code         |
2. Morse Code to Text         |
3. Exit                       |
==============================|
```

1. **Option 1 (Text to Morse)**: Enter any sentence (e.g., `HELLO WORLD`) to get `.... . .-.. .-.. ---   .-- --- .-. .-.. -..`.
2. **Option 2 (Morse to Text)**: Enter Morse code separated by spaces for letters and double spaces for words.
3. **Option 3**: Exit the program.

---

 Project Statement: Morse Code Converter

 1. Problem Statement
Morse code remains a foundational encoding scheme historically used in telecommunications, aviation, maritime communication, and assistive technologies. However, encoding plain text into Morse code manually or decoding raw Morse signals back into human readable text is time consuming and prone to human error, especially for untrained individuals. There is a need for an efficient, lightweight, and accessible software utility that can instantly bidirectionally convert text and Morse code through an intuitive user interface.

 2. Scope of the Project
The scope of this project includes:
- **Bidirectional Conversion**: Providing instant translation from standard alphanumeric text to Morse code and vice-versa.
- **Support for Alphanumeric Characters**: Full coverage of English letters (A–Z) and numeric digits (0–9).
- **Console Interface**: Delivering an interactive, lightweight Command Line Interface (CLI) that requires minimal computing resources.
- **Error Handling**: Managing invalid user menu selections and gracefully handling unknown inputs during translation.

 Out of Scope:
- Support for complex special punctuation, accented characters, or non-Latin alphabets.
- Audio signal playback (beeps/tones) or visual light flashes for Morse signals.
- Graphical User Interface (GUI) or web application interface.

 3. Target Users
- **Students & Educators**: Learning or teaching basic computer science concepts, mapping/dictionary data structures, string manipulation, or communication protocols.
- **Amateur Radio (Ham Radio) Operators**: Enthusiasts looking for a quick tool to reference or double-check Morse code messages.
- **Hobbyists & Puzzle Enthusiasts**: Individuals interested in cryptography, classical ciphers, or retro communication techniques.
- **Developers**: Programmers looking for a clean reference implementation of bidirectional dictionary mapping in Python.

 4. High-Level Features
1. **Text-to-Morse Code Encoding**:
   - Converts standard text strings into standard dot-and-dash Morse representation.
   - Automatically handles whitespace between words and converts inputs to uppercase for consistent mapping.
2. **Morse Code-to-Text Decoding**:
   - Parses space-delimited Morse signals back into standard English letters and numbers.
   - Preserves word separation using double-space conventions.
3. **Interactive Menu Loop**:
   - User-friendly CLI menu allowing continuous operations without restarting the script.
   - Exit prompt and graceful session termination.
4. **Fast and Lightweight Processing**:
   - Pure Python implementation with zero external dependencies, running efficiently on any platform with Python installed.

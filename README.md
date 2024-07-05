# Multilingual Voice Transcriptions

This project is a Streamlit web application that uses OpenAI's Whisper model to transcribe multilingual audio files into English. The application also provides features for storing and displaying transcription history, calculating word frequencies, and identifying unique phrases.

## Features

- **Multilingual Transcription:** Transcribe audio files in various languages into English.
- **Word Frequency Analysis:** Calculate and display the most frequently used words in the current user's transcriptions and compare them against global frequencies.
- **Unique Phrase Identification:** Identify and display the top 3 unique phrases spoken by the user.
- **Transcription History:** Store and display the history of transcriptions for the user.

## Installation
refer requirements.txt file

### Prerequisites

**Install Python**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/).

### Prerequisites

1. **Install Python**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/).


1. **Clone the Repository**:

    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2. **Set Up Virtual Environment**:

    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For MacOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Python Packages**:

    ```bash
    pip install -r requirements.txt
    ```

Usage:

1. Run the Streamlit application
    streamlit run voice_analyzer.py

2. Open your web browser and navigate to http://localhost:8501.

3. Upload an audio file (supported formats: .wav, .mp3, .m4a, .ogg).

4. Click the "Transcribe Audio" button to start the transcription process.

5. View the transcription, word frequency comparison, and top unique phrases in the web interface.

Database Setup:
The application uses SQLite to store transcription history. The database is automatically set up and configured when the application runs for the first time.

Code Overview
1. Main Application (voice_analyzer.py)
2. Uploads and saves the audio file.
3. Loads the Whisper model.
4. Transcribes the audio file into English.
5. Saves the transcription to the database.
6. Displays the transcription, word frequency comparison, and top unique phrases.

Database Functions (database.py)
* save_transcription(text): Saves a new transcription to the SQLite database.
* get_transcription_history(): Retrieves transcription history from the SQLite database.

Helper Functions
1. calculate_word_frequency(text): Calculates the frequency of words in a given text.
2. extract_top_unique_phrases(text, top_n=3): Extracts and returns the top N unique phrases from a given text.
3. calculate_global_word_frequency(): Calculates the global word frequency from all transcriptions in the database.
4. display_comparison_table(user_text): Displays a comparison table of word frequencies between the current user's text and global text.



Acknowledgements
* Streamlit
* OpenAI Whisper
* FFmpeg



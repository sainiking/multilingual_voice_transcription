import streamlit as st
import whisper
import tempfile
from database import save_transcription, get_transcription_history
from collections import Counter
import re
import pandas as pd

st.title("Multilingual Voice Transcriptions!")

st.text("Whisper Model Loaded, Select an audio file to transcribe.")
# upload audio file with streamlit
audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a", "ogg"])

model = whisper.load_model("base")



if st.sidebar.button("Transcribe Audio"):
    # calculate_word_frequency function here.
    def calculate_word_frequency(text):
        words = re.findall(r'\w+', text.lower())
        return Counter(words)


    # Function to extract and count phrases
    def extract_top_unique_phrases(text, top_n=3):
        # Simple phrase extraction based on punctuation
        phrases = re.split(r'[.!?]', text)
        # Removing empty strings and stripping whitespace
        phrases = [phrase.strip() for phrase in phrases if phrase]
        phrase_count = Counter(phrases)
        # Filtering out phrases that occur more than once
        unique_phrases = [phrase for phrase, count in phrase_count.items() if count == 1]
        # Sorting unique phrases by length (longest first) as a proxy for uniqueness
        unique_phrases_sorted = sorted(unique_phrases, key=len, reverse=True)
        # Returning the top N unique phrases
        return unique_phrases_sorted[:top_n]


    #calculate_global_word_frequency function here.
    def calculate_global_word_frequency():
        transcriptions = get_transcription_history()
        all_text = " ".join([transcription.text for transcription in transcriptions])
        return calculate_word_frequency(all_text)
    
    # display_comparison_table function here.
    def display_comparison_table(user_text):
        user_freq = calculate_word_frequency(user_text)
        global_freq = calculate_global_word_frequency()
        
        # Create a DataFrame for comparison.
        df = pd.DataFrame(list(user_freq.items()), columns=['Word', 'User Frequency'])
        df['Global Frequency'] = df['Word'].apply(lambda x: global_freq.get(x, 0))
        
        st.header("Comparison Table:")
        st.table(df)
    
    
    if audio_file is not None:
        # save the audio file to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.' + audio_file.name.split('.')[-1]) as tmp_file, open(tmp_file.name, 'wb') as tmp_file:
            tmp_file.write(audio_file.getvalue())
            tmp_path = tmp_file.name

        st.sidebar.success("Transcribing Audio")
        
        # Transcribe the audio file with transcribe to English only.
        transcription = model.transcribe(tmp_path, task="translate")
        save_transcription(transcription["text"])
        st.sidebar.success("Transcription Complete")
        
        # Display the transcription
        st.header("Transcription Result:")
        st.markdown(transcription["text"])
        
        # Call to display the comparison table
        display_comparison_table(transcription["text"])
        
        # Extract and display top 3 unique phrases
        top_phrases = extract_top_unique_phrases(transcription["text"])
        st.header("Top 3 Unique Phrases:")
        st.write(top_phrases)
    else:
        st.sidebar.error("Please upload an audio file.")

else:
    st.info("After uploading the file, hit the 'Transcribe Audio' to the left.")
    st.info("The transcription will be displayed below.")

st.sidebar.header("Play original audio file.")
st.sidebar.audio(audio_file)

# Display transcription history
st.sidebar.header("Transcription History")
for transcription in get_transcription_history():
    st.sidebar.text(f"{transcription.created_at}: {transcription.text}")

import streamlit as st
from groq import Groq
import os
import re

# Get API key from Streamlit Secrets
api_key = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=api_key)

# Title and intro
st.title("🌦️ Emotional Weather Forecast")
st.write("Describe your feelings and receive a soulful weather forecast, mood score, advice, and music 🎶")

# Journal input
user_input = st.text_area("📝 How are you feeling today?", height=200)

def get_emotional_forecast(journal_entry):
    prompt = f"""
You are an emotionally intelligent assistant. The user just wrote this journal entry:

"{journal_entry}"

Based on this, give:
1. An emotional weather forecast using poetic metaphors.
2. A mood rating out of 10 (just the number).
3. A soulful one-line piece of advice.

Keep the forecast creative and under 80 words.
Format output like:
Forecast: ...
Mood: 7
Advice: ...
"""

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are a poetic, emotionally intelligent assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8
    )

    result = response.choices[0].message.content

    # Extract mood
    mood_match = re.search(r"Mood:\s*(\d+)", result)
    mood_score = int(mood_match.group(1)) if mood_match else 5

    # Choose Spotify playlist
    mood_to_spotify = {
        range(1, 4): ("😔", "https://open.spotify.com/playlist/37i9dQZF1DWUvHZA1zLcjW"),
        range(4, 7): ("😌", "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0"),
        range(7, 11): ("😊", "https://open.spotify.com/playlist/37i9dQZF1DX1BzILRveYHb")
    }

    emoji, playlist_link = "😐", "#"
    for mood_range, (e, link) in mood_to_spotify.items():
        if mood_score in mood_range:
            emoji, playlist_link = e, link
            break

    result += f"\n\n{emoji} Your mood emoji\n🎵 [Spotify Mood Playlist]({playlist_link})"
    return result

# Show result
if st.button("🔍 Analyze My Emotions"):
    if user_input.strip():
        st.markdown(get_emotional_forecast(user_input))
    else:
        st.warning("Please write something first 💬")

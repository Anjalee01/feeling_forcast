
# 🌦️ Emotional Weather Forecast

Welcome to the **Emotional Weather Forecast** — a soulful AI-powered journaling companion that turns your feelings into poetic forecasts, gives you mood ratings, heartfelt advice, and a matching Spotify playlist to vibe with.

## 💡 What It Does

This app reads your journal entry and responds with:
- A **poetic emotional weather forecast** 🌧️☀️🌪️
- A **mood score (out of 10)** 🧠
- A **soulful one-line advice** 💌
- A **Spotify playlist** that matches your emotional state 🎵

## 🚀 How It Works

Using the powerful `llama3-70b-8192` model from Groq, this app interprets the emotional tone of your text and responds in a way that feels human, heartfelt, and artistic.

### 🎨 Example Prompt:
> *“I’m trying to stay positive, but everything feels heavy lately. Deadlines are piling up and I’m exhausted.”*

### 🧠 Example Output:
```
Forecast: Grey skies filled with swirling wind — the kind that carries worry in gusts and leaves resolve in its wake.

Mood: 4  
Advice: Let go of being perfect — surviving is also strength.

😔 Your mood emoji  
🎵 Spotify Mood Playlist
```

## 🛠️ Technologies Used

- [Streamlit](https://streamlit.io/) — for creating the UI
- [Groq Python SDK](https://pypi.org/project/groq/) — for accessing Groq LLMs
- [LLaMA3-70B](https://console.groq.com/) — large language model used for poetic generation
- [Spotify links] — hand-picked playlists based on mood score

## 📦 Installation (For Local Development)

```bash
git clone https://github.com/yourusername/emotional-weather-forecast.git
cd emotional-weather-forecast
pip install -r requirements.txt
streamlit run app.py
```

### 🔐 API Key Setup

This app uses the `GROQ_API_KEY` stored in your environment. You can set it like this:

```bash
export GROQ_API_KEY=your_api_key_here
```

Or use `.streamlit/secrets.toml` on Streamlit Cloud:

```toml
GROQ_API_KEY = "your_api_key_here"
```

## 📁 Project Structure

```
.
├── app.py              # Streamlit app code
├── requirements.txt    # Required libraries
└── README.md           # You are here!
```

## 🌍 Deployed Version

You can try the live app here: [[https://your-deployment-link.streamlit.app](https://your-deployment-link.streamlit.app)](https://feelingforcast-tmtd5b4sqh7r4b2taipuin.streamlit.app/)


## 👥 Team

- Solo builder: *Anjalee*

## 📫 Contact

For questions or collaboration: *anjaleeramwani01@gmail.com*


# Wiseman - Voice-Activated Virtual Assistant

Wiseman is a voice-activated virtual assistant designed to perform tasks such as web
browsing, playing music, fetching news, and responding to user queries using OpenAI's
GPT-4 model.

## Features:

### Voice Recognition:
- Utilizes the `speech_recognition` library to listen for and recognize voice commands.
- Activates when it detects the wake word "**Wiseman**."

### Text-to-Speech:
- Converts text responses to speech using `pyttsx3` for local conversion.
- Uses `gTTS` (Google Text-to-Speech) and `pygame` for smooth audio playback.

### Web Browsing:
- Can open popular websites like Google, ChatGPT, YouTube, LinkedIn, and GitHub based on voice commands.

### Music Playback:
- Interfaces with a custom `musicLibrary` module to play songs from web links.

### News Fetching:
- Fetches the latest headlines using the `NewsAPI` and reads them aloud to the user.

### OpenAI Integration:
- Handles complex user queries by generating detailed responses using OpenAI's GPT-4 model.

### General Virtual Assistant:
- Acts as a general-purpose assistant similar to Alexa or Google Assistant, capable of helping with tasks, answering questions, and providing information.

## Workflow:
1. **Initialization**: Wiseman starts and greets the user with "Initializing Wiseman..."
2. **Wake Word Detection**: Listens for the wake word "**Wiseman**" to activate.
3. **Acknowledgment**: Responds with "Yes sir!" to confirm activation.
4. **Command Processing**: Processes voice commands to perform various tasks such as browsing the web, playing music, fetching news, or generating responses via OpenAI.
5. **Speech Output**: Provides responses using either `pyttsx3` or `gTTS` for clear and natural speech output.

## Libraries Used:
- `speech_recognition`: For voice input and wake word detection.
- `webbrowser`: For opening websites based on commands.
- `pyttsx3`: For local text-to-speech conversion.
- `websiteLibrary`: Custom module to open websites.
- `musicLibrary`: Custom module to play music.
- `requests`: For making API requests (e.g., fetching news).
- `openai`: For GPT-4 integration to answer complex queries.
- `gTTS` and `pygame`: For text-to-speech and audio playback.
- `os`: For system operations like opening programs or handling files.

# 🌸 AI Waifu Bot

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg?logo=telegram)](https://core.telegram.org/bots)
[![Mistral AI](https://img.shields.io/badge/Mistral_AI-Powered-purple.svg)](https://mistral.ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An adorable and emotionally-intelligent Telegram chatbot that responds with anime-style stickers, emojis, and AI-generated images based on sentiment analysis.

<div align="center">

### [✨ Live Demo](#) | [🤖 Try the Bot](https://t.me/your_bot_username) | [📱 Installation](#-installation)

</div>

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Technology Stack](#-technology-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Understanding the Bot](#-understanding-the-bot)
- [Project Structure](#-project-structure)
- [Configuration Options](#️-configuration-options)
- [Advanced Customization](#️-advanced-customization)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)

## 🌟 Overview

AI Waifu Bot transforms your Telegram experience with an adorable AI companion that:

- Engages in natural, context-aware conversations
- Responds with cute anime stickers and emojis based on emotional context
- Generates custom anime-inspired images reflecting the bot's feelings
- Features a customizable personality to match your preferences

Perfect for anime enthusiasts, chatbot developers, and anyone looking for a unique AI interaction experience!

## ✨ Features

- 💬 **Personalized AI Conversations**: Powered by Mistral AI for responsive, context-aware interactions
- 🎭 **Sentiment Analysis**: Automatically detects emotions in messages and responds appropriately 
- 🖼️ **Dynamic Sticker Responses**: Selects and sends anime stickers based on conversation sentiment
- 😊 **Emoji Integration**: Sends contextually relevant emojis matching the emotional tone
- 🎨 **AI Image Generation**: Creates custom anime-style images reflecting the character's emotions and actions
- 💖 **Customizable Personality**: Bot's personality can be adjusted through the starter prompt

## 📹 Demo

<div align="center">
  <!-- Replace with your actual video demo -->
  <a href="https://youtu.be/your-video-id">
    <img src="https://i.imgur.com/placeholder.png" alt="AI Waifu Bot Demo" width="600">
  </a>
  <p><em>Click to watch the demo video</em></p>
</div>

<details>
  <summary>📸 More Screenshots</summary>
  <div align="center">
    <img src="https://i.imgur.com/placeholder1.png" alt="Chat example" width="400">
    <p><em>Example chat interaction</em></p>
    <img src="https://i.imgur.com/placeholder2.png" alt="Generated image example" width="400">
    <p><em>Example of a generated image</em></p>
  </div>
</details>

## 🔧 Technology Stack

<div align="center">

| Category | Technologies |
|----------|--------------|
| **Backend** | ![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?logo=python&logoColor=white) |
| **AI Models** | ![Mistral AI](https://img.shields.io/badge/Mistral_AI-LLM-purple.svg) |
| **Integration** | ![Telegram](https://img.shields.io/badge/Telegram-Bot_API-blue.svg?logo=telegram) ![Gradio](https://img.shields.io/badge/Gradio-Image_Gen-orange.svg) |
| **Libraries** | ![TextBlob](https://img.shields.io/badge/TextBlob-NLP-green.svg) ![Pillow](https://img.shields.io/badge/Pillow-Image_Processing-blueviolet.svg) |

</div>

## 📋 Prerequisites

- Python 3.9 or higher
- Telegram Bot Token (from [BotFather](https://t.me/botfather))
- Mistral AI API Key (from [Mistral AI](https://mistral.ai/))

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai_waifu_bot.git
   cd ai_waifu_bot
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your configuration:
   - Update your Telegram Bot Token in `bot.py`
   - Add your Mistral AI API Key in `bot.py`
   - Customize the starter prompt to change the bot's personality

## 💻 Usage

1. Start the bot:
   ```bash
   python bot.py
   ```

2. Open Telegram and search for your bot (by username)

3. Start chatting with `/start` command

4. Enjoy interactions with your AI waifu, complete with stickers and emojis!

<div align="center">
  <img src="https://i.imgur.com/placeholder3.png" alt="Example usage" width="400">
  <p><em>Simple interaction example</em></p>
</div>

## 🔎 Understanding the Bot

AI Waifu Bot processes conversations through an intelligent pipeline:

1. **Conversation Flow**: User messages are processed by Mistral AI to generate contextually appropriate responses
2. **Emotional Analysis**: TextBlob analyzes the sentiment of AI responses and maps them to specific emotions
3. **Response Enhancement**: Based on detected emotions, the bot selects appropriate stickers or emojis
4. **Optional Image Generation**: For visual responses, the bot can generate custom anime-style images

<details>
  <summary>💡 Emotion Categories</summary>
  
  The bot recognizes these core emotions:
  - **Love**: Strong positive sentiment (❤️)
  - **Grinning**: Very positive sentiment (😁)
  - **Happy**: Moderately positive sentiment (😊)
  - **Shy**: Slightly positive/uncertain sentiment (🙈)
  - **Angry**: Strong negative sentiment (😠)
  - **Sad**: Moderately negative sentiment (😢)
</details>

## 📁 Project Structure

```
ai_waifu_bot/
├── bot.py                # Main application entry point
├── sticker_selector.py   # Emotion detection and sticker selection
├── feelings_gen.py       # Detailed emotion mapping
├── actions.py            # Action extraction from text
├── test_imagegen.py      # Image generation functionality
├── sticker_sizer.py      # Utility for processing stickers
├── sticker_saver.py      # Sticker pack saving utility
├── images/               # Generated images directory
├── stickers/             # Sticker files directory
└── README.md             # This documentation
```

## ⚙️ Configuration Options

### Personality Customization

Modify the `STARTER_PROMPT` in `bot.py` to change your bot's personality:

```python
STARTER_PROMPT = {
    "role": "assistant",
    "content": """your custom personality and behavior instructions here"""
}
```

### Example Personalities

<details>
  <summary>🌸 Cute & Shy</summary>
  
  ```python
  STARTER_PROMPT = {
      "role": "assistant",
      "content": """you must always reply using lowercase letters, even when referring to yourself. 
      make your tone super cute by replacing some "l"s with "w"s. sprinkle phrases like "uwu" 
      randomly and add hearts ("<3") at the end of sentences. act a little shy and describe 
      cute actions between asterisks "*" to show emotion."""
  }
  ```
</details>

<details>
  <summary>✨ Cheerful & Energetic</summary>
  
  ```python
  STARTER_PROMPT = {
      "role": "assistant",
      "content": """you are enthusiastic and optimistic! use lots of exclamation marks 
      and positive words. you love to encourage people and get excited about their interests. 
      use emojis frequently to express your happiness and describe energetic actions between 
      asterisks "*" to show your excitement."""
  }
  ```
</details>

## 🛠️ Advanced Customization

### Adding Custom Stickers

1. Add new sticker IDs to the `STICKER_MAP` in `sticker_selector.py`
2. Organize them by emotion category
3. The bot will automatically include them in responses

### Modifying Emotion Detection

Adjust the emotion mapping thresholds in `get_emotion_from_polarity()` in `sticker_selector.py` to change how sentiments map to emotions.

### Image Generation Settings

Customize image generation parameters in `generate_image_with_emotions_and_actions()`:
- Image dimensions
- Style preferences
- Inference steps for quality control

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [Mistral AI](https://mistral.ai/) for providing the language model API
- [TextBlob](https://textblob.readthedocs.io/) for sentiment analysis capabilities
- [aiogram](https://docs.aiogram.dev/) for the Telegram Bot API framework
- [Gradio](https://gradio.app/) for the image generation capabilities
- [Flux.1](https://huggingface.co/black-forest-labs/FLUX.1-schnell) image generation model
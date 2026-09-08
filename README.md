# 🤖 Jarvis: AI Voice Assistant Desktop Agent

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Gemini AI](https://img.shields.io/badge/Model-Gemini%203.6%20Flash-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

An autonomous desktop AI voice assistant powered by **Google Gemini 3.6 Flash**, featuring speech recognition, text-to-speech feedback, conversational memory, and OS automation via **Function Calling**.

---

## ✨ Features

- 🎙️ **Real-Time Voice Interface**: Offline text-to-speech with ambient noise calibration.
- 🧠 **Conversational Memory**: Multiturn chat memory powered by `google-genai` chat sessions.
- 🛠️ **Autonomous Function Calling**: Gemini chooses when to execute local Python tools:
  - 🖥️ Launch local Windows apps (`Notepad`, `Calculator`, `Command Prompt`).
  - 🌐 Open web links and trigger browser searches.
  - 📊 Live system diagnostics (CPU, RAM, and Battery metrics via `psutil`).
  - ⏰ Real-time date and time inquiries.
- 🔒 **Secure Architecture**: API keys isolated via `.env` environment variables.

---

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/Jarvis-AI-Voice-Assistant.git](https://github.com/YOUR_USERNAME/Jarvis-AI-Voice-Assistant.git)
cd Jarvis-AI-Voice-Assistant

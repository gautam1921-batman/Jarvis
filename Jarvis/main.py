import sys
import pyttsx3
import speech_recognition as sr
from google import genai
from google.genai import types
from rich.console import Console
from rich.panel import Panel

import config
from tools import AVAILABLE_TOOLS

console = Console()

# Initialize Gemini Client
ai_client = genai.Client(api_key=config.GEMINI_API_KEY)

# Initialize Chat Session with Tools
chat_session = ai_client.chats.create(
    model=config.MODEL_NAME,
    config=types.GenerateContentConfig(
        system_instruction=config.SYSTEM_INSTRUCTION,
        tools=AVAILABLE_TOOLS
    )
)

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

def setup_voice():
    engine.setProperty('rate', config.SPEECH_RATE)
    voices = engine.getProperty('voices')
    if len(voices) > config.VOICE_INDEX:
        engine.setProperty('voice', voices[config.VOICE_INDEX].id)

def speak(text: str):
    """Outputs text to both the rich terminal and speaker output."""
    console.print(Panel(f"[bold cyan]Jarvis:[/bold cyan] {text}", border_style="cyan"))
    engine.say(text)
    engine.runAndWait()

def listen() -> str:
    """Captures microphone input with ambient noise calibration."""
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 0.8
    
    with sr.Microphone() as source:
        console.print("[dim]Listening...[/dim]")
        recognizer.adjust_for_ambient_noise(source, duration=0.8)
        
        try:
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=10)
            console.print("[dim]Processing voice input...[/dim]")
            
            query = recognizer.recognize_google(audio)
            console.print(f"[bold green]You:[/bold green] {query}")
            return query.lower()
            
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            console.print("[yellow]-> Voice not understood.[/yellow]")
            return ""
        except sr.RequestError:
            console.print("[red]-> Network error in speech recognition.[/red]")
            return ""

def process_command(prompt: str) -> bool:
    if not prompt:
        return True

    if any(term in prompt for term in ["exit", "stop", "goodbye", "shutdown"]):
        speak("Shutting down core protocols. Goodbye, Boss.")
        return False

    try:
        response = chat_session.send_message(prompt)
        speak(response.text.strip())
    except Exception as e:
        console.print(f"[bold red]Execution Error:[/bold red] {e}")
        speak("I encountered an internal error processing that command.")

    return True

if __name__ == "__main__":
    setup_voice()
    console.print(Panel.fit("[bold blue]JARVIS AI ASSISTANT[/bold blue]\n[dim]Autonomous Voice Core Online[/dim]", border_style="blue"))
    speak("Jarvis AI online and ready for commands.")
    
    running = True
    while running:
        user_input = listen()
        running = process_command(user_input)
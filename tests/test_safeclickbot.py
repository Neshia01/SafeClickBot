"""Regression tests for the SafeClickBot knowledge base."""
from pathlib import Path

from chatbot.engine import ChatbotEngine, load_themes

THEMES = load_themes(Path(__file__).resolve().parent.parent / "themes")
ENGINE = ChatbotEngine(THEMES["safeclickbot"])

def test_safeclickbot_theme_is_loaded():
    assert THEMES["safeclickbot"]["bot_name"] == "SafeClickBot"

def test_all_required_intents_exist():
    expected = {
        "salam", "phishing", "link_palsu", "keamanan_otp", "password",
        "penipuan_online", "malware", "akun_diretas", "data_pribadi",
        "terima_kasih",
    }
    actual = {item["tag"] for item in THEMES["safeclickbot"]["intents"]}
    assert actual == expected

def test_core_questions_are_classified():
    cases = [
        ("Apa itu phishing?", "phishing"),
        ("Bagaimana mengenali link palsu?", "link_palsu"),
        ("Apakah kode OTP boleh dibagikan?", "keamanan_otp"),
        ("Bagaimana cara membuat password aman?", "password"),
        ("Ciri penipuan online?", "penipuan_online"),
        ("Apa itu malware?", "malware"),
        ("Akun saya diretas", "akun_diretas"),
        ("Cara melindungi data pribadi?", "data_pribadi"),
    ]
    for message, expected_intent in cases:
        intent, _ = ENGINE.classify(message)
        assert intent == expected_intent, (message, intent)

def test_unknown_question_uses_fallback():
    result = ENGINE.reply("berapa harga tiket konser?")
    assert result["intent"] is None
    assert result["reply"] in THEMES["safeclickbot"]["fallback"]

"""
Chatbot engine with multi-language support (Tamil / English / Tanglish).
"""
import os
import requests
from chatbot.shg_knowledge import get_shg_answer
from chatbot.language import detect_language

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "meta-llama/llama-3.1-8b-instruct:free"


def _fallback(message: str, lang: str) -> str:
    msg = message.lower()

    greetings = {
        "english": "Hello! I'm the SHG Smart Assistant for Thanjavur. Ask me about schemes, loans, business ideas, or any general question.",
        "tamil": "வணக்கம்! நான் தஞ்சாவூர் SHG ஸ்மார்ட் உதவியாளர். திட்டங்கள், கடன், வணிக யோசனைகள் பற்றி கேளுங்கள்.",
        "tanglish": "Vanakkam! Naan Thanjavur SHG Smart Assistant. Schemes, loan, business ideas pathi kelunga.",
    }
    thanks = {
        "english": "You're welcome! Ask anything else.",
        "tamil": "நன்றி! வேறு எதுவும் கேளுங்கள்.",
        "tanglish": "Nandri! Vera edhuvum kelunga.",
    }

    if any(g in msg for g in ["hello", "hi", "hey", "namaste", "vanakkam", "வணக்கம்"]):
        return greetings.get(lang, greetings["english"])
    if "thank" in msg or "நன்றி" in msg or "nandri" in msg:
        return thanks.get(lang, thanks["english"])
    if "python" in msg:
        return ("Python is a popular programming language.\n\n"
                "```python\nprint('Vanakkam Thanjavur!')\n```")
    if "?" in msg or "என்ன" in msg or "enna" in msg:
        return {
            "english": "Good question. Enable AI key (OPENROUTER_API_KEY) for detailed answers on general topics.",
            "tamil": "நல்ல கேள்வி. AI key (OPENROUTER_API_KEY) enable பண்ணுங்க.",
            "tanglish": "Nalla kelvi. AI key (OPENROUTER_API_KEY) enable pannunga.",
        }.get(lang, "Good question!")

    return {
        "english": "I help with SHG schemes, Thanjavur business ideas, loans. Could you rephrase?",
        "tamil": "SHG திட்டங்கள், வணிக யோசனைகள், கடன் உதவ முடியும். மீண்டும் சொல்லுங்கள்.",
        "tanglish": "SHG schemes, business ideas, loan-ku help pannuven. Marubadi sollunga.",
    }.get(lang, "Please rephrase.")


def get_bot_response(user_message: str, preferred_lang: str = None) -> str:
    """Main entry: returns the bot's reply."""
    if not user_message or not user_message.strip():
        return "Please type a message / தயவுசெய்து ஒரு செய்தி டைப் பண்ணுங்க."

    # Auto-detect language unless forced
    lang = preferred_lang if preferred_lang in ("tamil", "english", "tanglish") else detect_language(user_message)

    # 1. SHG answer
    shg = get_shg_answer(user_message, lang)
    if shg:
        return shg

    # 2. Try AI
    api_key = os.getenv("OPENROUTER_API_KEY", "").strip()
    if api_key:
        try:
            lang_instruction = {
                "tamil": "Reply in Tamil (தமிழ்).",
                "tanglish": "Reply in Tanglish (Tamil words typed in English letters).",
                "english": "Reply in clear English.",
            }.get(lang, "Reply in English.")

            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            }
            payload = {
                "model": MODEL,
                "messages": [
                    {"role": "system",
                     "content": (f"You are SHG Smart Assistant for women's SHGs in "
                                 f"Thanjavur, Tamil Nadu. Help with schemes, loans, "
                                 f"business ideas. {lang_instruction} Keep answers simple.")},
                    {"role": "user", "content": user_message},
                ],
                "max_tokens": 700,
            }
            r = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=30)
            if r.status_code == 200:
                data = r.json()
                return data["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print("AI error:", e)

    # 3. Fallback
    return _fallback(user_message, lang)
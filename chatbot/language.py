"""
Detects whether the input is Tamil script, English, or Tanglish.
"""
import re


def detect_language(text: str) -> str:
    """
    Returns: 'tamil', 'tanglish', or 'english'
    """
    if not text:
        return "english"

    # Check for Tamil Unicode characters
    tamil_chars = re.findall(r"[\u0B80-\u0BFF]", text)
    if len(tamil_chars) > 2:
        return "tamil"

    # Tanglish detection - Tamil words typed in English letters
    tanglish_markers = [
        "enna", "epdi", "eppadi", "vanakkam", "nanba", "nanbi",
        "sollu", "solunga", "kudu", "kudunga", "venum", "vendum",
        "illa", "illai", "iruku", "irukku", "pannu", "pannunga",
        "theriyuma", "puriyutha", "mudiyuma", "evlo", "evvalavu",
        "yaaru", "yethu", "edhu", "eppo", "eppothu", "seri",
        "romba", "nalla", "sari", "theva", "thozhil", "panam",
        "kadan", "valarchi", "magalir", "amma", "akka", "thangachi",
        "engey", "enga", "yaen", "yen", "sollunga"
    ]
    words = re.findall(r"\b[a-z]+\b", text.lower())
    hits = sum(1 for w in words if w in tanglish_markers)
    if hits >= 1:
        return "tanglish"

    return "english"
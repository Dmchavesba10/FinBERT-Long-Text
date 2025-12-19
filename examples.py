"""
examples.py
Demonstrates how to use the FinBERT-Long-Text analyzer.
"""
from sentiment_analyzer import SentimentAnalyzer

def run_examples():
    # Initialize the model once
    analyzer = SentimentAnalyzer()

    print("\n--- TEST 1: Simple Headline (Short Text) ---")
    short_text = "NVIDIA reports record-breaking revenue for Q3, beating all analyst expectations."
    score, sentiment = analyzer.analyze(short_text)
    print(f"Text: {short_text}")
    print(f"Result: {sentiment} ({score:.4f})\n")

    print("--- TEST 2: The 'Buried Lead' (Long Text with Mixed Signals) ---")
    # This simulates a long article:
    # Paragraph 1: Boring history (Neutral)
    # Paragraph 2: Past scandal (Negative)
    # Paragraph 3: Current massive success (Positive) -> THIS should win.
    long_text = (
        "In 1999, the company was founded in a small garage in California. " * 20 + # Boring filler
        "In 2015, the company faced a class-action lawsuit regarding privacy violations. " * 5 + # Negative noise
        "HOWEVER, today the CEO announced a 200% increase in dividends and a strategic partnership with OpenAI that ensures growth for the next decade." # The real signal
    )
    
    score, sentiment = analyzer.analyze(long_text)
    print(f"Text Length: {len(long_text)} characters")
    print(f"Expected: Positive (detecting the recent news despite past noise)")
    print(f"Result:   {sentiment} ({score:.4f})\n")

    print("--- TEST 3: Purely Neutral/Informational ---")
    neutral_text = "The stock market will remain closed on Monday due to the national holiday. Trading resumes Tuesday."
    score, sentiment = analyzer.analyze(neutral_text)
    print(f"Text: {neutral_text}")
    print(f"Result: {sentiment} ({score:.4f})\n")

if __name__ == "__main__":
    run_examples()

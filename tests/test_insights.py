from insights import generate_insights

def test_generate_insights():
    insights = generate_insights("Reels", 250, 50, 45)
    assert "Reels" in insights, "GPT insights generation failed"

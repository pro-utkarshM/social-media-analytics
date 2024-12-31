import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_insights(post_type, avg_likes, avg_shares, avg_comments):
    prompt = (
        f"Analyze the following social media post data:\n"
        f"Post Type: {post_type}\n"
        f"Average Likes: {avg_likes}\n"
        f"Average Shares: {avg_shares}\n"
        f"Average Comments: {avg_comments}\n\n"
        f"Provide actionable insights for improving engagement."
    )
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
    )
    return response.choices[0].text.strip()

from database import connect_to_astra_db, fetch_average_metrics
from insights import generate_insights

if __name__ == "__main__":
    session = connect_to_astra_db()
    post_type = input("Enter post type (e.g., Reels, Carousel): ").strip()

    metrics = fetch_average_metrics(session, post_type)
    if metrics and metrics.avg_likes:
        avg_likes, avg_shares, avg_comments = metrics.avg_likes, metrics.avg_shares, metrics.avg_comments
        print(f"Post Type: {post_type}")
        print(f"Average Likes: {avg_likes}, Shares: {avg_shares}, Comments: {avg_comments}")

        insights = generate_insights(post_type, avg_likes, avg_shares, avg_comments)
        print("\nGenerated Insights:")
        print(insights)
    else:
        print(f"No data found for post type: {post_type}")

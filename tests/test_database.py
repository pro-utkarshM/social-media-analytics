from database import connect_to_astra_db, fetch_average_metrics

def test_fetch_average_metrics():
    session = connect_to_astra_db()
    result = fetch_average_metrics(session, "Reels")
    assert result is not None, "Metrics fetch failed"

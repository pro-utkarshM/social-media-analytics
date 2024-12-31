from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from config import ASTRA_CLIENT_ID, ASTRA_CLIENT_SECRET, ASTRA_DB_ENDPOINT

def connect_to_astra_db():
    auth_provider = PlainTextAuthProvider(ASTRA_CLIENT_ID, ASTRA_CLIENT_SECRET)
    cluster = Cluster([ASTRA_DB_ENDPOINT], auth_provider=auth_provider)
    return cluster.connect()

def fetch_average_metrics(session, post_type):
    query = """
    SELECT AVG(likes) AS avg_likes, AVG(shares) AS avg_shares, AVG(comments) AS avg_comments
    FROM engagement
    WHERE post_type = %s
    """
    result = session.execute(query, (post_type,))
    return result.one()

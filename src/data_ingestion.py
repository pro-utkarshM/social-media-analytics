import uuid
from database import connect_to_astra_db

def create_schema(session):
    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS social_media WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}
    """)
    session.set_keyspace('social_media')

    session.execute("""
    CREATE TABLE IF NOT EXISTS engagement (
        post_id UUID PRIMARY KEY,
        post_type TEXT,
        likes INT,
        shares INT,
        comments INT
    )
    """)

def insert_mock_data(session):
    mock_data = [
        (uuid.uuid4(), 'Carousel', 120, 30, 15),
        (uuid.uuid4(), 'Reels', 250, 50, 45),
        (uuid.uuid4(), 'Static Image', 80, 20, 10),
        (uuid.uuid4(), 'Carousel', 140, 40, 25),
        (uuid.uuid4(), 'Reels', 300, 60, 50),
    ]

    for record in mock_data:
        session.execute("""
        INSERT INTO engagement (post_id, post_type, likes, shares, comments)
        VALUES (%s, %s, %s, %s, %s)
        """, record)

if __name__ == "__main__":
    session = connect_to_astra_db()
    create_schema(session)
    insert_mock_data(session)
    print("Mock data inserted successfully.")

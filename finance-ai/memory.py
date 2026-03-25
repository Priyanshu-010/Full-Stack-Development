import sqlite3

conn = sqlite3.connect("memory-db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS chats (
  user_id TEXT,
  message TEXT,
  response TEXT
)             
""")

conn.commit()
def save_chat(user_id, message, response):
    cursor.execute(
        "INSERT INTO chats VALUES (?, ?, ?)",
        (user_id, message, response)
    )
    conn.commit()

def get_history(user_id):
    cursor.execute(
        "SELECT message, response FROM chats WHERE user_id=?",
        (user_id,)
    )
    return cursor.fetchall()
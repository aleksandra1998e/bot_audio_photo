import sqlite3


def save_to_database_audio(user_id, audio):
    # Connect to the database
    conn = sqlite3.connect("audio.db")
    c = conn.cursor()

    # Create a table to store the audio files if it doesn't already exist
    c.execute(
        "CREATE TABLE IF NOT EXISTS audio_files (user_id INTEGER, audio BLOB)"
    )

    # Insert the audio file into the table
    c.execute(
        "INSERT INTO audio_files (user_id, audio) VALUES (?, ?)",
        (user_id, audio)
    )

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()


def save_to_database_photo(user_id, photo):
    # Connect to the database
    conn = sqlite3.connect("photos.db")
    c = conn.cursor()

    # Create a table to store the photos if it doesn't already exist
    c.execute(
        "CREATE TABLE IF NOT EXISTS photos (user_id INTEGER, photo BLOB)"
    )

    # Insert the photo into the table
    c.execute(
        "INSERT INTO photos (user_id, photo) VALUES (?, ?)",
        (user_id, photo.get_file())
    )

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

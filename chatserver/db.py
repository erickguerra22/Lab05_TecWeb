#!/usr/bin/python

import sqlite3

def connect():
    conn = sqlite3.connect('mydb.db')
    return conn

def get_messages():
    messages = []

    db = connect()
    cur = db.cursor()
    cur.execute("""
        SELECT
            id,
            text,
            user,
            created_on
        FROM
            messages;
    """)
    rows = cur.fetchall()

    for row in rows:
        message = {
            "id": row[0],
            "text": row[1],
            "user": row[2],
            "created_on": row[3]
        }
        messages.append(message)

    return messages

def create_message(message):
    
    db = connect()
    cur = db.cursor()
    cur.execute("""
        INSERT INTO messages
            (text, user, created_on)
            VALUES (?, ?, datetime());
    """, (
        message["text"],
        message["user"]
    ))
    db.commit()
    return { "success": True }
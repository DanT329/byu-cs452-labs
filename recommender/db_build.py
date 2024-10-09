## This script is used to create the tables in the database

import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

CONNECTION = os.getenv('CONNECTION_STRING')

# need to run this to enable vector data type
CREATE_EXTENSION = "CREATE EXTENSION vector"

# TODO: Add create table statement
CREATE_PODCAST_TABLE = """
CREATE TABLE IF NOT EXISTS podcast (
    id VARCHAR(255) PRIMARY KEY,
    title TEXT NOT NULL
);
"""
# TODO: Add create table statement
CREATE_SEGMENT_TABLE = """
CREATE TABLE IF NOT EXISTS podcast_segment (
    id VARCHAR(255) PRIMARY KEY,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    content TEXT NOT NULL,
    embedding VECTOR(128), 
    podcast_id VARCHAR(255),
    FOREIGN KEY (podcast_id) REFERENCES podcast(id)
);
"""
# TODO: Create tables with psycopg2 (example: https://www.geeksforgeeks.org/executing-sql-query-with-psycopg2-in-python/)

try:
    conn = psycopg2.connect(CONNECTION)
    cur = conn.cursor()
    
    # Enable vector extension
    cur.execute(CREATE_EXTENSION)
    
    # Create the tables
    cur.execute(CREATE_PODCAST_TABLE)
    cur.execute(CREATE_SEGMENT_TABLE)

    # Commit changes and close
    conn.commit()
    cur.close()
    conn.close()
    print("Tables created successfully.")
except Exception as e:
    print(f"Error: {e}")



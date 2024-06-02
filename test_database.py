
import os
import random
from supabase import create_client, Client

os.environ["SUPABASE_URL"] = "https://jjjvrciysvivtfzqdxbj.supabase.co"
os.environ["SUPABASE_KEY"] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpqanZyY2l5c3ZpdnRmenFkeGJqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTY5MjU0MDUsImV4cCI6MjAzMjUwMTQwNX0.B4XP_SAihW2RMLu-Iyys2418FtFYIwM37XAQ_ZgA5OI"

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)


# connect database to the GUI component
# display database items: questions and answer choices
def fetch_data():
    response = supabase.table("question_bank").select('*').execute()
    data = response.data
    # display data
    print(data)

fetch_data()



# update database when question status changed


# randomly assign answer choices to touch sesnors



# send signal to GUI when condition met: question answered correctly or incorrectly
# send signal to audio output when condition met: question answered correctly or incorrectly


# If question answered incorrectly, rotate question to back and continue repeating until all questions answered correctly
# Update question status to database when question answered correctly
#  End question rotation once all questions answered correctly
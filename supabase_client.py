import os
from pdb import main
from supabase import create_client, Client
from dotenv import load_dotenv
import json


# Load Supabase Credentials
load_dotenv()
url = os.getenv("SUPABASE_URL")
if url is None:
	raise ValueError("SUPABASE_URL environment variable is not set")

key = os.getenv("SUPABASE_KEY")
if key is None:
	raise ValueError("SUPABASE_KEY environment variable is not set")

supabase: Client = create_client(url, key)
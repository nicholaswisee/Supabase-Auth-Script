import json
from supabase_client import supabase

def main():
  with open("example.json", "r") as file:
    users = json.load(file)
  
  for user in users:
    response = supabase.auth.sign_up(
      {
        "email": user["email"],
        "password": user["password"],
      }
    )
    
    if response.user is None:
      print(f"Failed to create user {user['email']}")

if __name__ == "__main__":
    main()
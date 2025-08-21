import json
from supabase_client import supabase

def main():
  with open("./data/bcc.json", "r") as file:
    users = json.load(file)
  
  for user in users:
    response = supabase.auth.admin.create_user(
      {
        "email": user["email"],
        "password": user["password"],
        "email_confirm": True,
        "user_metadata": {
          "display_name": user['team_name']
        }
      }
    )
    
    if response.user is None:
      print(f"Failed to create user {user['email']}")

if __name__ == "__main__":
    main()
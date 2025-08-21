# Supabase Auth Script

A simple Python script to manage user authentication and data with Supabase.

## Requirements

- Python 3.8+
- [supabase-py](https://github.com/supabase-community/supabase-py)
- [requests](https://docs.python-requests.org/en/latest/)

## Installation

1. Clone this repository:

   ```pwsh
   git clone https://github.com/nicholaswisee/Supabase-Auth-Script.git
   cd Supabase-Auth-Script
   ```

2. (Optional) Create and activate a virtual environment:

  on Windows:

   ```pwsh
    python -m venv venv
    venv\Scripts\activate
   ```

  on macOS/Linux:

  ```zsh
    python3 -m venv venv
    source venv/bin/activate
  ```

3. Install dependencies:

   ```pwsh
   pip install -r requirements.txt
   ```

4. Configure environment variables in a .env file using the format in .env.example

## Usage

Edit `main.py` and `supabase_client.py` to configure your Supabase credentials and logic. Run the script:

```pwsh
python main.py
```

## License
MIT

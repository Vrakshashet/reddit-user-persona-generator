Reddit User Persona Generator


Overview:
This project creates a .txt file by extracting public posts and comments from a given Reddit user profile. After that, you can enter this data into ChatGPT (or another LLM) to create a user persona that reveals motivations, frustrations, goals, behaviors, and personality traits.

Features:
    Scrapes posts/comments from any public Reddit profile.
    Saves all user content to a .txt file.
    Ideal for running content through ChatGPT to generate a persona.

    
Steps to follow:

1. Clone the Repository
    git clone https://github.com/your-username/reddit.git
    cd reddit

2. Install Dependencies
    pip install requests beautifulsoup4

3. Run the Script
    python scrape_reddit_persona.py
4. Input Reddit Profile URL
    Example:
        Enter Reddit profile URL: https://www.reddit.com/user/Hungry-Move-6603/

5. Output
    A .txt file (e.g., Hungry-Move-6603_raw.txt) will be created containing the user’s post and comment content.

Generate Persona (Optional):

    After running the script:
    -Open the generated .txt file
    -Copy the contents
    -Paste it into ChatGPT or another LLM with a prompt like:
    -"Copy and paste the content into ChatGPT to generate the persona."

Project Structure:

reddit/
│
├── reddit.py      # Main Python script
├── README.md                     # Project documentation
└── *.txt                         # Output files per Reddit user


Tech Stack:

    Python 3.x
    Requests
    BeautifulSoup4

Disclaimer:
    This tool only works for public Reddit profiles. It does not support private users or deleted content. Always respect users’ privacy and use the generated personas ethically.

License:
MIT License
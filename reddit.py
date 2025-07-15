import requests
from bs4 import BeautifulSoup
import time

HEADERS = {'User-Agent': 'Mozilla/5.0'}
MAX_ITEMS = 20

def extract_username(url):
    return url.strip("/").split("/")[-1]

def get_user_content(username):
    base_url = f"https://old.reddit.com/user/{username}/"
    content = []

    for section in ['submitted', 'comments']:
        url = f"{base_url}{section}/"
        try:
            res = requests.get(url, headers=HEADERS)
            soup = BeautifulSoup(res.text, 'html.parser')
            posts = soup.find_all("div", class_="entry")[:MAX_ITEMS]

            for post in posts:
                title = post.find("a", class_="title")
                body = post.find("div", class_="usertext-body")
                if title:
                    content.append("Post Title: " + title.get_text(strip=True))
                if body:
                    content.append("Post Body: " + body.get_text(strip=True))
            time.sleep(2)
        except Exception as e:
            print(f"Error scraping {section}: {e}")
    return content

def save_to_txt(username, content):
    filename = f"{username}_raw.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for item in content:
            f.write(item + "\n\n")
    print(f"Reddit content saved to {filename}")
    print("Copy and paste the content into ChatGPT to generate the persona.")

def main():
    reddit_url = input("Enter Reddit profile URL: ").strip()
    username = extract_username(reddit_url)
    print(f"Scraping activity for u/{username}...")

    content = get_user_content(username)
    if not content:
        print("No content found.")
        return

    save_to_txt(username, content)

if __name__ == "__main__":
    main()

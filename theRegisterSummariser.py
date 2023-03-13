import requests
from bs4 import BeautifulSoup
import datetime
import openai

# Configure OpenAI API key
openai.api_key = "<CHANGE_ME>"

# Define function to summarize text using OpenAI's GPT-3 model
def summarize_text(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following text:\n\n{text}\n\nSummary:",
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# Get the current date and format it as YYYY/MM/DD
today = datetime.datetime.today().strftime("%Y/%m/%d")

# Create the URL for the current date
url = f"https://www.theregister.com/Archive/{today}/"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")
articles = soup.find_all("article")

# Prompt the user to select an article
print("Please select an article to summarize:")
print("0. Summarize all articles")
for i, article in enumerate(articles):
    title = article.find("h4").get_text()
    print(f"{i+1}. {title}")
selection = int(input("\n>>> ")) - 1

if selection == -1:
    # Summarize all articles
    for i, article in enumerate(articles):
        link = "https://www.theregister.com" + article.find("a")["href"]
        article_page = requests.get(link, headers=headers)
        article_soup = BeautifulSoup(article_page.content, "html.parser")
        article_text = "".join([p.get_text() for p in article_soup.find_all("p")])
        title = article_soup.title.string
        summary = summarize_text(article_text)
        print(f"\n\nTitle ({i+1}):", title)
        print(summary)
else:
    # Extract the selected article's information and summarize the text
    selected_article = articles[selection]
    link = "https://www.theregister.com" + selected_article.find("a")["href"]
    article_page = requests.get(link, headers=headers)
    article_soup = BeautifulSoup(article_page.content, "html.parser")
    article_text = "".join([p.get_text() for p in article_soup.find_all("p")])
    title = article_soup.title.string
    summary = summarize_text(article_text)
    print("\n\nTitle:", title)
    print(summary)
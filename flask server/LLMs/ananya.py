from transformers import pipeline
import pdfplumber
from googleapiclient.discovery import build
from flask import Flask, render_template_string

app = Flask(__name__)

# imp --> 10,000 queries per day limit
API_KEY = 'AIzaSyD0p7lDyhV_xzC-F928KB-IvEBWm0tgaY8'
CX = 'b5ae4213aef84410b'  
# Pegasus-XSUM model
summarizer = pipeline("summarization", model="google/pegasus-xsum")

def extract_text_from_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        app.logger.error(f"Error extracting text from PDF: {str(e)}. File: {pdf_path}")
        return f"Error extracting text from PDF: {str(e)}. Please ensure the file is a valid PDF."


def fetch_articles_from_web(query, num_results=5):
    try:
        # build the service using API key
        service = build("customsearch", "v1", developerKey=API_KEY)

        # make a request to the Custom Search API
        result = service.cse().list(q=query, cx=CX, num=num_results).execute()

        # extracting links from the search results
        articles = [item['link'] for item in result.get('items', [])]

        return articles
    except Exception as e:
        app.logger.error(f"Error fetching articles from web: {str(e)}")
        return f"Error fetching articles from web. Please try again."

@app.route("/article-generator")
def hello():
    pdf_path = '/Users/ananyasirandass/Downloads/ML intro.pdf'
    article = extract_text_from_pdf(pdf_path)
    
    if "Error" in article:
        return article  # Return the error message directly
    
    max_sequence_length = 512
    truncated_article = article[:max_sequence_length]
    summary = summarizer(truncated_article, max_length=230, min_length=30, do_sample=False)
    summary_text = summary[0]['summary_text']

    articles = fetch_articles_from_web(summary_text, num_results=5)
    
    if "Error" in articles:
        return articles  # Return the error message directly

    clickable_link = "<br>".join([f"<a href='{url}' target='_blank'>{url}</a>" for idx, url in enumerate(articles, start=1)])

    return render_template_string(clickable_link)


if __name__ == "__main__":
    app.run(debug=True)
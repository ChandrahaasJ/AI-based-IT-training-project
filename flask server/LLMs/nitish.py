import pdfplumber
from gensim.models.doc2vec import Doc2Vec,\
    TaggedDocument
from nltk.tokenize import word_tokenize
from threading import Thread
import requests
from transformers import AutoTokenizer, AutoModel
import multiprocessing
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi as yta
from langchain_community.document_loaders import YoutubeLoader
import numpy as np
API_URL = "https://api-inference.huggingface.co/models/google/pegasus-xsum"
headers = {"Authorization": "Bearer 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"}
def cosine_similarity(a,b):
    cosine = np.dot(a,b) / (np.linalg.norm(a)) * (np.linalg.norm(b))
    return cosine
def load_pdf(pdf_path):
    pdf_path=pdf_path.strip('\"')
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text()
            return text
    except FileNotFoundError:
        print(f"Error: File not found at the specified path: {pdf_path}")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
        return None
def infer_vector(doc, model):
    return model.infer_vector(word_tokenize(doc.lower()))

def load_vector_embeddings_from_data(data):
    tagged_data = [TaggedDocument(words=word_tokenize(str(doc.lower())), tags=[str(i)]) for i, doc in enumerate(data)]
    model = Doc2Vec(vector_size=20, min_count=2, epochs=100)
    model.build_vocab(tagged_data)
    model.train(tagged_data, total_examples=model.corpus_count, epochs=model.epochs)

    with multiprocessing.Pool() as pool:
        document_vectors = pool.starmap(infer_vector, zip(data, [model]*len(data)))
def summary_gen(payload):#required 2
    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()
    if isinstance(result, list) and len(result) > 0 and isinstance(result[0], dict):
        summary_text = result[0].get('summary_text', '')
        return summary_text
    return None
def load_model():#required 1
    tokenizer = AutoTokenizer.from_pretrained("google/pegasus-xsum")
    model=AutoModel.from_pretrained("google/pegasus-xsum",)
def fetch_youtube_videos(api_key, query, max_results=5):
    youtube = build('youtube', 'v3', developerKey=api_key)


    # Call the search.list method to retrieve search results
    search_response = youtube.search().list(
        q=query,
        type='video',
        part='id,snippet',
        maxResults=max_results  # Specify the number of results you want
    ).execute()

    # Extract video details from the search results
    videos = []
    for search_result in search_response.get('items', []):
        video = {
            'title': search_result['snippet']['title'],
            'video_id': search_result['id']['videoId'],
            'thumbnail_url': search_result['snippet']['thumbnails']['default']['url']
        }
        videos.append(video)

    return videos
def link_gen(query):#required 3
    # Example Usage for 3 video recommendations
    api_key = 'AIzaSyCzb0smKSb1xSW5gppSbdpPo1FPJuRgEGw'
    recommendations = fetch_youtube_videos(api_key, query, max_results=5)
    a=[]
    b=[]

    for index, video in enumerate(recommendations, start=5):
        embed_code = f'<iframe width="560" height="315" src="https://www.youtube.com/watch?v={video["video_id"]}" frameborder="0" allowfullscreen></iframe>'
        embed2=f'https://www.youtube.com/watch?v={video["video_id"]}'
        a.append(embed2)
        loader = YoutubeLoader.from_youtube_url(
        f'https://www.youtube.com/watch?v={video["video_id"]}',
        add_video_info=False,
        language=["en", "id"],
        translation="en",)
        #b.append(loader.load()) # a is the link and b is the transcript of the video here
    return a # using b [0 to 4 ] I am able to get the transcript of each vidoes individually and store the transcript in an array. Now i need to get the vectors of each of them into an array
def final_task(a):#required
    m=multiprocessing.Process(target=load_model)
    b=load_pdf(a)
    #print("Loaded pdf")
    #print("Summary generation started")
    d=summary_gen(b)
    if d==None:
        d=summary_gen(b)
    print(f"Summary of data is {d}")
    e=link_gen(d)
    #print(e)
    return e
#Text summariazation by Ps G88
"""
modules used 
spacy //pip install spacy
youtube_transcript_api //pip install youtube-transcript-api
google.generativeai  //pip install google-generativeai

if anyone is using conda , intall it according to its requirements 
"""
import spacy 
from spacy .lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
from youtube_transcript_api import YouTubeTranscriptApi as yta 
import google.generativeai as palm
import re 
import ai21


class all_in_one():
        #def getsentence(data):#Give data in the string format 
        def getsentence(data,lines):#Give data in the string format and no of requried lines 
                #lines=100
                stopwords=list(STOP_WORDS)
                nlp=spacy.load('en_core_web_sm')
                docx=nlp(data)
                wordFrequencies={}
                for word in docx:
                    if word.text not in stopwords:
                        if word.text not in wordFrequencies.keys():
                            wordFrequencies[word.text]=1
                        else:
                            wordFrequencies[word.text]+=1

                maximumfreq=max(wordFrequencies.values())
                for word in wordFrequencies.keys():
                    wordFrequencies[word]=(wordFrequencies[word]/maximumfreq) 
                sentencelist=[sentence for sentence in docx.sents]
                sentencescores={}
                for sent in sentencelist:
                    for word in sent :
                        if word.text.lower() in wordFrequencies.keys():
                            if len(sent.text.split(' '))<30:
                                if sent not in sentencescores.keys():
                                    sentencescores[sent]=wordFrequencies[word.text.lower()]
                                else:
                                    sentencescores[sent]+=wordFrequencies[word.text.lower()]
                #print(sentencescores)
             

                summarized=nlargest(lines,sentencescores,key=sentencescores.get)
                final=""
                for i in summarized:
                    final+=str(i)
                return final 
        def transcribe(link):#Here pass the link only , copy it from the url 
                ids=link.split("=")
                vid_id=ids[1]
                data=yta.get_transcript(vid_id)
                transcript=''
                for value in data:
                    for key,val in value.items():
                        if key=="text":
                            transcript+=val

                l=transcript.splitlines()
                finaldata=" ".join(l)
                return finaldata
        def askai(data):#basically u can ask anything , data should be given in sting format
                apikey="API key"
                palm.configure(api_key=apikey)
                modelid='models/text-bison-001'
                toBeAsked=data#to be given in string 

                """models/chat-bison-001
                models/text-bison-001
                models/embedding-gecko-001"""


                completion=palm.generate_text(
                    model=modelid,
                    prompt=toBeAsked,
                    temperature=0.5,
                    max_output_tokens=50000,
                    candidate_count=1

                )

                return completion.result
        def askai21(content , doubt ):
             ai21.api_key = 'API key        '
             a=ai21.Answer.execute(context=content, question=doubt)
             data={}
             data["answer"]=a.answer
             data["valid"]=a.answerInContext
             return data
        

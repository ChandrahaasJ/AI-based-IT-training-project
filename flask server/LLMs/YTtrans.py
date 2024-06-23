from youtube_transcript_api import YouTubeTranscriptApi as yta 
import google.generativeai as gemini
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
def askgem(question):
                apikey="AIzaSyCHAf6umJfrfEoyd4u_quG6BIKjGOFqud4"
                gemini.configure(api_key=apikey)
                model = gemini.GenerativeModel('gemini-pro')
                response = model.generate_content(question)
                print(response.text)
if(__name__=="__main__"):
        #x= "can you summarise this?"+transcribe("https://www.youtube.com/watch?v=pKd0Rpw7O48")
        #askgem(x)
        with open("out.txt","r") as fp:
            z=fp.read()
            y=str(z)
            askgem("summarize this file by omitting non-contextual information"+y)

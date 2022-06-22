# from unittest import TextTestResult
from youtube_transcript_api import *
from bottle import *
import re
from transformers import pipeline

app = Bottle()
# app_path = 

def get_youtube_ID(youtube_link):
    youtube_id_match_object = re.search(r'.*=(.*)$',youtube_link)
    youtube_id = youtube_id_match_object.groups(0)[0]
    return youtube_id


def get_transcript_text(youtube_id):
    text_dictionary_list = YouTubeTranscriptApi.get_transcript(youtube_id)
    transcript_text = ''
    for i in text_dictionary_list:
        new_line = i['text']
        
        transcript_text+=new_line + ' '
    

    transcript_file = open("transcript.txt","w")
    transcript_file.write(transcript_text)
    return transcript_text

def test_working(youtube_link):
    youtube_id = get_youtube_ID(youtube_link)
    text = get_transcript_text(youtube_id)



def get_summary(text):
    classifier = pipeline("summarization")
    summary_dict = classifier(text)

    print(summary_dict)
    summary = summary_dict[0]["summary_text"]
    print(summary)

    summary_file = open("summary.txt","w")
    summary_file.write(summary)
    return summary

    
@app.error(500)
def error500(error):
    return template('error500')
@app.route('/')
def home(filename = "frontend.html"):
    return static_file(filename, root='./')

@app.route('/',method='POST')
def summarize(file1 = "frontend.html"):
    youtube_link = request.forms.get('youtube_link')

    transcript_file = request.forms.get('file')

    youtube_id = get_youtube_ID(youtube_link)

    transcript_text = get_transcript_text(youtube_id)
    
    transcript_text = transcript_text[:1000]

    summary = get_summary(transcript_text)

    # return static_file(file1, root = './')
    return template('summary',summary_text=summary)


if __name__ == '__main__':
    run(app, host='localhost', port=8080, reloader=True)
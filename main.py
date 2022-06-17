# from unittest import TextTestResult
from youtube_transcript_api import *
from bottle import *
import re
from transformers import pipeline

app = Bottle()
# app_path = 
file1 = "frontend.html"

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/')
def home():
    return static_file(file1, root='./')

@app.post('/')
def summarize():
    youtube_link = request.forms.get('youtube_link')
    youtube_id_match_object = re.search(r'.*=(.*)$',youtube_link)
    youtube_id = youtube_id_match_object.groups(0)[0]
    print(youtube_id)
    try:
        text_dictionary_list = YouTubeTranscriptApi.get_transcript(youtube_id)
        transcript_text =""
        for i in text_dictionary_list:
            transcript_text+=' '+i['text']
        transcript_file = open("transcript.txt","w")
        transcript_file.write(transcript_text)

        classifier = pipeline("summarization")
        summary_dict = classifier(transcript_text)

        print(summary_dict)
        summary = summary_dict[0]["summary_text"]
        print(summary)

        summary_file = open("summary.txt","w")
        summary_file.write(summary)
    except TranscriptsDisabled:
        print(TranscriptsDisabled.CAUSE_MESSAGE)
    return static_file(file1, root = './')
        
@error(500)
def error500(error):
    return static_file(file1, root='./')




    # print(text_dictionary_list)
    # print(transcript_text) 


run(app, host='localhost', port=8080, reloader=True)
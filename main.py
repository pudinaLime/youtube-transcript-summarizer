from youtube_transcript_api import *
from bottle import *
import re


app = Bottle()
# app_path = 


@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/')
def home(filename = "frontend.html"):
    return static_file(filename, root='./')

@app.post('/summarize')
def summarize(file1 = "frontend.html"):
    youtube_link = request.forms.get('youtube_link')
    youtube_id_match_object = re.search("=\w*")
    youtube_id = youtube_id_match_object.group()[1:]
    text_dictionary = YouTubeTranscriptApi.get_transcript(youtube_id)
    print(text_dictionary)
    return static_file(file1, root = './')


run(app, host='localhost', port=8080, reloader=True)
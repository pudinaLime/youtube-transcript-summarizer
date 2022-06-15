from youtube_transcript_api import *
import re

# youtube_link = "https://www.youtube.com/watch?v=YZPC0j-f2tU"
youtube_link = "https://www.youtube.com/watch?v=eBSeCp__xhI"
youtube_id_match_object = re.search(r'.*=(.*)$',youtube_link)
youtube_id = youtube_id_match_object.groups(0)[0]
print(youtube_id)
# youtube_id ="eBSeCp__xhI"
text_dictionary_list = YouTubeTranscriptApi.get_transcript(youtube_id)
print(text_dictionary_list)
# print(YouTubeTranscriptApi.list_transcripts(youtube_id))
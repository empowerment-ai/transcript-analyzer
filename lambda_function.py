import json
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    tx =YouTubeTranscriptApi.get_transcript(video_id)
   
    outtxt =''
    for i in tx:
      blurb = (i['text'])
      outtxt += f" {blurb} \n"
     

    return outtxt

def lambda_handler(event, context):
    video_id = event['queryStringParameters']['video_id']
    transcript = get_transcript(video_id)
    #transcript = 'Hello World'
    return {
        'statusCode': 200,
        'body': json.dumps({"transcript_text": transcript})
    }
    

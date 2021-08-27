import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from conf import IMAGES_DIR
from apiclient.http import MediaFileUpload
import random
import sys
import time

from apiclient.discovery import build
from apiclient.errors import HttpError
from apiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow


def post_video(name, director, year):
    credentials = None

    if os.path.exists('token.pickle'):
        print('Loading Credentials From File...')
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)

    # If there are no valid credentials available, then either refresh the token or log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            print('Refreshing Access Token...')
            credentials.refresh(Request())
        else:
            print('Fetching New Tokens...')
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets.json',
                scope=['https://www.googleapis.com/auth/youtube.upload'])

            flow.run_local_server(port=8080,
                                  prompt='consent',
                                  authorization_prompt_message='')
            credentials = flow.credentials

            # Save the credentials for the next run
            with open('token.pickle', 'wb') as f:
                print('Saving Credentials for Future Use...')
                pickle.dump(credentials, f)

    body = dict(snippet=dict(
        title=f"{name} - ({year}) Speedy Movie Review",
        description=
        f"Today's review is about {name}, which is a {year} movie directed by {director}. I hope you enjoy the video. Stay great.",
        tags=f"{name} Movie Review",
        categoryId='22'),
                status=dict(privacyStatus='public'))

    youtube = build("youtube", 'v3', credentials=credentials)
    video_file = os.path.join(IMAGES_DIR, 'final_video.mp4')
    insert_request = youtube.videos().insert(part=''.join(body.keys()),
                                             body=body,
                                             media_body=MediaFileUpload(
                                                 video_file,
                                                 chunksize=-1,
                                                 resumable=True))
    response = insert_request.execute()


post_video('NOME', 'DIRETOR', 'ANO')

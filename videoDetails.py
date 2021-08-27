import os
from googleapiclient.http import MediaFileUpload
from conf import IMAGES_DIR


class Video:
    movietxt = open('MovieData.txt', 'r').read()
    movie_splited = movietxt.split(',')
    description = f"""Today's review is about {movie_splited[0]}, which is a {movie_splited[1]} 
    movie directed by {movie_splited[2]}. I hope you enjoy the video. Stay great."""
    category = "1"
    keywords = "Review"
    privacyStatus = "private"

    def getFileName(self, type):
        for file in os.listdir(IMAGES_DIR):
            if type == "final_video" and file.split(".", 1)[1] != "jpg":
                return file
                break
            elif type == "1" and file.split(".", 1)[1] != "mp4":
                return file
                break

    def insertThumbnail(self, youtube, videoId):
        thumnailPath = os.path.join(IMAGES_DIR, '1.jpg')

        request = youtube.thumbnails().set(
            videoId=videoId, media_body=MediaFileUpload(thumnailPath))
        response = request.execute()
        print(response)
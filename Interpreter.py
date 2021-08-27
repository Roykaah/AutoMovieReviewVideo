from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS, ROBOT_DIR, IMAGES_DIR
from moviepy.editor import *
from moviepy.audio.fx.all import volumex
from PIL import Image
from AudioMaker import cria_salva_audio
from Get_Movie_Data import dados_do_ultimo_filme_assistido
from download_google_images import download_images
import time
from gambiarram_image_sequence import cria_video


def make_robot_messages():
    dados = dados_do_ultimo_filme_assistido()
    dados['director'] = 'Park chan wook'
    frases = [
        f"Welcome, Today's review will be about, {dados['title']}",
        f"It's a {dados['year']} piece of art, Directed by {dados['director']}",
        f"And I'm giving this movie a {int(dados['my_rating'])} out of 10, see you later"
    ]
    for i in range(0, 3):
        cria_salva_audio(frases[i], i)
    return dados


#nine lives is almost as bad as you think. At least it does not pretend that it is something better than it is. The cgi is absolutely amazing


def video_from_1img(img_name):
    path = os.path.join(IMAGES_DIR, f'{img_name}.jpg')
    frame = ImageClip(path)
    frame = frame.resize((720, 1080))
    frame = frame.img
    clip = ImageSequenceClip([frame], fps=1 / 4)
    return clip


#output_welcome_video = os.path.join(IMAGES_DIR, 'Welcome.mp4')
#output_director_video = os.path.join(IMAGES_DIR, 'Director.mp4')
output_final_video = os.path.join(IMAGES_DIR, 'final_video.mp4')
#output_end_video = os.path.join(IMAGES_DIR, 'rating.mp4')
dados = make_robot_messages()
#with open('MovieData.txt', 'w') as arq:
#   arq.write(f"{dados['title']},{dados['year']},{dados['director']}")
movie_query = f"{dados['title']} {dados['year']}"
#download_images(movie_query, 37)
#jdownload_images(dados['director'], 1)
time.sleep(1)

welcome_audio_path = os.path.join(ROBOT_DIR, '0.mp3')
welcome_audio = AudioFileClip(welcome_audio_path)
welcome_video = video_from_1img('1')
welcome_video = welcome_video.set_audio(welcome_audio)
welcome_video = welcome_video.subclip(0, welcome_audio.duration)
#welcome_video.write_videofile(output_welcome_video)

director_audio_path = os.path.join(ROBOT_DIR, '1.mp3')
director_audio = AudioFileClip(director_audio_path)
director_video = video_from_1img('0')
director_video = director_video.set_audio(director_audio)
director_video = director_video.subclip(0, director_audio.duration)
#director_video.write_videofile(output_director_video)

end_audio_path = os.path.join(ROBOT_DIR, '2.mp3')
end_audio = AudioFileClip(end_audio_path)
rating = int(dados['my_rating'])
end_video = video_from_1img(f'{rating}star')
end_video = end_video.set_audio(end_audio)
end_video = end_video.subclip(0, end_audio.duration)
#end_video.write_videofile(output_end_video)

recorded_audio_path = os.path.join(SAMPLE_INPUTS, "aud.mp3")
recorded_audio = AudioFileClip(recorded_audio_path)
videoimages_needed = int(recorded_audio.duration / 4 + 1)

mine = cria_video(videoimages_needed)
mine = mine.set_audio(recorded_audio)
cria_video(videoimages_needed)
final_video = concatenate_videoclips(
    [welcome_video, director_video, mine, end_video])
final_video.write_videofile(output_final_video,
                            codec='libx264',
                            audio_codec="aac")
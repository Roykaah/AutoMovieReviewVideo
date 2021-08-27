from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS, ROBOT_DIR, IMAGES_DIR
from moviepy.editor import *
from moviepy.audio.fx.all import volumex
from PIL import Image
from AudioMaker import cria_salva_audio
from Get_Movie_Data import dados_do_ultimo_filme_assistido
from download_google_images import download_images
import time


def video_from_1img(img_name):
    path = os.path.join(IMAGES_DIR, f'{img_name}.jpg')
    frame = ImageClip(path)
    frame = frame.resize((720, 1080))
    frame = frame.img
    clip = ImageSequenceClip([frame], fps=1 / 4)
    return clip


def cria_video(n):
    t0 = video_from_1img('2')
    clip = concatenate_videoclips([t0])
    if n > 1:
        t1 = video_from_1img('2')
        clip = concatenate_videoclips([clip, t1])
    if n > 2:
        t2 = video_from_1img('3')
        clip = concatenate_videoclips([clip, t2])
    if n > 3:
        t3 = video_from_1img('4')
        clip = concatenate_videoclips([clip, t3])
    if n > 4:
        t4 = video_from_1img('5')
        clip = concatenate_videoclips([clip, t4])
    if n > 5:
        t5 = video_from_1img('6')
        clip = concatenate_videoclips([clip, t5])
    if n > 6:
        t6 = video_from_1img('7')
        clip = concatenate_videoclips([clip, t6])
    if n > 7:
        t7 = video_from_1img('8')
        clip = concatenate_videoclips([clip, t7])
    if n > 8:
        t8 = video_from_1img('9')
        clip = concatenate_videoclips([clip, t8])
    if n > 9:
        t9 = video_from_1img('10')
        clip = concatenate_videoclips([clip, t9])
    if n > 10:
        t10 = video_from_1img('11')
        clip = concatenate_videoclips([clip, t10])
    if n > 11:
        t11 = video_from_1img('12')
        clip = concatenate_videoclips([clip, t11])
    if n > 12:
        t12 = video_from_1img('13')
        clip = concatenate_videoclips([clip, t12])
    if n > 13:
        t13 = video_from_1img('14')
        clip = concatenate_videoclips([clip, t13])
    if n > 14:
        t14 = video_from_1img('15')
        clip = concatenate_videoclips([clip, t14])
    if n > 15:
        t15 = video_from_1img('16')
        clip = concatenate_videoclips([clip, t15])
    if n > 16:
        t16 = video_from_1img('17')
        clip = concatenate_videoclips([clip, t16])
    if n > 17:
        t17 = video_from_1img('18')
        clip = concatenate_videoclips([clip, t17])
    if n > 18:
        t18 = video_from_1img('19')
        clip = concatenate_videoclips([clip, t18])
    if n > 19:
        t19 = video_from_1img('20')
        clip = concatenate_videoclips([clip, t19])
    if n > 20:
        t20 = video_from_1img('21')
        clip = concatenate_videoclips([clip, t20])
    if n > 21:
        t21 = video_from_1img('22')
        clip = concatenate_videoclips([clip, t21])
    if n > 22:
        t22 = video_from_1img('23')
        clip = concatenate_videoclips([clip, t22])
    if n > 23:
        t23 = video_from_1img('25')
        clip = concatenate_videoclips([clip, t23])
    if n > 24:
        t24 = video_from_1img('26')
        clip = concatenate_videoclips([clip, t24])
    if n > 25:
        t25 = video_from_1img('27')
        clip = concatenate_videoclips([clip, t25])
    if n > 26:
        t26 = video_from_1img('28')
        clip = concatenate_videoclips([clip, t26])
    if n > 27:
        t27 = video_from_1img('29')
        clip = concatenate_videoclips([clip, t27])
    if n > 28:
        t28 = video_from_1img('30')
        clip = concatenate_videoclips([clip, t28])
    if n > 29:
        t29 = video_from_1img('31')
        clip = concatenate_videoclips([clip, t29])
    if n > 30:
        t30 = video_from_1img('32')
        clip = concatenate_videoclips([clip, t30])
    if n > 31:
        t31 = video_from_1img('33')
        clip = concatenate_videoclips([clip, t31])
    if n > 32:
        t32 = video_from_1img('34')
        clip = concatenate_videoclips([clip, t32])
    if n > 33:
        t33 = video_from_1img('35')
        clip = concatenate_videoclips([clip, t33])
    if n > 34:
        t34 = video_from_1img('36')
        clip = concatenate_videoclips([clip, t34])
    if n > 35:
        t35 = video_from_1img('37')
        clip = concatenate_videoclips([clip, t35])
    return clip

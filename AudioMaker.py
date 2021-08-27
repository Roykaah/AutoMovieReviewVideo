from conf import ROBOT_DIR
import voicerss_tts as RSS
import os


def cria_salva_audio(Frase, num):
    robot_path = os.path.join(ROBOT_DIR, f'{num}.mp3')
    api_key = '5afb00f644714461be278bb0b3f5a62e'
    params = {
        'key': f'{api_key}',
        'src': f'{Frase}',
        'hl': 'en-gb',
        'v': num,
        'r': '0',
        'c': 'mp3',
        'f': '48khz_16bit_stereo'
    }
    result = RSS.__request(params)
    audio = result['response']
    newFile = open(robot_path, "wb")
    newFile.write(audio)
    newFile.close()


cria_salva_audio(
    """Welcome, Today's review will be about, Nine Lives,
        It's a 2016 piece of art, Directed by Gary,
        And I'm giving this movie a 4 outta 10. Goodbye, see you later, love you""",
    'Nancy')

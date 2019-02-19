import tempfile
import sh
import os


def speech(text, options):
    lang_options = ()
    if options.lang:
        lang_options = (options.lang, )
    _, fname = tempfile.mkstemp(suffix=".mp3")
    from gtts import gTTS
    tts = gTTS(text, *lang_options)
    tts.save(fname)
    sh.mpv(fname)
    os.unlink(fname)

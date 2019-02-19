import sh


def speech(text, options):
    lang_options = ()
    if options.lang:
        lang_options = ("--language", options.lang)
    sh.festival(*lang_options, "--tts", _in=text)

import sh


def speech(text, options):
    lang_options = ()
    if options.lang:
        lang_options = ("-v", options.lang)
    sh.ekho(*lang_options, "-f", "-", _in=text)

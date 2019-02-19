#!/usr/bin/python

import argparse
import sh
import time


def speech(text, tts, lang):
    try:
        s2s = __import__("s2s.engines." + options.tts)
        getattr(s2s.engines, options.tts).speech(text, options) 
    except Exception as e:
        print("Failed to play: " + repr(e))


def paste():
    try:
        return sh.xclip("-selection", "p", '-o').stdout.decode("utf-8")
    except:
        return None


def watcher(options):
    t = paste()

    while True:
        t_new = paste()
        if t_new != t:
            if t_new:
                print("New text detected:", t_new)
                speech(t_new, options.tts, options.lang)
            t = t_new

        time.sleep(0.1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Selection to Speech')
    parser.add_argument('-w', '--watcher', action="store_true", default=False,
                        help='Watcher mode, run in the background and read everything selected.')
    parser.add_argument('-t', '--tts', nargs='?', default="google",
                        help='Specify TTS engine to use. Possible values: google (default), ekho, festival')
    parser.add_argument('-l', '--lang', nargs='?', default=None,
                        help='Specify language.')
    options = parser.parse_args()

    if options.watcher:
        watcher(options)
    else:
        speech(paste(), options.tts, options.lang)

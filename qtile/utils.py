from os.path import expanduser
from libqtile.lazy import lazy


HOME_DIR = expanduser("~")
TERMINALS = []
TERMINALS.append("alacritty")
TERMINALS.append("xterm")
BROWSERS = []
BROWSERS.append("firefox")
BROWSERS.append("google-chrome-stable")
BROWSERS.append("librewolf")
TORRENT_CLIENTS = []
TORRENT_CLIENTS.append("transmission-gtk")
FILE_MANAGERS = []
FILE_MANAGERS.append("pcmanfm")
FONTS = []
FONTS.append("Source Code Pro Bold")
FONTS.append("Fira Code Bold")
APP_LAUNCHERS = []
APP_LAUNCHERS.append(f"dmenu_run -p '⮞ ' -fn '{FONTS[0]}'")
TEXT_EDITORS = []
TEXT_EDITORS.append("code")
BACKLIGHT_NAME = "intel_backlight"


def read_props(filepath, sep='='):
    props = {}
    with open(filepath, "rt") as f:
        for line in f:
            l = line.strip()
            if l:
                key_value = l.split(sep)
                key = key_value[0].strip()
                value = sep.join(key_value[1:]).strip().strip('"')
                props[key] = value
    return props


@lazy.function
def float_to_front(qtile):
    for group in qtile.groups:
        for window in group.windows:
            if window.floating:
                window.cmd_bring_to_front()

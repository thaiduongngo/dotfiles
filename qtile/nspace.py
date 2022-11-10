from os.path import expanduser
from libqtile.lazy import lazy


HOME_DIR = expanduser("~")
# Font settings
FONTS = [
    "Source Code Pro Bold",
    "Fira Code Bold"
]
FONT_SIZE = 12
FONT_SIZE_SMALL = 11
FONT_ICON_SIZE = 24
FONT_ICON_BIG_SIZE = 30
# App settings
TERMINALS = ["alacritty", "xterm"]
BROWSERS = ["firefox", "google-chrome-stable", "brave"]
TORRENT_CLIENTS = ["transmission-gtk"]
FILE_MANAGERS = ["pcmanfm"]
APP_LAUNCHERS = [f"dmenu_run -p '❯ ' -fn '{FONTS[1]}'"]
TEXT_EDITORS = ["code", "emacs"]
IDES = ["pycharm"]
# Other settings
BACKLIGHT_NAME = "intel_backlight"
BAR_HEIGHT = 28
WN_MARGIN = 5
WN_BORDER_WIDTH = 3
TEXT_PADDING_SIZE = 3
OPACITY = 0.9


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

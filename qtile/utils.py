from os.path import expanduser
from subprocess import Popen
from libqtile import hook
from libqtile.lazy import lazy


MOD = "mod4"
SHIFT = "shift"
CTRL = "control"
RETURN = "Return"
HOME = expanduser("~")

WORKSPACES = (
    ("1", "1", "monadwide"),
    ("2", "2", "monadtall"),
    ("3", "3", "monadtall"),
    ("4", "4", "monadtall"),
    ("5", "5", "monadtall"),
    ("6", "6", "monadtall"),
    ("7", "7", "monadtall"),
    ("8", "8", "monadtall"),
    ("9", "9", "monadtall"),
    ("10", "0", "monadtall"),
)

M_BTNS = []
M_BTNS.append("Button1")
M_BTNS.append("Button2")
M_BTNS.append("Button3")

TERMINALS = []
TERMINALS.append("alacritty")
TERMINALS.append("xterm")

BROWSERS = []
BROWSERS.append("firefox")
BROWSERS.append("google-chrome-stable")
BROWSERS.append("librewolf")

TORRENT_CLIENT = "transmission-gtk"

FILE_MANAGERS = []
FILE_MANAGERS.append("pcmanfm")

FONTS = []
FONTS.append("Roboto Mono")
FONTS.append("Source Code Pro")
FONTS.append("Fira Code")
FONT = FONTS[0]
FONT_SIZE = 13
FONT_SIZE_SMALL = 11

APP_LAUNCHER = f"dmenu_run -p '⮞ ' -fn '{FONT}'"
BACKLIGHT_NAME = "intel_backlight"

TEXT_EDITORS = []
TEXT_EDITORS.append("code")
TEXT_EDITOR = TEXT_EDITORS[0]

# Colors setting


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


COLORS = read_props(f"{HOME}/.config/qtile/colors.properties")

THIS_CURRENT = COLORS["maroon"]
ACTIVE = COLORS["iceblue"]
INACTIVE = COLORS["charcoalgray"]
HIGHLIGHT = [COLORS["lemonyellow"], COLORS["comicbookyellow"], ]
URGENT = COLORS["scarletred"]
FOREGROUND = COLORS["iceblue"]
FOREGROUND1 = COLORS["pastelred"]
FOREGROUND2 = COLORS["cetaceanblue"]
BACKGROUND = [COLORS["cetaceanblue"], COLORS["midnightblue"], ]
FOCUS = COLORS["grassgreen"]
NORMAL = COLORS["iceblue"]

WN_MARGIN = 4
WN_BORDER_WIDTH = 2
PADDING_SIZE = 3
OPACITY = 0.86


@ hook.subscribe.startup
def autostart():
    Popen([HOME + '/.config/qtile/autostart.sh'])


@ hook.subscribe.startup_once
def autostart_once():
    Popen([HOME + '/.config/qtile/autostart_once.sh'])


@lazy.function
def float_to_front(qtile):
    for group in qtile.groups:
        for window in group.windows:
            if window.floating:
                window.cmd_bring_to_front()

from libqtile.config import Key, KeyChord, Click, Drag
from libqtile.lazy import lazy
from nspace import TERMINALS, TEXT_EDITORS, TORRENT_CLIENTS, BROWSERS, FILE_MANAGERS, APP_LAUNCHERS, IDES


M_BTNS = ["Button1", "Button2", "Button3"]
MOD = "mod4"
SHIFT = "shift"
CTRL = "control"
RETURN = "Return"
NULL_KEY = []


@lazy.function
def float_to_front(qtile):
    for group in qtile.groups:
        for window in group.windows:
            if window.floating:
                window.cmd_bring_to_front()


MOUSE_EVENTS = [
    Drag([MOD], M_BTNS[2], lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([MOD], M_BTNS[0], lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([MOD], M_BTNS[1], lazy.window.bring_to_front()),
]

KEY_CHORD_MM = [
    Key(NULL_KEY, "x", lazy.spawn(FILE_MANAGERS[0]), ),
    Key(NULL_KEY, "v", lazy.spawn(TEXT_EDITORS[0]), ),
    Key(NULL_KEY, "e", lazy.spawn(TEXT_EDITORS[1]), ),
    Key(NULL_KEY, "f", lazy.spawn(BROWSERS[0]), ),
    Key(NULL_KEY, "g", lazy.spawn(BROWSERS[1]), ),
    Key(NULL_KEY, "b", lazy.spawn(BROWSERS[2]), ),
    Key(NULL_KEY, "t", lazy.spawn(TORRENT_CLIENTS[0]), ),
    Key(NULL_KEY, "y", lazy.spawn(IDES[0]), ),
]

DEFAULT_KEYS = [
    # Switch between windows
    Key([MOD], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([MOD], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([MOD], "j", lazy.layout.down(), desc="Move focus down"),
    Key([MOD], "k", lazy.layout.up(), desc="Move focus up"),
    Key([MOD], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([MOD, SHIFT], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([MOD, SHIFT], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([MOD, SHIFT], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([MOD, SHIFT], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([MOD, CTRL], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([MOD, CTRL], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([MOD, CTRL], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([MOD, CTRL], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([MOD], "n", lazy.layout.normalize(),
               desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [MOD, SHIFT],
        RETURN,
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Toggle between different layouts as defined below
    Key([MOD], "Tab", lazy.next_layout(),
               desc="Toggle between layouts"),
    Key([MOD], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([MOD, CTRL], "r", lazy.reload_config(), desc="Reload the config"),
    Key([MOD, CTRL], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Sound
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("amixer set 'Master' 5%+")
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("amixer set 'Master' 5%-")
    ),
    # Monitor brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight + 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight - 5")),
    # More keybindings
    Key([MOD], RETURN, lazy.spawn(TERMINALS[0]), ),
    Key([MOD, CTRL], RETURN, lazy.spawn(TERMINALS[1]), ),
    Key([MOD], "r", lazy.spawn(APP_LAUNCHERS[0]), ),
    Key([MOD], "p", lazy.spawncmd(), ),
    Key([MOD, SHIFT], "f", float_to_front),
    Key(
        [MOD], "f",
        lazy.window.toggle_floating(),
        desc="Toggle floating",
    ),
    Key(
        [MOD, CTRL], "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen",
    ),
    Key([MOD], "x", lazy.spawn(FILE_MANAGERS[0]), ),
    Key([MOD, CTRL], "s", lazy.spawn(f"{TERMINALS[0]} -e shutdown now"), ),
    Key([MOD], "g", lazy.ungrab_all_chords(), ),
    # KeyChord: M-m
    KeyChord([MOD], "m", KEY_CHORD_MM,),
]


KEYS = DEFAULT_KEYS

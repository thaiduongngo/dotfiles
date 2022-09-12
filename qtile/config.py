import os
import subprocess
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.dgroups import simple_key_binder


def load_props(filepath, sep='='):
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


MOD = "mod4"
SHIFT = "shift"
CTRL = "control"
RETURN = "Return"

HOME = os.path.expanduser('~')

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
BROWSERS.append("brave")

TORRENT_CLIENT = "transmission-gtk"

FILE_MANAGERS = []
FILE_MANAGERS.append("pcmanfm")

FONTS = []
FONTS.append("Source Code Pro")
FONTS.append("Fira Code")
FONTS.append("Roboto Mono")
FONT = FONTS[0]
FONT_SIZE = 13
FONT_SIZE_SMALL = 11

APP_LAUNCHER = f"dmenu_run -p '❯ ' -fn '{FONT}'"
BACKLIGHT_NAME = "intel_backlight"

TEXT_EDITORS = []
TEXT_EDITORS.append("code")
TEXT_EDITOR = TEXT_EDITORS[0]


COLORS = load_props(f"{HOME}/.config/qtile/colors.properties")

THIS_CURRENT = COLORS["navyblue"]
ACTIVE = COLORS["comicbookyellow"]
INACTIVE = COLORS["charcoalgray"]
HIGHLIGHT = [COLORS["lemonyellow"], COLORS["comicbookyellow"], ]
URGENT = COLORS["scarletred"]
FOREGROUND = COLORS["iceblue"]
FOREGROUND2 = COLORS["cetaceanblue"]
BACKGROUND = [COLORS["cetaceanblue"], COLORS["midnightblue"], ]
FOCUS = COLORS["grassgreen"]
NORMAL = COLORS["iceblue"]

WN_MARGIN = 4
PADDING_SIZE = 2
OPACITY = 0.85

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
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
    Key([MOD, SHIFT], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([MOD, SHIFT], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([MOD, CTRL], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([MOD, CTRL], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([MOD, CTRL], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([MOD, CTRL], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([MOD], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
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
    Key([MOD], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([MOD], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([MOD, CTRL], "r", lazy.reload_config(), desc="Reload the config"),
    Key([MOD, CTRL], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([MOD], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([MOD], "i", lazy.spawn(BROWSERS[0]), desc="Spawn browser"),
    Key([MOD], "g", lazy.spawn(BROWSERS[1]), desc="Spawn browser"),
    Key([MOD], "b", lazy.spawn(BROWSERS[2]), desc="Spawn browser"),
    Key([MOD], "t", lazy.spawn(TORRENT_CLIENT), desc="Spawn torrent client"),
    Key([MOD], "m", lazy.spawn(FILE_MANAGERS[0]), desc="Spawn files manager"),
    Key([MOD], "x", lazy.spawn(TEXT_EDITOR), desc="Spawn editor"),
    # Sound
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "amixer -c 0 sset Master 1- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "amixer -c 0 sset Master 1+ unmute")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight + 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight - 5")),
    Key([MOD], RETURN, lazy.spawn(TERMINALS[0]), desc="Launch terminal"),
    Key([MOD, CTRL], RETURN, lazy.spawn(TERMINALS[1]), desc="Launch terminal"),
    Key([MOD], "r", lazy.spawn(APP_LAUNCHER), desc="Spawn app launcher"),
]

groups = [Group("1SY", "ratiotile"),
          Group("2WS", "monadtall"),
          Group("3WS", "monadtall"),
          Group("4DE", "monadtall"),
          Group("5WW", "monadtall"),
          Group("6WW", "monadtall"),
          Group("7CH", "monadtall"),
          Group("8CH", "monadtall"),
          Group("9OT", "max"), ]
i = 1
for g in groups:
    keys.extend(
        [
            Key(
                [MOD],
                str(i),
                lazy.group[g.name].toscreen(),
                desc=f"Switch to group {format(g.name)}",
            ),
            Key(
                [MOD, SHIFT],
                str(i),
                lazy.window.togroup(g.name, switch_group=True),
                desc=f"Switch to & move focused window to group {g.name}",
            ),
        ]
    )
    i = i + 1

LAYOUT_STYLE = {"border_width": 3,
                "margin": WN_MARGIN,
                "border_focus": FOCUS,
                "border_normal": NORMAL,
                }

layouts = [
    layout.RatioTile(**LAYOUT_STYLE),
    layout.MonadTall(**LAYOUT_STYLE),
    layout.MonadWide(**LAYOUT_STYLE),
    layout.Max(**LAYOUT_STYLE),
    layout.Floating(**LAYOUT_STYLE),
    # layout.Columns(**LAYOUT_STYLE),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    # layout.Floating(),
]

widget_defaults = dict(
    font=FONT,
    fontsize=FONT_SIZE,
    padding=PADDING_SIZE,
    background=BACKGROUND,
    foreground=FOREGROUND,
)

extension_defaults = widget_defaults.copy()

sep_big = widget.Sep(
    linewidth=0,
    padding=4,
)

sep = widget.Sep(
    linewidth=0,
    padding=PADDING_SIZE,
)


def create_widgets():
    widgets = [
        sep,
        widget.Image(
            filename="~/.config/qtile/icons/arch-round1.png",
            scale="False",
            mouse_callbacks={
                M_BTNS[0]: lambda: qtile.cmd_spawn(TERMINALS[0])}),
        sep_big,
        widget.GroupBox(
            padding=PADDING_SIZE,
            active=ACTIVE,
            inactive=INACTIVE,
            highlight_color=HIGHLIGHT,
            block_highlight_text_color=FOREGROUND2,
            highlight_method="line",
            rounded=False,
            this_current_screen_border=THIS_CURRENT,
            this_screen_border=THIS_CURRENT,
            urgent_alert_method="line",
            urgent_text=URGENT,
            urgent_border=URGENT,
        ),
        sep,
        # widget.Prompt(),
        widget.WindowName(
            # foreground=FOREGROUND2,
            # background=HIGHLIGHT,
            padding=10,
            empty_group_string="<Empty>"),
        # widget.Systray(),
        sep_big,
        widget.CurrentLayoutIcon(scale=0.7, ),
        sep,
        widget.Net(fmt="❯ N:{}",
                   interface="wlp5s0",
                   padding=PADDING_SIZE),
        sep,
        widget.Volume(fmt="❯ V:{}",
                      padding=PADDING_SIZE,),
        sep,
        widget.Backlight(fmt="❯ D:{}",
                         padding=PADDING_SIZE,
                         backlight_name=BACKLIGHT_NAME, ),
        sep,
        # widget.Clock(format="%Y-%m-%d %a %I:%M %p",
        #              padding=PADDING_SIZE, ),
        widget.Clock(format="❯ %Y-%m-%d %I:%M %p",
                     padding=PADDING_SIZE, ),
        sep,
    ]
    return widgets


def create_screen():
    screen = Screen(
        top=bar.Bar(
            create_widgets(),
            30,
            opacity=OPACITY,
        ),
    )
    return screen


screens = [create_screen(), ]

# Drag floating layouts.
mouse = [
    Drag([MOD], M_BTNS[0], lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([MOD], M_BTNS[2], lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([MOD], M_BTNS[1], lazy.window.bring_to_front()),
]

dgroups_key_binder = simple_key_binder(MOD)
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = True
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    auto_float_types="dialog",
)

auto_fullscreen = True
focus_on_window_activation = "focus"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


@ hook.subscribe.startup
def autostart():
    subprocess.Popen([HOME + '/.config/qtile/autostart.sh'])


@ hook.subscribe.startup_once
def autostart_once():
    subprocess.Popen([HOME + '/.config/qtile/autostart_once.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

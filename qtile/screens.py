from libqtile import bar, layout, widget, qtile
from libqtile.config import Group, Key, Screen
from libqtile.lazy import lazy
from keys import MOD, SHIFT, M_BTNS
from utils import FONTS, HOME_DIR, BACKLIGHT_NAME, TERMINALS, read_props

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
# Colors setting
COLORS = read_props(f"{HOME_DIR}/.config/qtile/colors.properties")
ACTIVE = COLORS["iceblue"]
INACTIVE = "4c566a"
THIS_CURRENT = "2e3440"
HIGHLIGHT = [COLORS["iceblue"], "d8dee9", ]
URGENT = COLORS["scarletred"]
BACKGROUND = ["2e3440", "3b4252", ]
FOREGROUND = COLORS["iceblue"]
FOREGROUND1 = COLORS["pastelred"]
FOREGROUND2 = "2e3440"
FOCUS = COLORS["grassgreen"]
NORMAL = COLORS["iceblue"]
WN_MARGIN = 4
WN_BORDER_WIDTH = 2
PADDING_SIZE = 3
OPACITY = 0.91
FONT_SIZE = 13
FONT_SIZE_SMALL = 11


def create_groups(ks):
    grps = []
    for ws in WORKSPACES:
        grps.append(Group(ws[0], layout=ws[2]))
        ks.extend(
            [
                Key(
                    [MOD],
                    ws[1],
                    lazy.group[ws[0]].toscreen(),
                ),
                Key(
                    [MOD, SHIFT],
                    ws[1],
                    lazy.window.togroup(ws[0], switch_group=True),
                ),
            ]
        )
    return grps, ks


LAYOUT_STYLE = {"border_width": WN_BORDER_WIDTH,
                "margin": WN_MARGIN,
                "border_focus": FOCUS,
                "border_normal": NORMAL,
                }


def create_layouts():
    return [
        layout.MonadTall(**LAYOUT_STYLE),
        layout.MonadWide(**LAYOUT_STYLE),
        layout.RatioTile(**LAYOUT_STYLE),
        layout.Max(**LAYOUT_STYLE),
        layout.Floating(**LAYOUT_STYLE),
        layout.Matrix(**LAYOUT_STYLE),
        # layout.TreeTab(**LAYOUT_STYLE),
        # layout.Columns(**LAYOUT_STYLE),
        # Try more layouts by unleashing below layouts.
        # layout.Stack(num_stacks=2),
        # layout.Bsp(),
        # layout.MonadTall(),
        # layout.MonadWide(),
        # layout.RatioTile(),
        # layout.Tile(),
        # layout.TreeTab(),
        # layout.VerticalTile(),
        # layout.Zoomy(),
    ]


WIDGET_DEFAULTS = dict(
    font=FONTS[0],
    fontsize=FONT_SIZE,
    padding=PADDING_SIZE,
    background=BACKGROUND,
    foreground=FOREGROUND,
)


sep_big = widget.Sep(
    linewidth=0,
    padding=6,
)

sep = widget.Sep(
    linewidth=0,
    padding=3,
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
        widget.Prompt(fmt="⮞ {}"),
        widget.WindowName(fmt="⮞ {}",
                          padding=10,
                          empty_group_string="<Empty>"),
        sep_big,
        widget.CurrentLayoutIcon(scale=0.7, ),
        sep,
        widget.StatusNotifier(padding=PADDING_SIZE, ),
        sep,
        widget.Volume(fmt="{}",
                      padding=PADDING_SIZE, ),
        sep,
        widget.Backlight(fmt="{}",
                         padding=PADDING_SIZE,
                         backlight_name=BACKLIGHT_NAME, ),
        sep,
        widget.Battery(fmt="{}",
                       padding=PADDING_SIZE, ),
        sep,
        widget.Clock(format="%Y-%m-%d %I:%M %p",
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

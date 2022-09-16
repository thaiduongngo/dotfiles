from utils import FONTS, HOME_DIR, BACKLIGHT_NAME, TERMINALS, read_props
from keys import MOD, SHIFT, M_BTNS
from libqtile.lazy import lazy
from libqtile.config import Group, Key, Screen
from libqtile import bar, layout, widget, qtile

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
# Colors theme
THEME = read_props(f"{HOME_DIR}/.config/qtile/cpunk.properties")

WN_MARGIN = 4
WN_BORDER_WIDTH = 3
PADDING_SIZE = 3
OPACITY = 0.9
FONT_SIZE = 13
FONT_SIZE_SMALL = 11
ICON_SIZE = 31


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
                "border_focus": THEME["FOCUS"],
                "border_normal": THEME["NORMAL"],
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
        # layout.Tile(),
        # layout.TreeTab(),
        # layout.VerticalTile(),
        # layout.Zoomy(),
    ]


WIDGET_DEFAULTS = dict(
    font=FONTS[0],
    fontsize=FONT_SIZE,
    padding=PADDING_SIZE,
    background=[THEME["BACKGROUND1"], THEME["BACKGROUND2"]],
    foreground=THEME["FOREGROUND"],
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
        sep_big,
        widget.Image(
            filename="~/.config/qtile/icons/arch-round1.png",
            scale="False",
            mouse_callbacks={
                M_BTNS[0]: lambda: qtile.cmd_spawn(TERMINALS[0])}),
        sep_big,
        widget.GroupBox(
            padding=PADDING_SIZE,
            active=THEME["ACTIVE"],
            inactive=THEME["INACTIVE"],
            highlight_color=[THEME["HIGHLIGHT1"], THEME["HIGHLIGHT2"]],
            block_highlight_text_color=THEME["FOREGROUND2"],
            highlight_method="line",
            rounded=False,
            this_current_screen_border=THEME["THIS_CURRENT"],
            this_screen_border=THEME["THIS_CURRENT"],
            urgent_alert_method="line",
            urgent_text=THEME["URGENT"],
            urgent_border=THEME["URGENT"],
        ),
        sep_big,
        widget.Prompt(fmt="❯ {}"),
        widget.WindowName(fmt="❯ {}",
                          padding=6,
                          empty_group_string="<Empty>"),
        sep_big,
        widget.CurrentLayoutIcon(scale=0.66, ),
        sep,
        widget.StatusNotifier(padding=PADDING_SIZE, ),
        sep,
        widget.TextBox(text="&#xf028;", fontsize=ICON_SIZE,
                       foreground=THEME["HIGHLIGHT1"],),
        widget.Volume(
            padding=PADDING_SIZE, ),
        widget.TextBox(text="&#xf108;", fontsize=ICON_SIZE,
                       foreground=THEME["HIGHLIGHT1"],),
        widget.Backlight(padding=PADDING_SIZE,
                         backlight_name=BACKLIGHT_NAME, ),
        sep,
        widget.TextBox(text="&#xf240;", fontsize=ICON_SIZE,
                       foreground=THEME["HIGHLIGHT1"],),
        widget.Battery(padding=PADDING_SIZE, ),
        sep,
        widget.TextBox(text="&#xf133;", fontsize=ICON_SIZE,
                       foreground=THEME["HIGHLIGHT1"],),
        widget.Clock(format="%I:%M %p",
                     padding=PADDING_SIZE, ),
        # widget.Clock(format="%Y-%m-%d %I:%M %p",
        #              padding=PADDING_SIZE, ),
        sep_big,
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

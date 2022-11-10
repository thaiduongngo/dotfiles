
from libqtile.lazy import lazy
from libqtile.config import Group, Key, Screen
from libqtile import bar, layout, widget, qtile
from keys import M_BTNS
from nspace import FONTS, HOME_DIR, BACKLIGHT_NAME, TERMINALS, read_props
from nspace import BAR_HEIGHT, WN_MARGIN, WN_BORDER_WIDTH, FONT_SIZE, FONT_ICON_SIZE, TEXT_PADDING_SIZE, OPACITY, FONT_ICON_BIG_SIZE


# Colors theme
THEME = read_props(f"{HOME_DIR}/.config/qtile/cpunk.properties")

LAYOUT_STYLE = {"border_width": WN_BORDER_WIDTH,
                "margin": WN_MARGIN,
                "border_focus": THEME["FOCUS"],
                "border_normal": THEME["NORMAL"],
                }


def create_layouts():
    return [
        layout.MonadTall(**LAYOUT_STYLE),
        layout.MonadWide(**LAYOUT_STYLE),
        layout.Bsp(**LAYOUT_STYLE),
        layout.RatioTile(**LAYOUT_STYLE),
        layout.Max(**LAYOUT_STYLE),
        layout.Floating(**LAYOUT_STYLE),
        layout.Matrix(**LAYOUT_STYLE),
        # layout.TreeTab(**LAYOUT_STYLE),
        # layout.Columns(**LAYOUT_STYLE),
        # Try more layouts by unleashing below layouts.
        # layout.Stack(num_stacks=2),
        # layout.Tile(),
        layout.TreeTab(**LAYOUT_STYLE),
        # layout.VerticalTile(),
        # layout.Zoomy(),
    ]


WIDGET_DEFAULTS = dict(
    font=FONTS[0],
    fontsize=FONT_SIZE,
    padding=TEXT_PADDING_SIZE,
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

v_sep = widget.TextBox(
    text="&#xeb10;",
    foreground=THEME["INACTIVE"]
)


def create_widgets():
    widgets = [
        sep_big,
        widget.TextBox(
            text="&#xf303;",
            foreground=THEME["HIGHLIGHT1"],
            fontsize=FONT_ICON_BIG_SIZE,
            mouse_callbacks={M_BTNS[0]: lambda: qtile.cmd_spawn(
                f"{TERMINALS[0]} --class alacrittysysinfo --title sysinfo -e bpytop")}
        ),
        sep,
        widget.TextBox(
            text="&#xe795;",
            foreground=THEME["HIGHLIGHT1"],
            fontsize=FONT_ICON_BIG_SIZE,
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(TERMINALS[0])},
        ),
        v_sep,
        widget.GroupBox(
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
            hide_unused=True,
            disable_drag=True,
        ),
        v_sep,
        widget.CurrentLayoutIcon(scale=0.7),
        sep,
        widget.Prompt(fmt="❯ {}"),
        widget.WindowName(padding=6,
                          empty_group_string="<Empty>"),
        widget.TextBox(
            text="&#xfaa8;",
            fontsize=FONT_ICON_SIZE,
            foreground=THEME["HIGHLIGHT1"],),
        widget.Net(
            format="{down}↓{up}↑",),
        v_sep,
        widget.TextBox(text="&#xfa7d;", fontsize=FONT_ICON_SIZE,
                       foreground=THEME["HIGHLIGHT1"],),
        widget.Volume(),
        v_sep,
        widget.TextBox(text="&#xf5df;", fontsize=FONT_ICON_SIZE,
                       foreground=THEME["HIGHLIGHT1"],),
        widget.Backlight(backlight_name=BACKLIGHT_NAME),
        v_sep,
        widget.TextBox(
            text="&#xf240;",
            fontsize=FONT_ICON_SIZE,
            foreground=THEME["HIGHLIGHT1"],),
        widget.Battery(),
        v_sep,
        widget.TextBox(
            text="&#xf073;",
            fontsize=FONT_ICON_SIZE,
            foreground=THEME["HIGHLIGHT1"],),
        widget.Clock(
            format="%I:%M %p",
            mouse_callbacks={M_BTNS[0]: lambda: qtile.cmd_spawn(f"{TERMINALS[0]} --hold  --class alacrittykhal --title Calendar -e khal --color interactive")}),
        v_sep,
        widget.TextBox(
            text="&#xf705;",
            fontsize=FONT_ICON_SIZE,
            foreground=THEME["HIGHLIGHT1"],
            mouse_callbacks={M_BTNS[0]: lambda: qtile.cmd_shutdown()}),
        widget.TextBox(
            text="&#xf0e2;",
            fontsize=FONT_ICON_SIZE,
            foreground=THEME["HIGHLIGHT1"],
            mouse_callbacks={M_BTNS[0]: lambda: qtile.cmd_spawn(f"{TERMINALS[0]} -e reboot")}),
        widget.TextBox(
            text="&#xf011;",
            fontsize=FONT_ICON_SIZE,
            foreground=THEME["HIGHLIGHT1"],
            mouse_callbacks={M_BTNS[0]: lambda: qtile.cmd_spawn(f"{TERMINALS[0]} -e shutdown now")}),
        sep_big,
    ]
    return widgets


def create_screen():
    screen = Screen(
        top=bar.Bar(
            create_widgets(),
            BAR_HEIGHT,
            opacity=OPACITY,
        ),
    )
    return screen

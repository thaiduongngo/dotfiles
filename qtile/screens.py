
from libqtile.lazy import lazy
from libqtile.config import Group, Key, Screen
from libqtile import bar, layout, widget, qtile
from keys import M_BTNS
from nspace import FONTS, HOME_DIR, BACKLIGHT_NAME, TERMINALS, read_props
from nspace import WN_MARGIN, WN_BORDER_WIDTH, FONT_SIZE, FONT_ICON_SIZE, TEXT_PADDING_SIZE, OPACITY


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


def create_widgets():
    widgets = [
        sep_big,
        widget.Image(
            filename="~/.config/qtile/icons/arch-round1.png",
            scale="False",
            mouse_callbacks={
                M_BTNS[0]: lambda: qtile.cmd_spawn(TERMINALS[0])}),
        sep,
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
        ),
        sep,
        widget.Prompt(fmt="❯ {}"),
        widget.WindowName(fmt="❯ {}",
                          padding=6,
                          empty_group_string="<Empty>"),
        sep,
        widget.CurrentLayoutIcon(scale=0.66),
        sep,
        widget.StatusNotifier(),
        sep,
        widget.TextBox(text="&#xf028;", fontsize=FONT_ICON_SIZE,
                       foreground=THEME["HIGHLIGHT1"],),
        widget.Volume(),
        sep,
        widget.TextBox(text="&#xf108;", fontsize=FONT_ICON_SIZE,
                       foreground=THEME["HIGHLIGHT1"],),
        widget.Backlight(backlight_name=BACKLIGHT_NAME),
        sep,
        widget.TextBox(text="&#xf240;", fontsize=FONT_ICON_SIZE,
                       foreground=THEME["HIGHLIGHT1"],),
        widget.Battery(),
        sep,
        widget.TextBox(text="&#xf133;", fontsize=FONT_ICON_SIZE,
                       foreground=THEME["HIGHLIGHT1"],),
        widget.Clock(format="%I:%M %p"),
        # widget.Clock(format="%Y-%m-%d %I:%M %p"),
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

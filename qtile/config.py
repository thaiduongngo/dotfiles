from libqtile import layout, hook
from libqtile.config import Click, Drag, Match
from libqtile.lazy import lazy
from libqtile.dgroups import simple_key_binder
from subprocess import Popen
from utils import HOME_DIR
from keys import create_keys, MOD, M_BTNS
from screens import create_groups, create_layouts, create_screen, WIDGET_DEFAULTS

dgroups_key_binder = simple_key_binder(MOD)
dgroups_app_rules = []  # type: list
keys = create_keys()
groups, keys = create_groups(ks=keys)
layouts = create_layouts()
widget_defaults = WIDGET_DEFAULTS
extension_defaults = widget_defaults.copy()
screens = [create_screen(), ]
mouse = [
    Drag([MOD], M_BTNS[0], lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([MOD], M_BTNS[2], lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([MOD], M_BTNS[1], lazy.window.bring_to_front()),
]

# Run the utility of `xprop` to see the wm class and name of an X client.
# Add more rules into the list `FLOAT_RULES`
FLOAT_RULES = [
    ("wm_class", "microsoft teams - preview"),
    ("title", "Confirm File Replacing"),
]


def create_float_rules(float_rules):
    frs = [*layout.Floating.default_float_rules]
    for float_rule in float_rules:
        if float_rule[0] == "wm_class":
            frs.append(Match(wm_class=float_rule[1]))
        elif float_rule[0] == "title":
            frs.append(Match(title=float_rule[1]))
    return frs


floating_layout = layout.Floating(float_rules=create_float_rules(FLOAT_RULES))
follow_mouse_focus = False
bring_front_click = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False
wmname = "LG3D"
wl_input_rules = None


@ hook.subscribe.startup
def autostart():
    Popen([f"{HOME_DIR}/.config/qtile/autostart.sh"])


@ hook.subscribe.startup_once
def autostart_once():
    Popen([f"{HOME_DIR}/.config/qtile/autostart_once.sh"])

from libqtile import layout, hook
from libqtile.config import Match
from libqtile.dgroups import simple_key_binder
from subprocess import Popen
from nspace import HOME_DIR
from keys import MOD, KEYS, MOUSE_EVENTS
from screens import create_layouts, create_screen, WIDGET_DEFAULTS
from grps import create_groups
from floatings import create_floating


dgroups_key_binder = simple_key_binder(MOD)
dgroups_app_rules = []  # type: list
keys = KEYS
groups = create_groups(ks=keys)
layouts = create_layouts()
widget_defaults = WIDGET_DEFAULTS
extension_defaults = widget_defaults.copy()
screens = [create_screen(), ]
mouse = MOUSE_EVENTS
floating_layout = create_floating(layout)
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

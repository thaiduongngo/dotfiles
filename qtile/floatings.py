from libqtile import layout
from libqtile.config import Match


WM_CLASS = "wm_class"
TITLE = "title"
# Run the utility of `xprop` to see the wm class and name of an X client.
# Add more rules into the list `FLOAT_RULES`
FLOAT_RULES = [
    (WM_CLASS, "microsoft teams - preview"),
    (WM_CLASS, "vlc"),
    (WM_CLASS, "mpv"),
    (WM_CLASS, "spectacle"),
    (TITLE, "Confirm File Replacing"),
    (TITLE, "Copying files"),
]


def create_floating(layout):
    frs = [*layout.Floating.default_float_rules]
    for fr in FLOAT_RULES:
        if fr[0] == WM_CLASS:
            frs.append(Match(wm_class=fr[1]))
        elif fr[0] == TITLE:
            frs.append(Match(title=fr[1]))
    return layout.Floating(float_rules=frs)

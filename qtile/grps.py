from libqtile.lazy import lazy
from libqtile.config import Group, Key
from keys import MOD, SHIFT


WORKSPACES = (
    ("1", "1", "bsp"),
    ("2", "2", "bsp"),
    ("3", "3", "bsp"),
    ("4", "4", "bsp"),
    ("5", "5", "bsp"),
    ("6", "6", "bsp"),
    ("7", "7", "bsp"),
    ("8", "8", "bsp"),
    ("9", "9", "bsp"),
    ("0", "0", "bsp"),
)


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
    return grps

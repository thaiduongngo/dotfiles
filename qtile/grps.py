from libqtile.lazy import lazy
from libqtile.config import Group, Key
from keys import MOD, SHIFT


WORKSPACES = (
    ("1", "1", "ratiotile"),
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

from libqtile.config import Key
from libqtile.lazy import lazy
import commands

mod = "mod4"
default_term = "alacritty"

# >>> keys section >>>
keys = [
    # Switch between windows in current stack pane
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

    # Move windows up or down in current stack
    Key([mod, "control"], "j", lazy.layout.shuffle_down()),
    Key([mod, "control"], "k", lazy.layout.shuffle_up()),
    Key([mod, "control"], "h", lazy.layout.shuffle_left()),
    Key([mod, "control"], "l", lazy.layout.shuffle_right()),

    Key([mod, "mod1"], "k", lazy.layout.grow()),
    Key([mod, "mod1"], "j", lazy.layout.shrink()),
    Key([mod, "mod1"], "h", lazy.layout.normalize()),
    Key([mod, "mod1"], "l", lazy.layout.maximize()),

    Key([mod, "shift"], "k", lazy.layout.grow_up()),
    Key([mod, "shift"], "j", lazy.layout.grow_down()),
    Key([mod, "shift"], "h", lazy.layout.grow_left()),
    Key([mod, "shift"], "l", lazy.layout.grow_right()),

    Key([mod, "mod1", "control"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1", "control"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1", "control"], "h", lazy.layout.flip_left()),
    Key([mod, "mod1", "control"], "l", lazy.layout.flip_right()),
    Key([mod, "shift"], 'f', lazy.layout.flip()),

    Key([mod, "shift"], "BackSpace", lazy.layout.reset()),
    Key([mod], "equal", lazy.layout.increase_ratio()),
    Key([mod], "minus", lazy.layout.decrease_ratio()),
    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn(default_term)),
    Key([mod], 'f', lazy.window.toggle_floating()),
    Key([mod], 'F11', lazy.window.toggle_fullscreen()),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, 'shift'], "Tab", lazy.prev_layout()),
    Key([mod, 'control'], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),
    Key([mod, 'shift'], "r", lazy.spawn(commands.rofi)),
    Key([mod], "p", lazy.spawn('xrandr --output eDP1 --off'), lazy.restart()),
    Key([], "Print", lazy.spawn(commands.ss)),
    Key([mod], "Print", lazy.spawn(commands.ss_mod)),
    Key(['shift'], "Print", lazy.spawn(commands.ss_doc)),
    Key([mod, 'shift'], "Print", lazy.spawn(commands.ss_doc_mod)),

    # Media keys setup
    Key([], "XF86AudioPlay", lazy.spawn("cmus-remote -u")),
    Key([], "XF86AudioNext", lazy.spawn("cmus-remote -n")),
    Key([mod], "XF86AudioNext", lazy.spawn("cmus-remote --seek +10s")),
    Key([mod], "XF86AudioPrev", lazy.spawn("cmus-remote --seek -10s")),
    Key([], "XF86AudioPrev", lazy.spawn("cmus-remote -r")),
    Key([], "XF86AudioStop", lazy.spawn("cmus-remote -s")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ +2%")),
    Key([mod], "XF86AudioRaiseVolume", lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ -2%")),
    Key([mod], "XF86AudioLowerVolume", lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl -- set-sink-mute @DEFAULT_SINK@ toggle")),
]
# <<< keys section <<<



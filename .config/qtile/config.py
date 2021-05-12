# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import subprocess
import time
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget, hook

from typing import List  # noqa: F401

mod = "mod4"
myterm = "alacritty"
my_screenshotdir = '/home/gentoo/henrique/Screenshots/'
my_print_cmd = "sh -c 'import -window root " +\
                my_screenshotdir + "$(date +%Y%m%d%H%M%S).png'"

my_vol_cmd = "/home/gentoo/henrique/.config/qtile/get_volume.sh"
my_rofi_cmd = "rofi -theme /usr/share/rofi/themes/arthur.rasi \
                -show drun \
                -terminal " + myterm 

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

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn(myterm)),
    Key([mod], 'f', lazy.window.toggle_floating()),
    Key([mod], 'F11', lazy.window.toggle_fullscreen()),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, 'shift'], "Tab", lazy.prev_layout()),
    Key([mod, 'control'], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),
    Key([mod, 'shift'], "r", lazy.spawn(my_rofi_cmd)),
    Key([mod], "p", lazy.spawn('xrandr --output eDP1 --off')),
    Key([], "Print", lazy.spawn(my_print_cmd)),
   
    # Media keys setup
    Key([], "XF86AudioPlay", lazy.spawn("cmus-remote -u")),
    Key([], "XF86AudioNext", lazy.spawn("cmus-remote -n")),
    Key([], "XF86AudioPrev", lazy.spawn("cmus-remote -r")),
    Key([], "XF86AudioStop", lazy.spawn("cmus-remote -s")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ +1%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ -1%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl -- set-sink-mute 0 toggle")), 
]

groups = [Group(i) for i in "12345678"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

# >>> layouts section >>>

layout_params = dict(
    margin=6, 
    border_focus='DB5247', #'A33A4E', #'A73F32', #A0ffff',
    border_normal='222120',
    border_width=2
)

layouts = [
    layout.MonadTall(**layout_params),
    layout.Max(),
    layout.Stack(num_stacks=2, **layout_params),
    layout.Bsp(**layout_params),
    layout.Columns(**layout_params),
    layout.Matrix(**layout_params),
    #layout.MonadWide(**layout_params),
    #layout.RatioTile(**layout_params),
    #layout.Tile(**layout_params),
    #layout.TreeTab(),
    #layout.VerticalTile(**layout_params),
    #layout.Zoomy(**layout_params),
]
# <<< layouts section <<<

colors = {
    'text_highlight' : 'A73F32',
    'text_normal' : 'EDC29A', 
}


widget_defaults = dict(
    font='Source Code Pro',
    fontsize=9,
    padding=3,
    foreground='EDC29A',
    background='171615',
    border_color='323130',

    # graph monitor
    line_width=2,
    frequency=0.1,
    start_pos='top',
    samples=5000
)
extension_defaults = widget_defaults.copy()


separator_options = dict(
    foreground=widget_defaults['border_color'],
    linewidth=2,
    size_percent=50,
    padding=3,
)

mybar = bar.Bar([
                widget.Image(filename = "~/.config/qtile/gentoo.png",
                             scale = True,
                             margin=5,
                ),
                widget.Sep(**separator_options),
                widget.Clock(format='%a %d of %b %H:%M:%S'),
                widget.Sep(**separator_options),
                widget.CurrentLayout(foreground=colors['text_highlight'],),
                widget.GroupBox(active='EDC29A',
                                block_highlight_text_color=colors['text_highlight'],
                                this_current_screen_border=colors['text_highlight'],
                                borderwidth=1,
                                disable_drag=True,
                ),
                widget.Sep(**separator_options),
                widget.Prompt(),
                widget.Sep(**separator_options),
                widget.WindowName(foreground=colors['text_highlight']),
                widget.Cmus(foreground=widget_defaults['foreground'],
                            play_color=colors['text_highlight'],
                            align='right',
                ),
                widget.Sep(**separator_options),
                widget.Volume(),
                widget.Systray(icon_size=12),
                widget.Sep(**separator_options),
                widget.CPUGraph(graph_color='FF9AA0',
                                fill_color='7D2F3E',
                ),
                widget.MemoryGraph(graph_color='FF0000',
                                   fill_color='A12231',
                ),
                widget.NetGraph(graph_color='FF7753',
                                fill_color='9C382B',
                ),
                widget.HDDBusyGraph(device='sdb',
                                    graph_color='FAD42E',
                                    fill_color='9E6B26',
                ),
            ],
            size=24,
            # config
            opacity=0.9,
            margin=[3, 5, 3, 5],
            background='171615')



screens = [ 
    Screen(top=mybar,
           wallpaper='/home/shared/wallpapers/nebula.jpg',
           wallpaper_mode='fill',),

    Screen(top=mybar,
           wallpaper='/home/shared/wallpapers/nebula.jpg',
           wallpaper_mode='fill',),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
    pass

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "qtile"

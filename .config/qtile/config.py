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
from libqtile import layout, bar, widget, hook, qtile
#from powerline.bindings.qtile.widget import PowerlineTextBox

from typing import List  # noqa: F401
import commands
from keybindings import mod, keys, default_term
from colorschemes import dracula_colors as colors


# >>> groups section >>>
g_symbols = '☿♀♁♂♃♄⛢♆'
groups = [Group(name) for name in g_symbols]

for g in groups:
    keys.extend([
        Key([mod], str(g_symbols.index(g.name) + 1),
            lazy.group[g.name].toscreen()),
        Key([mod, 'control'], str(g_symbols.index(g.name) + 1),
            lazy.window.togroup(g.name, switch_group=False)),
        Key([mod, 'shift'], str(g_symbols.index(g.name) + 1),
            lazy.window.togroup(g.name, switch_group=True)),
    ])
# <<< groups section <<<

# >>> layouts section >>>
layout_params = dict(
    margin=0,
    border_focus=colors['border'],
    border_normal=colors['border_inactive'],
    border_width=1
)

layouts = [
    layout.Bsp(**layout_params,
               grow_amount=5,
               fair=False,),
    layout.Max(),
    layout.MonadTall(**layout_params),
]
# <<< layouts section <<<

widget_defaults = dict(
    #font='SauceCodePro Nerd Font',
    font='Source Code Pro Bold',
    fontsize=9,
    padding=2,
    foreground=colors['highlight'],
    background=colors['background'],
    border_color=colors['border'],
)

extension_defaults = widget_defaults.copy()

graph_monitor_options = dict(
    graph_color=colors['highlight'],
    line_width=1,
    #start_pos='top',
    frequency=0.3,
    samples=100,
    margin_x=1,
    margin_y=4,
    border_width=0,
    type='line',
    mouse_callbacks={ 'Button1': lambda qtile: qtile.cmd_spawn('alacritty -e htop') },
)

separator_options = dict(
    foreground=colors['separator'],
    linewidth=1,
    size_percent=50,
    padding=4,
)

groupbox_options = dict(
    active=colors['highlight'],
    font='Symbola',
    fontsize=10,
    block_highlight_text_color=colors['group_active'],
    this_current_screen_border=colors['group_active'],
    inactive=colors['group_inactive'],
    borderwidth=1,
    disable_drag=True
)

clock_options = dict(
    format='%a %d of %b %H:%M:%S',
    mouse_callbacks={
        'Button1': lambda qtile: qtile.cmd_spawn('xcalendar'),
        'Button3': lambda qtile: qtile.cmd_spawn('killall xcalendar')
    }
)

widgets_main = [
    widget.Sep(**separator_options),
    widget.TextBox(
                 '',
                 fontsize=18,
                 foreground=colors['highlight'],
                 mouse_callbacks={
                    'Button1': lambda qtile: qtile.cmd_spawn(commands.rofi)
                 }
    ),
    widget.Sep(**separator_options),
    widget.CurrentLayout(foreground=colors['highlight'],),
    widget.GroupBox(**groupbox_options),
    widget.Sep(**separator_options),
    widget.Prompt(prompt='☉ ',),
    widget.Sep(**separator_options),
    widget.WindowName(foreground=colors['highlight']),
    widget.CPUGraph(**graph_monitor_options),
    widget.MemoryGraph(**graph_monitor_options),
    widget.NetGraph( **graph_monitor_options),
    widget.HDDBusyGraph(device='sdb', **graph_monitor_options),
    widget.HDDBusyGraph(device='sda', **graph_monitor_options),
    widget.Spacer(bar.STRETCH),
    widget.Cmus(foreground=colors['text_normal'],
                play_color=colors['highlight'],
            ),
    widget.Sep(**separator_options),
    widget.Systray(icon_size=12),
    widget.Sep(**separator_options),
    widget.TextBox('', fontsize=18),
    widget.Volume(),
    widget.Sep(**separator_options),
    widget.Clock(**clock_options),
    widget.Sep(**separator_options),
    #widget.BatteryIcon(),
]

widgets_bar2 = [
    widget.Sep(**separator_options),
    widget.WindowName(foreground=colors['highlight']),
    widget.Sep(**separator_options),
    widget.Clock(**clock_options),
    widget.Sep(**separator_options),
    widget.GroupBox(**groupbox_options),
    widget.Sep(**separator_options),
]

bar_defaults = dict(size=24,
                    opacity=1,
                    margin=[0, 0, 0, 0],
                    background=colors['background'])

bar_screen1 = bar.Bar(widgets=widgets_main,
                      **bar_defaults)
bar_screen2 = bar.Bar(widgets=widgets_bar2,
                      **bar_defaults)

screens = [
    Screen(top=bar_screen1,
           wallpaper='~/.wallpapers/planets2.jpg',
           wallpaper_mode='fill',),
    Screen(top=bar_screen2,
           wallpaper='~/.wallpapers/planets2.jpg',
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
floating_layout = layout.Floating(
    float_rules=[
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
        {'wmclass': 'xcalendar'}, # xcalendar
        {'wmclass': 'dayEditor'} # xcalendar day editor
    ],
    **layout_params
)
auto_fullscreen = True
focus_on_window_activation = "smart"
#reconfigure_screens = True

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
    subprocess.call([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

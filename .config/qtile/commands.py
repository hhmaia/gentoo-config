# >>> screenshot related >>>
ss_dir = '/home/gentoo/henrique/Screenshots/'
ss_doc_dir = '/home/gentoo/henrique/Screenshots/doc/'
ss_pattern = "$(date +%Y%m%d%H%M%S).png'"

ss = "sh -c 'import -window root " + ss_dir + ss_pattern
ss_mod = "sh -c 'import " + ss_dir + ss_pattern
ss_doc = "sh -c 'import -window root " + ss_doc_dir+ ss_pattern
ss_doc_mod = "sh -c 'import " + ss_doc_dir + ss_pattern
# <<< screenshot related <<<

rofi = "rofi -show drun \
                -width 20 \
                -show-icons \
                -theme ~/.config/rofi/themes/dracula.rasi \
                -terminal alacritty"



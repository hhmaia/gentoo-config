# /etc/skel/.bashrc
#
# This file is sourced by all *interactive* bash shells on startup,
# including some apparently interactive shells such as scp and rcp
# that can't tolerate any output.  So make sure this doesn't display
# anything or bad things will happen !

# Test for an interactive shell.  There is no need to set anything
# past this point for scp and rcp, and it's important to refrain from
# outputting anything in those cases.
if [[ $- != *i* ]] ; then
	# Shell is non-interactive.  Be done now!
	return
fi

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

. ~/.local/bin/git-prompt.sh

## >>> powerline initialize >>>
if [ ! -z ${COLORTERM} ]; then
    PS1="\[\033[38;5;15;1m濾\033[0m\]"
    PS1="${PS1}\[\033[38;5;13;1m\$(__git_ps1 ' %s')\033[0m\]"
    PS1="${PS1}\[\033[38;5;15;1m 濾\033[0m\]"
    PS1="${PS1}\[\033[38;5;12;1m\w\033[0m\] "
    #PS1="${PS1}\[\033[38;5;15;1m\033[0m\]"
    #PS1="${PS1}\[\033[38;5;11;1m\033[0m\] "
    PS1="${PS1}\[\033[38;5;11;1m 濾\033[0m\]"
    PS2="\[\033[38;5;11;1m濾\033[0m\]"
#    powerline-daemon -q
#    POWERLINE_BASH_CONTINUATION=1
#    POWERLINE_BASH_SELECT=1
#    . /usr/lib/python3.9/site-packages/powerline/bindings/bash/powerline.sh
fi
# <<< powerline initialize <<<
export PATH=~/.local/bin:"$PATH"


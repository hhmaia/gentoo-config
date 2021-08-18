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
    alias dir='dir --color=auto'
    alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

. /usr/share/git/git-prompt.sh

# >>> timer (for prompt) >>>
function timer_start {
  timer=${timer:-$SECONDS}
}

function timer_stop {
  timer_show=$(($SECONDS - $timer))
  printf -v seconds_show "%02d" $((${timer_show}%60))
  printf -v minutes_show "%02d" $((${timer_show}/60))
  unset timer
}

trap 'timer_start' DEBUG
PROMPT_COMMAND=timer_stop

#PS1='${timer_show}'
# <<< timer (for prompt) <<<

## >>> prompt >>>
if [ ! -z ${COLORTERM} ]; then
    # 濾
    PS1=''
    if ! cmp -s "/proc/1/mountinfo" "/proc/$$/mountinfo"; then
       PS1+="\[\e[38;5;1m\]\[\e[0m\]"
    fi
    PS1+="\[\e[38;5;7m\]\$(__git_ps1 '%s')\[\e[0m\]"
    if [ -v SSH_CONNECTION ]; then
        PS1+="\[\e[38;5;6m\] \h\[\e[0m\]"
    fi
    PS1+="\[\e[38;5;4m\]\${minutes_show}:\${seconds_show}\[\e[0m\]"
    PS1+="\[\e[38;5;1;1m\]\w\[\e[0m\]"
    PS1+='`if [ -n "$(jobs -p)" ]; then echo "\[\e[38;5;2;1m\]\j\[\e[0m\]"; fi`'
    PS1+="\[\e[38;5;11m\] ☉ \[\e[0m\]"

    PS2="\[\e[38;5;11;1m\]濾\[\e[0m\]"
fi
# <<< prompt <<<
export PATH=~/.local/bin:"$PATH"
export GPG_TTY=$(tty)

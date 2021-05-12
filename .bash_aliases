alias update-system='sudo sh -c "emerge --sync && emerge -uavDN @world"'
alias ml='conda activate ml-tf'

alias dq='df -h | grep sd | sort -h'
alias info='info --vi-keys'
alias pdb='python -m pdb'
alias fl='head -n 1'
alias lll='tail -n 1'
alias lb='lsblk -f'

# git aliases
alias gits='git status -s'
alias gitss='git status -s | head -n30'
alias gitl='git log --oneline'
alias gitt='git log --format=oneline --graph --all'
alias gitr='git rev-parse --short HEAD'

# some more ls aliases
alias ll='ls -l'
alias la='ls -A'
alias l='ls -CF'
alias lsa='ls -lahF --group-directories-first'

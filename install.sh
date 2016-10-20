#!/bin/bash
# Copyright 2016 Charles Daudré-Vignier <daudre.vignier.charles@narod.ru>
#    'install.sh' is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    'install.sh' is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with 'install.sh'.  If not, see <http://www.gnu.org/licenses/>.

main()
{
    OLD_PWD=$PWD
    OFSCRIPT_PWD="$HOME/.of-script"
    declare -r OFSCRIPT_PWD
    OFSCRIPT_LIB="$HOME/.of-script/lib"
    declare -r OFSCRIPT_LIB
    OFSCRIPT_ETC="$HOME/.of-script/etc"
    declare -r OFSCRIPT_ETC

    get_used_shell()
    {
        local cmd="whiptail --radiolist \"What shell are you using ?\nThis determine which script are compatible whith your favorite shell.\""

        local shell_list=$(cat /etc/shells|sed 1d|grep -v 'byobu'|egrep -v "(byobu|tmux|screen)")
        local nbr_shell=$(printf "$shell_list"|wc -l)
        cmd="$cmd $((nbr_shell+11)) 40 $((nbr_shell+1))"
        while read line ; do
            cmd="$cmd \"$line\" \"\" 0 "
        done <<< "$shell_list"
        eval "$cmd 3>&1 1>&2 2>&3"
    }

    install_python_script()
    {
       [[ -d '/opt/' ]] || mkdir /opt/ ;
       mkdir $OFSCRIPT_PWD;
       mkdir $OFSCRIPT_LIB;
       mkdir $OFSCRIPT_ETC;
    }

    used_shell=$(get_used_shell)

    declare shell_type
    local bad1="/bin/dash" ; local bad2="/bin/sh" ;
    local bad3="/usr/bin/ksh" ; local bad4="/bin/ksh" ; local bad5="/etc/alternative/ksh" ;
    local bad6="/usr/bin/csh" ; local bad7="/bin/csh" ; local bad8="/etc/alternative/csh";
    local bad9="/usr/bin/tcsh" ;  local bad10="/bin/tcsh" ; local bad11="/etc/alternative/tcsh";
    case $used_shell in
        "/usr/bin/zsh"|"bin/zsh"|"/etc/alternative/zsh"|"/etc/alternative/zsh-usrbin"|"/bin/zsh5"|"/bin/zsh4") conf_file='~/.zshrc'
        ;;
        "/bin/bash"|"/usr/bin/rbash") conf_file='~/.bashrc'
        ;;
        $bad1|$bad2|$bad3|$bad4|$bad5|$bad6|$bad7|$bad8|$bad9|$bad10|$bad11) printf "$used_shell is not compatible with these shell script.\nAborting...\n"
        ;;
    esac

    return 0
}

main "$@"

#!/bin/zsh

# Copyright 2016 Charles Daudré-Vignier <daudre.vignier.charles@narod.ru>

#    'korganizer-debug-333754' is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    'korganizer-debug-333754' is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with 'korganizer-debug-333754'.  If not, see <http://www.gnu.org/licenses/>.

main(){
    declare -r FILE="$HOME/.kde/share/config/korganizerrc"
    # Recupere les categories personnalisees par l'utilisateur
    createCCAT(){
        awk -v PCAT=$PCAT '{ print } /\[General\]/ { print PCAT }' $FILE > $FILE.tmp && mv $FILE.tmp $FILE
    }

    PCAT=$( 
        <$FILE |
        sed -n '/\[Category Colors2\]/,/\[/{//d;p}' |
        awk -F "=" '{print $1}'|sed '$d'|tr '\n' ',' |
        sed '$ s/.$//'
    )
    PCAT="Custom Categories=$PCAT"
    # Cherche si la ligne "Custom Categories" existe
    [[ "$( <$FILE|grep 'Custom Categories'|awk -F '=' '{print $1}' )" == 'Custom Categories' ]] &&
        XCAT=1 || XCAT=0
    # Si la ligne "Custom Categories" existe deja, vérifie que toutes les categories personnalisees y sont listees
    [[ $XCAT -eq 1 ]] &&
        grep -v 'Custom Categories' $FILE > $FILE.tmp &&
        mv $FILE.tmp $FILE &&
        createCCAT
    # Si la ligne "Custom Categories" n'existe pas, la crée et y ajoute les categories personnalisees definies par l'utilisateur
    [[ $XCAT -eq 0 ]] &&
        createCCAT
}

main "$@"
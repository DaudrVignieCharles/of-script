#!/usr/bin/python3.4
# -*-coding:UTF8 -*
# Copyright 2016 Charles Daudré-Vignier <daudre.vignier.charles@narod.ru>
#    'iftop_generic.py' is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    'iftop_generic.py' is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with 'iftop_generic.py'.  If not, see <http://www.gnu.org/licenses/>.

import os

def erase(numb):
    """Efface un certain nombre de lignes et remonte le curseur d'autant plus un."""
    print("\x1b[1A\033[2K"* numb +"\x1b[1A")

def cprint(cmd):
    """Execute une commande shell et retourne le résultat"""
    return os.popen(cmd).read().strip()

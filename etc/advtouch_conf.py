#!/usr/bin/python3.4
# -*-coding:UTF8 -*
# Copyright 2016 Charles Daudré-Vignier <daudre.vignier.charles@narod.ru>
#    'advtouch_conf.py' is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    'advtouch_conf.py' is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with 'advtouch_conf.py'.  If not, see <http://www.gnu.org/licenses/>.

##############
# C AND C++  #
##############

# ctxt is the copyright for C source file
# You can use {year} variable, and {name} variable (name of the file passed as argument when exec advtouch).
ctxt = """/*Copyright {year} Charles Daudré-Vignier <daudre.vignier.charles@narod.ru>
'{name}' is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.
'{name}' is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with '{name}'.  If not, see <http://www.gnu.org/licenses/>.œ*/
{include}
"""

# Common include for C
c_include = """#include<stdio.h>
#include<stdlib.h>
#include<string.h>
"""

# Common include for C++
cpp_include = """#include<iostream>
#include<string>
using namespace std;
"""

# Minimum code in the C or C++ file (default is main function declaration).
minimum_ctype_code = """
main()
{
    
    return 0;
}"""

##########
# Python #
##########

# ctxt is the copyright for Python source file
# You can use {year} variable, and {name} variable (name of the file passed as argument when exec advtouch).
shebangtxt = """# Copyright {year} Charles Daudré-Vignier <daudre.vignier.charles@narod.ru>
#    '{name}' is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    '{name}' is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with '{name}'.  If not, see <http://www.gnu.org/licenses/>.
"""

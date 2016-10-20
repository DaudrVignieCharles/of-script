#!/usr/bin/python3.4
# -*-coding:UTF8 -*
# Copyright 2016 Charles Daudré-Vignier <daudre.vignier.charles@narod.ru>
#    'advtouch.py' is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    'advtouch.py' is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with 'advtouch.py'.  If not, see <http://www.gnu.org/licenses/>.

from collections import OrderedDict
import os
os.sys.path.append('/opt/reroot/lib/')
import lib_generic


def desktop_generator():
    """Génerer le fichier desktop"""
    ended = False
    while ended == False:
        desk_template = OrderedDict([('version', '1.2'),
                        ('name', 'Minecraft'),
                        ('genericname', 'Construction game'),
                        ('comment', 'Minecraft the best game'),
                        ('type', 'Application'),
                        ('exec', '/usr/bin/Minecraft %U'),
                        ('tryexec', '/usr/bin/Minecraft'),
                        ('mimetype', 'java'),
                        ('icon', 'minecraft'),
                        ('categories', 'game;anothercategorie;anotherone')])
        for i in desk_template.keys():
            desk_template[i] = input("""{0} (Ex:{1}): """.format(i, desk_template[i]))

        desk_text = """[Desktop Entry]
Version={version}
Name={name}
GenericName={genericname}
Comment={comment}
Type={type}
Exec={exec}
TryExec={tryexec}
MimeType={mimetype}
Icon={icon}
Categories={categories}
""".format(version=desk_template['version'],
        name=desk_template['name'],
        genericname=desk_template['genericname'],
        comment=desk_template['comment'],
        type=desk_template['type'],
        exec=desk_template['exec'],
        tryexec=desk_template['tryexec'],
        mimetype=desk_template['mimetype'],
        icon=desk_template['icon'],
        categories=desk_template['categories'])

        print('\nAre these information exact :\n' + desk_text + 'Y/N ? ')
        while True:
            yesno = input('>>> ').lower()
            if yesno == 'y':
                ended=True
                break
            elif yesno == 'n':
                print('\x1bc')
                break
            else :
                print('You must enter Y or N...')
                input('<<<PRESS ENTER>>>')
                lib_generic.erase(3)
                continue
    desk_text_old = desk_text
    ended = False
    while not ended:
        desk_text = desk_text_old
        print('\x1Bc\nWould you want add some actions : Y/N ? ')
        yesno = input('>>> ').lower()
        if yesno == 'y':
            actions = input('Type wanted action name, action are splitted with semicolon (;) :\n>>> ')
            desk_text+="""X-Ayatana-Desktop-Shortcuts={0}\n""".format(actions)
            actionslist = actions.split(sep=';')
            actiondict = {}
            for i in actionslist:
                actiondict[i] = input('What is the action (exec) for {0} ? '.format(i))
            for i in actiondict.keys():
                desk_text+="""\n[{0} Shortcut Group]
Name={0}
Exec={1}
""".format(i, actiondict[i])
            print('\nAre these information exact :\n' + desk_text + 'Y/N ? ')
            while True:
                yesno = input('>>> ').lower()
                if yesno == 'y':
                    ended = True
                    break
                elif yesno == 'n':
                    print('\x1bc')
                    break
                else :
                    print('You must enter Y or N...')
                    input('<<<PRESS ENTER>>>')
                    lib_generic.erase(3)
                    continue
        elif yesno == 'n':
            print('\x1bc')
            break
        else :
            print('You must enter Y or N...')
            input('<<<PRESS ENTER>>>')
            lib_generic.erase(3)
            continue
    return desk_text
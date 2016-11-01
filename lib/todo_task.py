#!/usr/bin/python3.4
# -*-coding:UTF8 -*
# Copyright 2016 Charles Daudré-Vignier <daudre.vignier.charles@narod.ru>
#    'todo_task.py' is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    'todo_task.py' is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with 'todo_task.py'.  If not, see <http://www.gnu.org/licenses/>.

import pickle
import json
import datetime

def dater(task_date):
    try:
        up_date = datetime.datetime.strptime(task_date, '%d-%m-%Y')
        return up_date.strftime('%A %d %B %Y')
    except ValueError:
        print(task_date+" is not a valid date.\nValid date syntax is : 'day-month-year'. ")
        exit(1)


def tags_pretty_print(tags):
    return ', '.join(tags)


def print_task(task_name,task_list):
    print("""\x1b[31;1m[\x1b[33;1m {task_name} \x1b[31;1m]\x1b[0m
\x1b[34;1m * \x1b[0mDate :
{task_date}
\x1b[34;1m * \x1b[0mDescription :
{task_text}
\x1b[34;1m * \x1b[0mTags :
{task_tags}\n""".format(task_name=task_name, task_date=task_list[task_name]['date'], task_text=task_list[task_name]['text'], task_tags=tags_pretty_print(task_list[task_name]['tags'])))


def load_tasks(SAVEFILE):
    with open(SAVEFILE, 'r') as savefile:
        task_list = json.load(savefile)
    return task_list


def save_tasks(task_list, SAVEFILE):
    with open(SAVEFILE, 'w') as savefile:
        json.dump(task_list, savefile)
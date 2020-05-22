#!/usr/bin/env python3

"""
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

"""
Author: Rob Shepherd
First Created: May 2020
"""

import argparse
import sqlite3
import sys
import os
import json


def get_args():
    parser = argparse.ArgumentParser(description='Get/Set Key-Values in a database')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--get', nargs=2, metavar=('KEY', 'DEFAULT'), help='GET a value with key KEY and value DEFAULT if not set')
    group.add_argument('--set', nargs=2, metavar=('KEY', 'VALUE'), help='SET a value with key KEY and value VALUE')
    group.add_argument('--set-default', dest='set_def', nargs=2, metavar=('KEY', 'VALUE'), help='SET a value ONLY IF KEY does NOT already exist (used for populating defaults)')
    group.add_argument('--del', nargs=1, metavar=('KEY'), help='DELETE a key and value with key KEY')
    group.add_argument('--create', action='store_true', help="Create schema")
    parser.add_argument('--db', nargs=1, metavar='DATABASE', help="Specify Database path (you can also set an environment variable 'STALLY_SETTINGS_DB' which will be overriden by --db)")
    return parser.parse_args(), parser

def connect(dbpath):
    return sqlite3.connect(dbpath)

def create(dbpath):
    c = connect(dbpath)
    c.execute('create table if not exists settings (key varchar(100) PRIMARY KEY, val JSON)')

def kvget(dbpath, key, default_value=None):
    with connect(dbpath) as c:
        cur = c.execute('SELECT val FROM settings WHERE key=? LIMIT 1', (key,))
        val = cur.fetchone()
        if val is not None:
            val = val[0]
            val = json.loads(val)
        return val if val is not None else default_value

def kvset(dbpath, key, val):
    with connect(dbpath) as c:
        cur = c.execute('INSERT INTO SETTINGS VALUES( ?, json(?)) ON CONFLICT(key) DO UPDATE set val = json(?)', (key, json.dumps(val), json.dumps(val)))

def kvadd(dbpath, key, val):
    with connect(dbpath) as c:
        cur = c.execute('INSERT INTO SETTINGS VALUES( ?, json(?)) ON CONFLICT(key) DO NOTHING', (key, json.dumps(val)))      

if __name__ == "__main__":

    args, parser = get_args()
    db_path = args.db if hasattr(args, 'db') else None
    db_path=os.getenv('STALLY_SETTINGS_DB', db_path)
    if db_path is None:
        print("ERROR: No DB specified\n", file=sys.stderr)
        parser.print_help(sys.stderr)
        sys.exit(1)


    if args.get:
       print(kvget(db_path, args.get[0], default_value=args.get[1]))
    elif args.set:
       kvset(db_path, args.set[0], args.set[1])
    elif args.set_def:
       kvadd(db_path, args.set_def[0], args.set_def[1])
    
    elif args.create:
        create(db_path)
    else:
        print("ERROR: No command specified\n", file=sys.stderr)
        parser.print_help(sys.stderr)
        sys.exit(1)

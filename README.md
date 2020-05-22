# PesdaDB
A Key-Value database for the command-line and in Python, backed by SQLite3

### Overview

    you@computer:~ $ python3 ~/PesdaDB/pesdadb.py 
    ERROR: No command specified

    usage: settings.py [-h]
                       [--get KEY DEFAULT | --set KEY VALUE | --set-default KEY VALUE | --del KEY | --create]
                       [--db DATABASE]

    Get/Set Key-Values in a database

    optional arguments:
      -h, --help            show this help message and exit
      --get KEY DEFAULT     GET a value with key KEY and value DEFAULT if not set
      --set KEY VALUE       SET a value with key KEY and value VALUE
      --set-default KEY VALUE
                            SET a value ONLY IF KEY does NOT already exist (used
                            for populating defaults)
      --del KEY             DELETE a key and value with key KEY
      --create              Create schema
      --db DATABASE         Specify Database path (you can also set an environment
                            variable 'PESDADB' which will be overriden by --db)

### Specify path to database

(you can also use `--db <path>` on every call if you like)

    you@computer:~ $ export PESDADB=/tmp/my_pesdadb_store.db

### Manually create it first

    you@computer:~ $ python3 ~/PesdaDB/pesdadb.py --create

### Set and Get a string

    you@computer:~ $ python3 ~/PesdaDB/pesdadb.py --set foo bar

    you@computer:~ $ python3 ~/PesdaDB/pesdadb.py --get foo baz
    bar

### It always wants a default value 

...in case the key does not exist, so just specify an empty string if you don't care

    you@computer:~ $ python3 ~/PesdaDB/pesdadb.py --get foo ""
    bar

### Set a default value

if you want to overwrite a set of new default settings for your program, but this won't replace any existing ones

    you@computer:~ $ python3 ~/PesdaDB/pesdadb.py --set-default foo fuzz

    you@computer:~ $ python3 ~/PesdaDB/pesdadb.py --get foo ""
    bar

### Send in JSON, get back JSON

in fact it will only store valid json. Then you can chain it to JQ or something if you like

    you@computer:~ $ python3 ~/PesdaDB/pesdadb.py --set my_array '["zuli", "kyan", "lars", "fozz"]'

    you@computer:~ $ python3 ~/PesdaDB/pesdadb.py --get my_array "[]"
    ["zuli", "kyan", "lars", "fozz"]

    you@computer:~ $ python3 ~/PesdaDB/pesdadb.py --get my_array "[]" | jq '.'
    [
      "zuli",
      "kyan",
      "lars",
      "fozz"
    ]

    you@computer:~ $ python3 ~/PesdaDB/pesdadb.py --get my_array "[]" | jq '.[2]'
    "lars"

    you@computer:~ $ python3 ~/PesdaDB/pesdadb.py --set my_object '{"goodies": ["elsa", "anna", "kristoff", "sven", "olaf"], "baddies": ["marshmallow", "hans", "weaselman"]}'

    you@computer:~ $ python3 ~/PesdaDB/pesdadb.py --get my_object "{}" | jq '.baddies[0]'
    "marshmallow"

# Why

I needed a robust key/value store that can be 

* Used simulataneously between many programs at the same time. 
* Used in Python and on the CLI
* Handle JSON & with safe defaults

It's built upon the ubiquitous and amazing Sqlite3 which does all ofthe hard work to satisfay my wishlist above, and so PesdaDB is just a python wrapper for some SQL commands.

    
# License

PesdaDB is provided under the MIT license,  
 but if you use it commercially or otherwise, please consider send a postcard, by mail, from wherever you live, to:

    Rob & Family
    EvoMetric
    G58
    Menai Science Park
    Gaerwen
    Anglesey
    LL60 6AG
    UNITEC KINGDOM

# PesdaDB
A Key-Value database for the command-line and in Python, backed by SQLite3


    you@computer:~ $ export PESDADB=/tmp/my_pesdadb_store.db

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

    you@computer:~ $ python3 ~/PesdaDB/pesdadb.py --create

    you@computer:~ $ python3 ~/PesdaDB/pesdadb.py --set foo bar

    you@computer:~ $ python3 ~/PesdaDB/pesdadb.py --get foo baz
    bar

    you@computer:~ $ python3 ~/PesdaDB/pesdadb.py --get foo ""
    bar

    you@computer:~ $ python3 ~/PesdaDB/pesdadb.py --set-default foo fuzz

    you@computer:~ $ python3 ~/PesdaDB/pesdadb.py --get foo ""
    bar

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

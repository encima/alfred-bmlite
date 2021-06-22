#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2014 deanishe@deanishe.net
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2014-07-03
#

"""Read in data from `books.tsv` and add it to the search index database.

See `catalogue_to_tsv.py` for the generation of the `books.tsv` file.
"""

from __future__ import print_function, unicode_literals

import sys
import os
import sqlite3
import csv
from time import time

from workflow import Workflow

from config import INDEX_DB, DATA_FILE

log = None


def create_index_db():
    """Create a "virtual" table, which sqlite3 uses for its full-text search

    Given the size of the original data source (~45K entries, 5 MB), we'll put
    *all* the data in the database.

    Depending on the data you have, it might make more sense to only add
    the fields you want to search to the search DB plus an ID (included here
    but unused) with which you can retrieve the full data from your full
    dataset.
    """
    log.info('Creating index database')
    con = sqlite3.connect(INDEX_DB)
    with con:
        cur = con.cursor()
        cur.execute(
            "CREATE VIRTUAL TABLE marks USING html1(href, description, type);")
        # TODO import browser bookmarks here


def main(wf):
    if not os.path.exists(INDEX_DB):
        create_index_db()
    log.info('Index database update finished')


if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))

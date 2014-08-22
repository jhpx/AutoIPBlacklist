# -*- coding: utf8 -*-
# Cheack_IP.py
# Author: Jiangmf
from MySQLAdapter import *


def sync_csv_file(results):
    """Union update file "st_visitors.csv" by the new ip list in results."""
    file = open('st_visitors.csv', 'rb+')
    raw = set(file.read().split("\n")[:-1])
    print 'Old st_visitors.csv has %d ip records.' % len(raw)
    results = results.difference(raw)
    file.seek(0, 1)
    for r in results:
        file.write(r + '\n')
    file.flush()
    file.close()
    print 'New st_visitors.csv has %d ip records.' % (len(results)+len(raw))
    pass


def check_ip():
    """Find illegal ip from table related to plugin my-visitors and akismet."""
    [count, results] = MySQLAdapter.mysql_select(
        "SELECT ip FROM `st_visitors` "
        "WHERE `name` REGEXP '[a-zA-Z0-9]+\\s*[0-9]+' "
        "AND NOT EXISTS (SELECT * FROM `st_commentmeta` "
        "WHERE `meta_value` = 'false' AND `meta_key` = 'akismet_result' "
        "AND `name` LIKE CONCAT( '%', `comment_id` ) ) GROUP BY ip")
    print 'Table st_visitors has %s illegal ip records.' % count
    return map(lambda x: x[0], results)

# Script
if __name__ == "__main__":
    sync_csv_file(set(check_ip()))

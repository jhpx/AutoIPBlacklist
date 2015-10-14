#!/usr/bin/env python
# -*- coding: utf8 -*-
# Cheack_IP.py
# Author: Jiangmf
# Date: 2014-07-09
import MySQLdb
from MySQLAdapter import *


def delete_ip_records():
    """delete illegal ip list from table related to plugin my-visitors."""
    sqls = ["create temporary table tmp (ip varchar(32))",
            "Insert Into tmp (ip) SELECT ip FROM `st_visitors` "
            "WHERE `name` REGEXP '[a-zA-Z0-9]+\\s*[0-9]+' "
            "AND NOT EXISTS (SELECT * FROM `st_commentmeta` "
            "WHERE `meta_value` = 'false' AND `meta_key` = 'akismet_result' "
            "AND `name` LIKE CONCAT( '%', `comment_id` ) ) GROUP BY ip",
            "delete from `st_visitors` where ip in (select ip from tmp)"]
    count = MySQLAdapter.mysql_update_many(sqls)
    print '%s illegal records have been deleted' % count

# Script
if __name__ == "__main__":
    delete_ip_records()

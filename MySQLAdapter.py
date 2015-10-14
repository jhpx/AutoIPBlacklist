#!/usr/bin/env python
# -*- coding: utf8 -*-
# MySQLAdapter.py
# Author: Jiangmf
# Date: 2014-07-09
import MySQLdb
import os


class MySQLAdapter(object):
    config = os.path.split(os.path.realpath(__file__))[0] + os.sep +"my.cnf"

    @classmethod
    def mysql_select(cls, sql):

        try:
            print "Connecting to mysql server..."
            conn = MySQLdb.connect(read_default_file=cls.config)
            cur = conn.cursor()
            count = cur.execute(sql)

            results = cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            exit
        return [count, results]

    @classmethod
    def mysql_update(cls, sql):
        try:
            print "Connecting to mysql server..."
            conn = MySQLdb.connect(read_default_file=cls.config)
            cur = conn.cursor()
            count = cur.execute(sql)
            conn.commit()
            cur.close()
            conn.close()

        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            exit
        return count

    @classmethod
    def mysql_update_many(cls, sqls):
        try:
            print "Connecting to mysql server..."
            conn = MySQLdb.connect(read_default_file=cls.config)
            cur = conn.cursor()
            for sql in sqls:
                count = cur.execute(sql)
            conn.commit()
            cur.close()
            conn.close()

        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            exit
        return count

    @classmethod
    def set_default_file(cls, file="my.cnf", relative=True):
        if(relative):
            os.path.split(os.path.realpath(__file__))[0] + os.sep + file
        else:
            cls.config = file

pass

if __name__ == "__main__":
    MySQLAdapter.set_default_file()
    count_and_results = MySQLAdapter.mysql_select(
        "SELECT * FROM `st_visitors` limit 0, 1")
    print count_and_results[1]

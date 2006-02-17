#!/usr/bin/python
# -*- coding: utf-8 -*-
# This script scans a file for special WIN1252 characters that are NOT in
# ISO-8859-1. It then replaces those characters with their UTF-8 equivalent.
# It is assumed that the rest of the file is already in UTF-8.
# Oh, and it removes character-return also.

import string,sys,os

transmap = {}

transmap[13] = u""
transmap[0x84] = u"„"
transmap[0x8a] = u"Š"
transmap[0x8c] = u"Œ"
transmap[0x8e] = u"Ž"
transmap[0x91] = u"‘"
transmap[0x92] = u"’"
transmap[0x93] = u"“"
transmap[0x94] = u"”"
transmap[0x96] = u"–"
transmap[0x9a] = u"š"
transmap[0x9c] = u"œ"
transmap[0x9e] = u"ž"


for file in sys.argv[1:]:
    print "Doing %s" % file
    infile = open(file)
    str=unicode(infile.read(),'utf-8')
    str = str.translate(transmap)
    outfile = open("temp",'w')
    outfile.write(str.encode('utf-8'))

    infile.close()
    outfile.close()
    os.remove(file)
    os.rename("temp",file)


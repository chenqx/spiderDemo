# -*- coding: utf-8 -*-
'''
data process after crawling, Created on Oct, 2014
#version: 
#author: chenqx
See more: http://chenqx.github.com
'''


from lxml import etree
from ConfigParser import ConfigParser

class dataProcess:
    def __init__(self, source_filename, target_filename):
        # load stop words into the memory.
        fin = open(source_filename, 'r')

        read = fin.read()

        output = open(target_filename, 'w')
        output.write(read)

        fin.close()
        output.close()



##if __name__ == '__main__':
##
##    dataProcess('D:/Python27/src/bbs/bbsData.xml', 'D:/Python27/src/bbs/text.txt')

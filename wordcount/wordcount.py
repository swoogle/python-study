#! /usr/bin/env python3
#! _*_ coding: utf-8 _*_

import re
import sys
import os.path as op
from collections import Counter

# wordcount 给定一篇英文文档（input.txt），统计其中单词词频，将结果输入到文件中（output.txt)

with open(op.join(sys.path[0], 'input.txt')) as fi:
	words = fi.read().lower()
fi.close()
	
pattern = re.compile(r'[a-zA-Z]+\-?[a-zA-Z]*') #判断是否为英文单词
word_list = Counter(pattern.findall(words))

with open(op.join(sys.path[0], 'output.txt'), 'w') as fo:
	for word in word_list.most_common():
		fo.write("%s -> %d\n" % word)
fo.close()
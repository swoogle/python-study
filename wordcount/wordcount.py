#! /usr/bin/env python3

import re
from collections import Counter

# wordcount 给定一篇英文文档（input.txt），统计其中单词词频，将结果输入到文件中（output.txt)

fi = open('input.txt')
words = fi.read().lower()
fi.close()
	
pattern = re.compile(r'[a-zA-Z]+\-?[a-zA-Z]*') #判断是否为英文单词
word_list = Counter(pattern.findall(words))

with open('output.txt', 'w') as fo:
	for word in word_list.most_common():
		fo.write("%s -> %d\n" % word)
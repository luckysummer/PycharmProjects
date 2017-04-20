#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os, gzip
dir_path = '/home/ll/work/work-before/literature-based similarity/compounds/DUD'
result_dict = {}
fileName_ls = os.listdir(dir_path)
for fileName in fileName_ls:


    filePath = os.path.join(dir_path, fileName)
    with gzip.open(filePath, 'rb') as data:
        count = len(data.readlines())
        result_dict[filePath] = count
result = sorted(result_dict.items(), key=lambda d: d[1])
print result


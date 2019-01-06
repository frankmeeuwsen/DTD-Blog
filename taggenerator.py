#!/usr/bin/env python

'''
tag_generator.py

Copyright 2017 Long Qian
Contact: lqian8@jhu.edu

This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.
'''

import glob
import os
import frontmatter
from pprint import pprint

post_dir = '_posts/'
tag_dir = 'tag/'

filenames = glob.glob(post_dir + '*.m*d*')

total_tags = []
for filename in filenames:
    f = open(filename, 'r')
    post = frontmatter.load(f)
    if 'tags' in post.metadata and type(post.metadata['tags']) is str:
        # print("STR: "+post['title']+":"+post.metadata['tags'])
        current_tags = post.metadata['tags'].split()
        total_tags.extend(current_tags[1:])
    if 'tags' in post.metadata and type(post.metadata['tags']) is list:
        # print("LST: "+post['title']+": ".join(post.metadata['tags']))
        for i in range(len(post.metadata['tags'])):
            # print("tag:"+post.metadata['tags'][i])
            total_tags.append(post.metadata['tags'][i])
            
    f.close()
total_tags = sorted(set(total_tags))
print(total_tags)
old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)
    
if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

for tag in total_tags:
    tag_filename = tag_dir + tag + '.md'
    f = open(tag_filename, 'a')
    write_str = '---\nlayout: tagpage\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag + '\nrobots: noindex\n---\n'
    f.write(write_str)
    f.close()
print("Tags generated, count", total_tags.__len__())

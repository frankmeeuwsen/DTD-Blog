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

post_dir = '_posts/'
tag_dir = 'tag/'


filenames = glob.glob(post_dir + '*m*d*')

total_tags = []
for filename in filenames:
    post = frontmatter.load(filename)
    if 'tags' in post.keys():
        # print(post['title'])
        # print(filename)
        print(post['tags'])
        if post['tags'] is not None:
            total_tags.extend(post['tags'])
    
total_tags = set(total_tags)

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

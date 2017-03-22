#!/usr/bin/env python
#-*- coding: utf-8 -*-

# from wordpress_xmlrpc import Client, WordPressPost, WordPressTerm
# from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
# from wordpress_xmlrpc.methods.users import GetUserInfo
# from wordpress_xmlrpc.methods import taxonomies
# import csv
#
# wp = Client('http://log4geek.cc/xmlrpc.php', 'user', 'password')
#
# """
# 发表博文
# """
# post = WordPressPost()
# post.title = 'My new title'
# post.content = 'This is the body of my new post.'
# post.post_status = 'publish'
# post.terms_names = {
#     'post_tag': ['test', 'firstpost'], #标签
#     'category': ['Introductions', 'Tests'] #分类目录
# }
#
# wp.call(NewPost(post))

'''
新建tag或者category
'''
# from wordpress_xmlrpc import Client, WordPressPost, WordPressTerm
# from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
# from wordpress_xmlrpc.methods.users import GetUserInfo
# from wordpress_xmlrpc.methods import taxonomies
# import csv
#
#
# wp = Client('http://127.0.0.1/xmlrpc.php', 'user', 'password')
#
# tag = WordPressTerm()
# tag.taxonomy = 'category'#这里为category的话插入的是category，为post_tag的话插入的是tag
# tag.name = 'My New Tag'
# tag.id = wp.call(taxonomies.NewTerm(tag))

'''
新建带有父category/tag的子category/tag
'''
# child_cat = WordPressTerm()
# child_cat.taxonomy = 'category'#这里为category的话插入的是category，为post_tag的话插入的是tag
# child_cat.parent = parent_cat.id
# child_cat.name = 'My Child Category'
# child_cat.id = client.call(taxonomies.NewTerm(child_cat))

def test():
    a,b=0,1;
    while b<10000000:
        print(b,end=",");
        a,b=b,a+b;

#test();

def testInput():
    inputstr=input("please input:")
    print("your input is :"+inputstr);

testInput();
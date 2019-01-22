#-*- coding:utf-8 -*-

import requests
import sys
import io
def Login(func):
    """
	登录装饰器，登录时请求登录保存COOKIE，访问其他页面可以跳过认证。
	"""
    def wraper(jira_id,comment):
        data = {
            'os_username': 'bobtthp',
            'os_password': 'bobtthp'
        }
        login_url = 'http://xxx:xx/login.jsp'
        headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
        cookie = requests.post(login_url,headers=headers,data=data).cookies
        func(jira_id,comment,cookie)
    return wraper
@Login
def Add_comment(jira_id,comment,cookie):
    """
	请求JIRA接口，增加评论，直接调用这个方法参数需要传入JIRA id和评论内容。
	"""
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    data_url = 'http://xxx:xx/rest/api/2/issue/%s/comment' % (jira_id)
    add_comments = requests.post(data_url,headers=headers,cookies=cookie,json={'body':comment})
    return add_comments.status_code


if __name__ == '__main__':
    print sys.argv
    jira_id = sys.argv[1]
    comment_file = sys.argv[2]
    with io.open(comment_file,'r',encoding='utf-8') as f:
        comment = f.read()
    Add_comment(jira_id,comment)


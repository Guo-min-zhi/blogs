#!/usr/bin/env python
# coding: utf-8


prefix = 'controllers.blog.'

urls = (
	'/',              prefix+'Index',
	'/view/(\d+)',    prefix+'View',
	'/new',           prefix+'New',
	'/edit/(\d+)',    prefix+'Edit',
	'/delete/(\d+)',  prefix+'Delete',
)

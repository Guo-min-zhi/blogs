#!/usr/bin/env python
# coding: utf-8

import web
from configs.url import urls

app = web.application(urls, globals())

if __name__ == "__main__":
	app.run()



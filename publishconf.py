#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# SITEURL = 'http://redearthfarms.org'
SITEURL = 'http://org-redearthfarms-test.s3-website-us-east-1.amazonaws.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Since SITEURL is different in publish mode, need to regen menu items and
# side bar images
MENUITEMS = makemenuitems(MENUITEMS, SITEURL)
BARIMGS = makebarimgs(SITEURL)
# JSON array string to simplify use in templates
BARIMGSJSON = json.dumps(BARIMGS)

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

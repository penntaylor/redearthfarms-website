#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import glob
import os.path
from pathlib import Path
import json

AUTHOR = 'REF'
SITENAME = 'Red Earth Farms'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PAGE_PATHS = ['']
ARTICLE_PATHS = []
STATIC_PATHS = ['docs', 'images']

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

THEME = 'themes/refgold'

################################################################################
# Items in the main navigation menu on the left-hand side of the page

MENUITEMS=(('Home', 'index.html'),
           ('About', 'about.html'),
           ('History', 'history.html'),
           ('Who We Are', 'who-we-are.html'),
           ('Our Land', 'our-land.html'),
           ('Cooperatives', 'cooperatives.html'),
           ('Visiting', 'visiting.html'),
           ('Internships', 'internships.html'),
           ('Documents', 'documents.html'),
           ('Contact Us', 'contact-us.html'))

# Add SITEURL to head of menuitems
def makemenuitems(menuitems, siteurl):
    prefix = (siteurl + '/') if siteurl else ''
    return tuple([(label, prefix + url) for (label, url) in menuitems])

MENUITEMS = makemenuitems(MENUITEMS, SITEURL)
################################################################################



################################################################################
# Images for the sidebar
#
# Grab all files in sidebar image dir
root = os.path.dirname(os.path.realpath(__file__))
contentpath = Path(root) / Path(PATH)
imgs = glob.glob(contentpath.as_posix() + "/images/sidebar/*.*")
rimgs = [Path(x).relative_to(contentpath).as_posix() for x in imgs]
# Munge paths to output location of images -- strips 'content/' from head and re-homes to SITEURL
def makebarimgs(siteurl):
    prefix = (siteurl + '/') if siteurl else ''
    return [prefix + f for f in rimgs]

BARIMGS = makebarimgs(SITEURL)
# JSON array string to simplify use in templates
BARIMGSJSON = json.dumps(BARIMGS)
###############################################################################


# Generate the image bar javascript file from its own template
TEMPLATE_PAGES = {'img-bar.js': 'theme/js/img-bar.js'}


DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

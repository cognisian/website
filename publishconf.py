# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

DEBUG=False
# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://artificialbelligerence.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

#OVERRIDE Location of theme, the repos will be checked out
# during GitHub Action
#THEME = 'GITHUB_ACTION_THEME_LOC'
THEME = 'themes/pelican-bootstrap3'
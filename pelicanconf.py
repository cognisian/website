DEBUG=True
AUTHOR = 'Sean Chalmers'
SITENAME = 'ArtificialBelligerence'
SITESUBTITLE='Programmer, Developer of Code'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Toronto'
DEFAULT_LANG = 'en'

PLUGIN_PATHS = [
    "/home/schalmers/Projects/pelican-plugins",
    "plugins"
]
PLUGINS = ["sitemap", 'i18n_subsites']

# sitemap plugin settings
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    }
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = 'posts/{category}/{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = 'posts/{category}/{date:%Y}/{date:%m}/{slug}/index.html'

PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

# Turn off the author, category, tags pages
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''
TAG_URL = ''
TAG_SAVE_AS = ''

# Turn off the author, category, tags archive pages
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''

STATIC_PATHS = [
    'theme/images',
    'theme/css',
    'extra/robots.txt',
]

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {
            'path': 'robots.txt'
    },
}

#
# THEME
#
HIDE_SIDEBAR=True
THEME = '/home/schalmers/Projects/pelican-themes/pelican-bootstrap3'
THEME_TEMPLATES_OVERRIDES = ['template']
BOOTSTRAP_THEME = 'flatly'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

FAVICON = ''
SITELOGO = ''
SITELOGO_SIZE = 0 #width
BANNER = ''
BANNER_SUBTITLE = 'Programmer, Developer of Code'
BANNER_ALL_PAGES = False

BOOTSTRAP_NAVBAR_INVERSE = False
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = False

DEFAULT_PAGINATION = 10

# MENU
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Home', '/'),
    ('Writing', '/pages/poetry.html'),
    ('Resume', '/pages/resume.html'),
)

GITHUB_URL = 'https://github.com/cognisian'

LINKS = (
    ('Python.org', 'https://www.python.org/'),
    ('Pelican', 'https://getpelican.com/'),
    ('Theme', 'https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3'),
)

# Social widget
DISABLE_SIDEBAR_TITLE_ICONS = False
SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/in/seanchalmers'),
    ('github', GITHUB_URL),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True

CUSTOM_CSS='theme/css/main.css'
NAME = 'Sean Chalmers'
TAGLINE = 'Programmer, Developer of Code'
PIC = 'Upwork_Profile.png'

#sidebar links
EMAIL = 'seandchalmers@yahoo.ca'
PHONE = '(289) 681-2048'
LINKEDIN = 'seanchalmers'
GITHUB = 'cognisian'

CAREER_SUMMARY = 'I am an experienced full-stack programmer, with more than 20 years of experience, developing applications for the web and in the financial services industry.  Strong communication and organizational skills.  Proven abilities of innovation, problem resolution and comprehension of complex technical information.'

SKILLS = [
    {
        'title': 'OS',
        'items': [
            'Linux: Gentoo, Ubuntu, Red Hat',     
            'Microsoft: Windows',
            'IBM: OS/400'
    ]}, {
        'title': 'Language',
        'items': [
            'PHP, Java, Python, Bash, Perl, JavaScript, C/C++, COBOL'
    ]}, {
        'title': 'Build Tools',
        'items': [
            'Maven, Autotools, Pip, Composer, Meson, Gradle'
    ]}, {
        'title': 'Databases',
        'items': [
            'OSS: MariaDB, PostgreSQL, SQLite',
            'Oracle: MySQL, Oracle Database',
            'Microsoft: SQL Server',
            'IBM: DB/2'
    ]}, {
        'title': 'VCS',
        'items': [
            'Git, Subversion'
    ]}, {
        'title': 'Web',
        'items': [
            'Apache Server, Apache Geronimo, Wordpress, jQuery, HTML/CSS, Pelican'
    ]}, {
        'title': 'Other',
        'items': [
            'Nagios, Groundworks, ActiveMQ, LogRhythm, OSSEC IDS'
    ]}
]

EXPERIENCES = [{
        'job_title': 'Personal Leave',
        'time': '2018',
        'company': 'Personal',
        'details': 'Took personal time to recharge and investigate other pursuits.  Audited courses in Math, History and Philosophy.  Travelled.'    
    }, {
        'job_title': 'WordPress Consultant',
        'time': '2016 - 2018',
        'company': 'nomadreader.com, Remote',
        'details': 'Developed a WordPress PHP plugin and Google Chrome plugin to easily import and export to CSV, to view and the book data from Amazon and the associated additonal meta-data created by web site owner. This reduced the website operator\'s reliance on the Amazon book web service as well as allowing offline editing and importing of updated information.'
    }, {
        'job_title': 'Business Application Monitoring Specialist',
        'time': '2008 - 2016',
        'company': 'Symcor, Mississauga, ON',
        'details': 'Maintained Groundworks (based on Nagios monitoring system) a multi-site, geographically distributed monitoring system containing 1,500 servers and 40,000 monitored services along with the suite of provided and custom monitoring scripts.  Designed and developed a multi-site, distributed monitoring system (Java Message Service on Geronimo J2EE server) to support the ticket request load. Previously, the system would crash weekly losing advanced notice of potential client impacting technical issues. The current system was robust and had at most 2 to 3 crashes per year and any queued events would be forwarded to ticketing system, minimizing the number of lost events.'
    }, {
        'job_title': 'Joomla Consultant',
        'time': '2008 - 2016',
        'company': 'Toucan Search &amp; Selection, Burlington, ON',
        'details': 'Designed and integrated in Joomla a candidate profile submission form, a candidate search engine and email notification system using MySQL, PHP and JavaScript. This reduced the administrative tasks performed by company\'s recruiters by 80% through automation of the candidate information submission and notification process. '
    }, {
        'job_title': 'Web Consultant',
        'time': '2005 - 2007',
        'company': 'milkaudio.com, Burlington, ON',
        'details': 'Created Linux shell scripts to convert web site content from Server Side Include directives to PHP scripts.  This was done to incorporate PHP scripts to perform banner rotation.  Added PayPal payment processing, allowing the web site to sell tickets to Milk club events, using PHP and PayPal\'s Instant Payment Notification and Payment Data Transfer APIs.'
    }, {
        'job_title': 'Programmer Analyst',
        'time': '2001 - 2002',
        'company': 'Odeka, Toronto, ON',
        'details': 'Maintained and enhanced a large and complex investment planning software using data structures in Access and coding in VB 6.0.  Provided input to technical specifications reviews to ensure that projects met business requirements.  Documented programs as per project standards and created specifications and technical documents, as required.'
    }, {
        'job_title': 'Programmer Analyst',
        'time': '2000 - 2001',
        'company': 'Corporate Communications Interactive, Toronto, ON',
        'details': 'Maintained and enhanced a large and complex mutual fund reporting software using data structures in Access and coding in VB 6.0.  Created a tax reporting application submitting tax information files and tax statements using standards set by the Canada Customs and Revenue Agency (CCRA) using VB and data contained within Access database to the CCRA.  The tax statements were designed using ActiveReport report control.  As part of a design group, provided technical analysis and technical specifications to rewrite the software to use SQL Server 2000.  Coded, documented, tested and wrote the specifications for the new VB program and SQL Server stored procedures according to project standards.  Coded, documented and tested a support program to automate the distribution of new upgrades of the software using Visual C++ according to project standards.'
    }, {
        'job_title': 'Programmer Analyst',
        'time': '1996 - 2000',
        'company': 'Onlie Financial Services, Toronto, ON',
        'details': 'Maintained and enhanced the retail banking software based on the AS/400 platform using COBOL with the data stored in a combination of flat files and DB2 tables.  Maintained and enhanced a GUI front end to the AS/400 banking software based on PC’s using VB with the data stored in a SQL Server database.  Coded, documented, tested and wrote the specifications for a new internet banking software using DTS components written in VB 6.0 with the GUI written in ASP and interfacing the SQL Server database’s stored procedures and client data according to project standards.  Provided 24 hours a day 7 days a week phone based technical assistance to the client for the AS/400 and PC hardware and software platforms.  Provided on site technical support to clients in British Virgin Islands, Trinidad & Tobago and Singapore.'
    }
]

EDUCATIONS = [{
        'degree': 'Bachelor of Science – Computer Information Systems (With Distinction)',
        'meta': 'Athabasca University',
        'time': '2003 - 2006'
    }
]

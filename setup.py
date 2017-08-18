from distutils.core import setup
setup(
  name = 'iplookup',
  packages = ['iplookup'], # this must be the same as the name above
  version = '0.1',
  description = 'Module for looking up IPs from Domain Names',
  author = 'Darren Gibbard',
  author_email = 'dalgibbard@gmail.com',
  url = 'https://github.com/dalgibbard/iplookup', # use the URL to the github repo
  download_url = 'https://github.com/dalgibbard/iplookup/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['dns', 'ip', 'lookup', 'iplookup'], # arbitrary keywords
  install_requires = [
    "dnspython",
  ],
  classifiers = [
    "Intended Audience :: Developers",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Topic :: Software Development :: Libraries :: Python Modules",
  ],
)

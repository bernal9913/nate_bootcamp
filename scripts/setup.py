from distutils.core import setup
import zipfile
import py2exe
import os, random
from pathlib import Path
from time import sleep
from random import randrange
import sqlite3
import re
import glob

setup(zipfile = None, options = {'py2exe':{"bundle_files": 1}} , windows = ["hackerscript.py"])
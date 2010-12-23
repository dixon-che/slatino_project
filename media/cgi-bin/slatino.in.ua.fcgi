#!/bin/env python
# -*- coding: utf-8 -*-
import sys, os

# Add a custom Python path.
sys.path.insert(0, "/var/www/slatino/www.slatino.in.ua/")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "slatino.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(["method=threaded", "daemonize=false"])

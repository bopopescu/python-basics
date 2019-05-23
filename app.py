#!/usr/bin/env python

from src import app as application
import logging
logging.basicConfig(level=logging.INFO)

application.run(debug=True,host='0.0.0.0')


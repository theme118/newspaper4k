# -*- coding: utf-8 -*-

__title__ = 'newspaper'
__version__ = '0.0.1'
__author__ = 'Lucas Ou-Yang'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014 Lucas Ou-Yang'

from . import utils
from .api import build, popular_urls, build_article

from .settings import VERSION



# Set default logging handler to avoid "No handler found" warnings.
import logging

try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
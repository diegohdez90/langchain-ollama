"""Logging configuration for the module.
"""

import os
import logging
LOG = logging.getLogger(__name__)

# Create console handler
ch = logging.StreamHandler()

# Set log level based on environment
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development').lower()
if ENVIRONMENT == 'development':
    ch.setLevel(logging.DEBUG)
    LOG.setLevel(logging.DEBUG)
else:
    ch.setLevel(logging.WARNING)
    LOG.setLevel(logging.WARNING)

# Create formatter
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
ch.setFormatter(formatter)

LOG.addHandler(ch)

__all__ = [
    'LOG'
]

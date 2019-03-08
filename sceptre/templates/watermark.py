#!/usr/bin/env python3
"""
generate a watermark

Usage:
  watermark.py

Arguments:

Option:
  -h        Show this screen.
  -v --version        Show version.
"""

import git
import boto3


def repo():
    repo = git.Repo(search_parent_directories=True)
    return repo


def gci():
    gci = boto3.client('sts').get_caller_identity()
    return gci

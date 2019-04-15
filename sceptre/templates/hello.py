#!/usr/bin/env python3
"""
make some sample resources

Usage:
  sample.py

Arguments:

Option:
  -h        Show this screen.
  -v --version        Show version.
"""

from troposphere import Template


from cloudseeder import (
    bucket,
    watermark
)


class GetMeABucket(object):
    def __init__(self, sceptre_user_data):
        self.template = Template()
        self.sceptre_user_data = sceptre_user_data
        self.repo = watermark.repo()
        self.app_env = watermark.app_env(
            self.sceptre_user_data["app"],
            self.sceptre_user_data["env"]
        )
        self.my_description()
        self.my_bucket()

    def my_description(self):
        watermark.set_desc(
            self.template,
            self.app_env + " get me a bucket stack. "
        )

    def my_bucket(self):
        mytags = watermark.create_tags(
            self.sceptre_user_data["app"],
            self.sceptre_user_data["env"],
            self.sceptre_user_data["team"],
            self.repo.remotes.origin.url
        )
        bucket.add_bucket(
            mytags,
            self.template,
            self.sceptre_user_data["bucket_versioning"]
        )


def sceptre_handler(sceptre_user_data):
    mybucket = GetMeABucket(sceptre_user_data)
    return mybucket.template.to_json()

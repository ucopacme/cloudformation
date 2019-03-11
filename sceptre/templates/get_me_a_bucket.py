#!/usr/bin/env python3
"""
get me a bucket

Usage:
  get_me_a_bucket.py

Arguments:

Option:
  -h        Show this screen.
  -v --version        Show version.
"""

from troposphere import (
    GetAtt,
    Join,
    Output,
    Parameter,
    Ref,
    Split,
    Sub,
    Tags,
    Template,
)


from troposphere.s3 import (
    Bucket,
    VersioningConfiguration
)

import watermark


class GetMeABucket(object):
    def __init__(self, sceptre_user_data):
        self.template = Template()
        self.sceptre_user_data = sceptre_user_data
        self.repo = watermark.repo()
        self.app_env = self.sceptre_user_data["app"] + "-" + self.sceptre_user_data["env"]
        self.add_description()
        self.add_bucket()

    def add_description(self):
        self.description = self.template.set_description(
            self.sceptre_user_data["template_prefix"] + ' ' + self.app_env +
            " get me a bucket stack. " +
            self.sceptre_user_data["template_postfix"]
        )

    def add_bucket(self):
        self.bucket = self.template.add_resource(
            Bucket(
                "GetMeABucket",
                DeletionPolicy="Retain",
                Tags=Tags(
                    app=self.sceptre_user_data["app"],
                    env=self.sceptre_user_data["env"],
                    team=self.sceptre_user_data["team"],
                    repo=self.repo.remotes.origin.url,
                ),
                VersioningConfiguration=VersioningConfiguration(
                    Status=self.sceptre_user_data["bucket_versioning"],
                )
            )
        )
        self.template.add_output(
            Output(
                "BucketName",
                Description="Bucket name",
                Value=Ref(self.bucket)
            )
        )
        self.template.add_output(
            Output(
                "BucketNameARN",
                Description="Bucket name Arn",
                Value=GetAtt(self.bucket, "Arn")
            )
        )


def sceptre_handler(sceptre_user_data):
    bucket = GetMeABucket(sceptre_user_data)
    return bucket.template.to_json()

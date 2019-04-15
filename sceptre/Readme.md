# Cloudformation generation and deployment with sceptre


## Dependencies

You'll need to install the boiler plate cloudformation helper

```
pip install git+https://github.com/ucopacme/cloudseeder.git -U

```

Generate a template:

```
sceptre --var "prj=hello" --var "team=my-team" --var "app=my-bucket" --var "region=us-west-2"   --var "iam_role="  --var-file config/variables.yaml generate-template test hello | jq .
{
  "Description": "Sceptre managed infrastructure. Please use sceptre to configure the resources in this my-bucket-test get me a bucket stack.  Designed by UCOP Applied Cloud Management and Engineering in Oakland, California. patent pending.",
  "Outputs": {
    "BucketName": {
      "Description": "Bucket name",
      "Value": {
        "Ref": "GetMeABucket"
      }
    },
    "BucketNameARN": {
      "Description": "Bucket name Arn",
      "Value": {
        "Fn::GetAtt": [
          "GetMeABucket",
          "Arn"
        ]
      }
    }
  },
  "Resources": {
    "GetMeABucket": {
      "DeletionPolicy": "Retain",
      "Properties": {
        "PublicAccessBlockConfiguration": {
          "BlockPublicAcls": "true",
          "BlockPublicPolicy": "true",
          "IgnorePublicAcls": "true",
          "RestrictPublicBuckets": "true"
        },
        "Tags": [
          {
            "Key": "app",
            "Value": "my-bucket"
          },
          {
            "Key": "env",
            "Value": "test"
          },
          {
            "Key": "repo",
            "Value": "git@github.com:ucopacme/cloudformation.git"
          },
          {
            "Key": "team",
            "Value": "my-team"
          }
        ],
        "VersioningConfiguration": {
          "Status": "Suspended"
        }
      },
      "Type": "AWS::S3::Bucket"
    }
  }
}
```

Launch a template:

```
sceptre --var "prj=hello" --var "team=my-team" --var "app=my-bucket" --var "region=us-west-2"   --var "iam_role="  --var-file config/variables.yaml launch-stack test hello
```

Launch an environement:

```
sceptre --var "prj=hello" --var "team=my-team" --var "app=my-bucket" --var "region=us-west-2"   --var "iam_role="  --var-file config/variables.yaml launch-env test 
```

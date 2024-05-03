## Introduction

Infra_tool is a CLI tool to host static website on Amazon S3 bucket. And,
uses cloudfront distribution to serve as CDN for this website.

## Steps to run the application

NOTE: 

- Before you run the application. Please ensure that cloudformation stack
is clean. And, no bucket exists on AWS with the same bucket name. If bucket exists, manually delete the bucket from the interface.
- Sitename that we give in command line. Will be the bucket name on S3. 
- Before you run the command. Activate the python virtual environment.

```
source .venv/bin/activate
python3 -m pip install -r requirements.txt

```
## Command to run the application

```
python3 infra_tool.py --command create --sitename xyz.tattle.co.in --path <mention the directory path>
```

## File details

- `tool.py` - Contains the logic for parsing the command line arguments. Internally, call `cdk deploy` with arguments. `cdk deploy --context key=value --context key=value`.
- `app.py` - This is the entry point of the application. 
- `static_website_create_stack.py` - contains logic that creates stack, creates S3 bucket, deploys the buckets, uploads the website assets, adds CDN.
- `website_assets` - folder contains files that are to be uploaded on S3 and made live.

## Sample Website Live.
- https://d1zwwcu2xtieml.cloudfront.net


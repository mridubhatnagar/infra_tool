#!/usr/bin/env python3
import aws_cdk as cdk
from constructs import Construct
class StaticWebsiteStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, sitename:str, path:str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        website_bucket = cdk.aws_s3.Bucket(self, sitename,
            website_index_document="index.html",
            public_read_access=True,
            bucket_name=sitename,
            block_public_access=cdk.aws_s3.BlockPublicAccess(block_public_acls=False, block_public_policy=False, ignore_public_acls=False, restrict_public_buckets=False),
            removal_policy=cdk.RemovalPolicy.DESTROY  
        )

        bucket_policy = cdk.aws_iam.PolicyStatement(
            actions=["s3:PutObject", "s3:GetObject"],
            resources=[f"{website_bucket.bucket_arn}/*"],
            principals=[cdk.aws_iam.AnyPrincipal()],
            effect=cdk.aws_iam.Effect.ALLOW
        )
        website_bucket.add_to_resource_policy(bucket_policy)
        
        # Define the file to upload
        cdk.aws_s3_deployment.BucketDeployment(self, "DeployStaticWebsite",
            sources=[cdk.aws_s3_deployment.Source.asset(path)],  # Path to your local website files
            destination_bucket=website_bucket
        )
        
        cloudfront_distribution = cdk.aws_cloudfront.CloudFrontWebDistribution(self, "StaticWebsiteDistribution",
            origin_configs=[
                cdk.aws_cloudfront.SourceConfiguration(
                    s3_origin_source=cdk.aws_cloudfront.S3OriginConfig(
                        s3_bucket_source=website_bucket
                    ),
                    behaviors=[cdk.aws_cloudfront.Behavior(is_default_behavior=True)]
                )
            ]
        )

        cdk.CfnOutput(self, "BucketWebsiteURL",
            value=website_bucket.bucket_website_url
        )

        cdk.CfnOutput(self, "BucketName", 
                      value=website_bucket.bucket_name, 
                      export_name="bucketname")


        cdk.CfnOutput(self, "CloudFrontURL",
            value=cloudfront_distribution.distribution_domain_name,
            description="CloudFront Distribution URL"
        )
        


from aws_cdk import (
    Stack,
    aws_ecs as ecs,
    aws_ecr as ecr,
    aws_route53 as route53,
    aws_certificatemanager as acm,
    aws_ecs_patterns as ecs_patterns,
)
from constructs import Construct

class WanderarAdminInfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define the ECS cluster
        cluster = ecs.Cluster(self, "WanderarAdminCluster")

        # Define the ECR repository
        repo = ecr.Repository(self, "WanderarAdminRepo")

        # # Define the ECS service and task definition
        # ecs_service = ecs_patterns.ApplicationLoadBalancedFargateService(self, "WanderarAdminService",
        #     cluster=cluster,
        #     task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
        #         image=ecs.ContainerImage.from_ecr_repository(repo)
        #     )
        # )

        # # Define the Route53 record for the custom domain
        # route53.ARecord(self, "WanderarAdminDomainRecord",
        #     zone=route53.HostedZone.from_lookup(self, "Zone", domain_name="getwanderar.com"),
        #     record_name="admin",
        #     target=route53.RecordTarget.from_alias(ecs_service.load_balancer)
        # )

        # # Define the ACM certificate (replace 'certificateArn' with your actual certificate ARN)
        # cert_arn = "arn:aws:acm:us-east-1:801538786051:certificate/9a9792dd-3fa5-414f-9a99-b120d03824a5" # replace with your actual certificate ARN
        # acm.Certificate.from_certificate_arn(self, "WanderarAdminCertificate", certificate_arn=cert_arn)
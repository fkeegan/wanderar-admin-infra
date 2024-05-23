from aws_cdk import (
    Stack,
    CfnOutput,
    aws_ecs as ecs,
    aws_ecr as ecr,
    aws_route53 as route53,
    aws_certificatemanager as acm,
    aws_ecs_patterns as ecs_patterns,
    aws_elasticloadbalancingv2
)
from constructs import Construct

class WanderarAdminInfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Import the existing ACM certificate
        certificate = acm.Certificate.from_certificate_arn(self, "Certificate",
            certificate_arn="arn:aws:acm:us-east-1:801538786051:certificate/9a9792dd-3fa5-414f-9a99-b120d03824a5"
        )

        # Define the ECS cluster
        cluster = ecs.Cluster(self, "WanderarAdminCluster")

        # Define the ECR repository
        repo = ecr.Repository(self, "WanderarAdminRepo")

        # Define the ECS service and task definition
        ecs_service = ecs_patterns.ApplicationLoadBalancedFargateService(self, "WanderarAdminService",
            cluster=cluster,
            public_load_balancer=False,
            # protocol=aws_elasticloadbalancingv2.ApplicationProtocol.HTTPS,
            # certificate=certificate,
            # domain_name="admin.getwanderar.com",
            # domain_zone=hosted_zone,
            # redirect_http=True,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_ecr_repository(repo),
                container_port=5173
            )
        )

        # Print the DNS name of the load balancer
        CfnOutput(self, "LoadBalancerDNSName", value=ecs_service.load_balancer.load_balancer_dns_name)
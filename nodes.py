# Author :- Dheeraj Choudhary

from diagrams import Diagram
from diagrams.aws.network import VPC
from diagrams.aws.network import VPCRouter
from diagrams.aws.network import VPCPeering
from diagrams.aws.network import VPCElasticNetworkInterface
from diagrams.aws.compute import EC2
from diagrams.aws.compute import EC2Instance
from diagrams.aws.compute import EC2Instances
from diagrams.aws.compute import EC2Ami
from diagrams.aws.compute import LambdaFunction
with Diagram("Diagram", direction="LR"):
    VPC = VPC("VPC")
    VPCRouter = VPCRouter("VPCRouter")
    VPCPeering = VPCPeering("VPCPeering")
    VPCElasticNetworkInterface = VPCElasticNetworkInterface("VPCElasticNetworkInterface")
    EC2 = EC2("EC2")
    EC2Instance = EC2Instance("EC2Instance")
    EC2Instances = EC2Instances("EC2Instances")
    EC2Ami = EC2Ami("EC2Ami")
    LambdaFunction = LambdaFunction("LambdaFunction")

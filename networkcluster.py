# Author :- Dheeraj Choudhary
from diagrams import Cluster, Diagram
from diagrams.aws.network import VPC
from diagrams.aws.network import VPCRouter
from diagrams.aws.network import VPCPeering
from diagrams.aws.network import VPCElasticNetworkInterface
with Diagram("Diagram", direction="TB"):
    with Cluster("Network Cluster"):
        VPCPeering = VPCPeering("VPCPeering")
        VPCElasticNetworkInterface = 
        VPCElasticNetworkInterface("VPCElasticNetworkInterface")
        VPCRouter = VPCRouter("VPCRouter")
        VPC = VPC("VPC")

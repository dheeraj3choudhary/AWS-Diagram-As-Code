# Author :- Dheeraj Choudhary
from diagrams import Cluster, Diagram, Edge
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Diagram", show= True, direction="TB"):
    ELB("") >> Edge(color="red", label="Traffic") >> \
    [EC2("Instance1"),EC2("Instance2"),EC2("Instance3")]

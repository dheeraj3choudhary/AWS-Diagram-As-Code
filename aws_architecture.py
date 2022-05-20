# Author :- Dheeraj Choudhary
from diagrams import Cluster, Diagram
from diagrams.aws.database import RDS
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53

with Diagram("Simple Web Service with DB Cluster", show=True, direction="TB"):
    Web_LB = ELB("Web_Load_Balancer")
    App_LB = ELB("App_Load_Balancer")
    DNS= Route53("Route53")
    DB = RDS("Database")

    with Cluster("Web Teir"):
        web_teir = [EC2("NginxProxy"),
                   EC2("NginxProxy1"),
                   EC2("NginxProxy2")]
    with Cluster("App Teir"):
        app_teir = [EC2("app1"),
                   EC2("app2"),
                   EC2("app3")]


    DNS >> Web_LB >> web_teir
    web_teir >> App_LB
    App_LB >> app_teir
    app_teir >> DB

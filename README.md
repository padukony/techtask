# techtask

Technical Challenge:

Task1: Design of 3 tier environment:
- This 3 tier environment architecture is based on AWS cloud services
- Create separate VPC (Virtual Private Cloud) to isolate all the resources belong to the application.
- Create 3 private subnets to keep web,application and DB instances/VMs/services.
- Create 1 public subnet to for Bastion host(used to ssh to all hosts which are in private subnet) & NAT Gateway for all private instances to 
communicate to Internet for patch upgrade etc.
- Create EC2 (Elastic Cloud Computing) Instances for Web and application tier under Auto Scaling group.
- Create RDS for DB Tier and with Multi Availabitlity Zone configuration for High Availability.
- Configure Route53 DNS service with domain name of the web application and point to Static IP address (Elastic IP) of Elastic Load Balancer(ELB).
- Configure Elastic Load Balancer between Web and Application tier to support scalability of Application tier.


Task2: Write code that will query the meta data of an instance within AWS and provide a json formatted output. 
get_aws_ec2_metadata.py
- This is a python code that will query the metadata of an AWS EC2 instance and provide a json formatted output.
- This will give all metadata output in one short by passing "all" argument otherwise specific metadata value 
  can be retrieved by passing correct metadata key while executing this code.
- This python program should be executed using python3 on any AWS EC2 instance
- Execute as below by passing argument:\
  eg: $ python3 get_aws_ec2_metadata.py all\
      $ python3 get_aws_ec2_metadata.py network

Task3: Write a function that you pass in the nested json object and a key and get back the value
nested_object.py
-  This is a python code to get the value for specific key in nested json object
-  Nested json object and key is hardcoded in the main method
-  Execute as below by changing the key in the program:\
    eg: $ python3 nested_object.py

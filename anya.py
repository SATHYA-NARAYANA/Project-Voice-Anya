#!/usr/bin/python3
import os 
print("Welcome to Menu Program of Voice ANYA")
loc = input("\n Please tell me \n\n\t Do you wish to run commands Locally ? or Remote? \n")
while(True):
    print("""        Here are your options:
        ----------------------
        
        PRESS 0 TO EXIT
        COMMON COMMANDS
        ---------------
        S1. Date
        S2. Calender
        S3. NIC
        CONFIGURATIONS
        --------------
        C1. Configure yum
        C2. Configure Webserver
        C3. Configure Docker
        ADDITIONAL STORAGE /  DRIVES
        ----------------------------
        M1. Create Static Partition
        M2. Delete Static Partition
        M3. Format partition
        M4. Mount to folder
        M5. Unmount from folder
        M6. Create VG - LVM (Dynamic Partition)
        M7. Extend LVM size
        DOCKER
        ------
        D1. Run container
        D2. Stop container
        D3. Restart container and get shell access
        D4. Delete container
        D5. Show running containers
        D6. Show stopped containers
        
        HADOOP
        ------
        H1. Configure Client
        H2. Configure NameNode
        H3. Configure DataNode
        H4. Report
        H5. List Data
        H5. Put Data
        H6. Get Data
        H7. Remove Data
        """)

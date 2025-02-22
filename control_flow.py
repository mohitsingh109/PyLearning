"""
 Control Flow & Loops
"""

# if, else, elif

# Check the deployment status
# success, pending, failed
deployment_status = "success"  # by running some API or by running the stage in jenkins pipline

if deployment_status == "success":  # False
    print("✅ Deployment was successful. Proceed to next step.")
elif deployment_status == "pending":  # False
    print("⌛️ Deployment is pending! Please wait.")
else:
    print("❌ Deployment failed! Triggering rollback")

cloud_provider = "GCP"

if cloud_provider == "GCP" and (deployment_status == "success" or deployment_status == "pending"):
    print("🚀 Deploy to GCP and state monitoring")
elif cloud_provider == "AZURE":
    print("Deploy to AZURE")
elif cloud_provider == "ORACLE":
    print("Deploy to ORACLE")

print(cloud_provider)

# Loops (for, while, do while)

print("=========================")

# List
services = ["web-server", "database", "cache", "message-broker"]

for service in services:
    print(f"🔎 checking status of {service}")
    print(f"Real metric api of k8s")
    print(f"✅ {service} is running")

# Retrying Connection to a Server

print("===========================")

max_reties = 3
attempt = 0

while attempt < max_reties:  # 3 < 3
    print(f"🔄 Attempt {attempt + 1}: Trying to connect to database")
    connection_successfully = False  # Call API, hit database or any service directly

    if connection_successfully:
        print("✅ Connection Successfully")
        break  # break is used to come outside the while loop
    else:
        print("❌ Connection failed. Retrying...")

    attempt += 1  # 2 + 1 == 3

if attempt == max_reties:
    print("⚠️ Max retry attempts reached.")
    print("🚨 Alert to teams group: devops")

print("======================= Loop break & continue ======================= ")
# continue or break
# Restart of the services
services = ["web-server", "database", "cache", "message-broker"]
#service
disabled_services = ["cache"]

for service in services:
    if service in disabled_services:
        print(f"➡️Skipping {service}, as it is disabled.")
        continue  # Skip this rest of the code inside for loop

    print(f"🔧Restart {service}")

print("======================= Stop on critical error ======================= ")
# Stop on critical error
checks = ["Memory Usage", "CPU Usage", "Disk Space", "SSL Certificates"]

for check in checks:
    print(f"🔎 Run check: {check}")

    if check == "Disk Space":
        print("🚨 CRITICAL ERROR: Disk space is Low!")
        break

    print(f"✅ {check} is normal.")


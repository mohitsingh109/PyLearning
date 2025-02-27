# # Webserver
# print("Rotating logs for web server")
# print("Logs for web server rotated done")
#
# # Database
# print("Rotating logs for Database")
# print("Logs for Database rotated done")
# 100 serves

def rotate_logs(service_name):
    print(f"Rotating logs for {service_name}")
    print(f"Logs for {service_name} rotated done")


rotate_logs("web server")
rotate_logs("Databases")
rotate_logs("nginx")
rotate_logs("jira-ticket")

print("==============================")


# Check Disk space usage

def check_disk_space(used_space):
    if used_space > 90:
        return "🚨 Critical: Disk space is too high!"
    elif used_space > 75:
        return "⚠️ Warning: Disk space usage is high."
    else:
        return "✅ Disk space is within safe limit"


# call to API to fetch the disk usage for database (k8s, promothies, etc)
database_disk_usage = 80
print(check_disk_space(database_disk_usage))

# Global & local variable

threshold = 80  # Global variable


def is_memory_safe(usage):
    threshold = 90  # local variable
    return usage < threshold


print(is_memory_safe(85))
print(threshold)

import math


# 4 , load on each core = 23.7%
def calculate_cpu_load(cores, load_per_core):
    return math.ceil(cores * load_per_core)


print(f"CPU Load: {calculate_cpu_load(4, 23.7)}% ")

from datetime import datetime


def log_event(event_name):
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"{timestamp} {event_name}")


log_event("➡️ Deployment started")
log_event("✅ Service restarted")

import random


def generate_random_port():
    return random.randint(3000, 9000)  # Generate a port between 3000 to 9000


print(f"🔄 Allocated service port: {generate_random_port()}")
print(f"🔄 Allocated service port: {generate_random_port()}")
print(f"🔄 Allocated service port: {generate_random_port()}")
print(f"🔄 Allocated service port: {generate_random_port()}")
print(f"🔄 Allocated service port: {generate_random_port()}")
print(f"🔄 Allocated service port: {generate_random_port()}")

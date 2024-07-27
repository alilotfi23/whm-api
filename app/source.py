from flask import Flask, make_response, request
import json
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the URL and token from the environment variables
URL = os.getenv('URL')

# Function to list accounts
def listaccts(api_version, filter_resp, token):
    url = f"{URL}//json-api/listaccts?api.version=1&api.columns.a=user&api.columns.b=domain&" \
          "api.columns.c=plan&api.columns.d=email&api.columns.e=backup&api.columns.f=suspended&api.columns.enable=1"

    headers = {
        'Authorization': 'whm root:%s' % token
    }

    response = requests.request("GET", url, headers=headers, verify=False)
    return response


# Function to create an account
def createaccount(api_version, filter_resp, token, domain, username, password, contactemail, plan, dkim):
    url = f"{URL}//json-api/createacct?api.version=1&domain=%s&username=%s&password=%s&contactemail=%s&plan=%s&dkim=%s" % (
        domain, username, password, contactemail, plan, dkim)

    headers = {
        'Authorization': 'whm root:%s' % token
    }

    response = requests.request("GET", url, headers=headers, verify=False)
    return response


# Function to suspend an account
def suspend(api_version, filter_resp, token, user):
    url = f"{URL}//json-api/suspendacct?api.version=1&user=%s" % user

    headers = {
        'Authorization': 'whm root:%s' % token
    }

    response = requests.request("GET", url, headers=headers, verify=False)
    return response


# Function to modify an account
def modifyacct(api_version, filter_resp, token, user, domain, contactemail):
    url = f"{URL}//json-api/modifyacct?api.version=1&user=%s&domain=%s&contactemail=%s" % (
        user, domain, contactemail)

    headers = {
        'Authorization': 'whm root:%s' % token
    }

    response = requests.request("GET", url, headers=headers, verify=False)
    return response


# Function to change account plan/package
def changepackage(api_version, filter_resp, token, user, pkg):
    url = f"{URL}//json-api/changepackage?api.version=1&user=%s&pkg=%s" % (user, pkg)

    headers = {
        'Authorization': 'whm root:%s' % token
    }

    response = requests.request("GET", url, headers=headers, verify=False)
    return response


# Function to change account password
def passwd(api_version, filter_resp, token, user, password):
    url = f"{URL}//json-api/passwd?api.version=1&user=%s&password=%s" % (user, password)

    headers = {
        'Authorization': 'whm root:%s' % token
    }

    response = requests.request("GET", url, headers=headers, verify=False)
    return response


# Function to delete an account
def delete(api_version, filter_resp, token, username):
    url = f"{URL} //json-api/removeacct?api.version=1&username=%s" % username

    headers = {
        'Authorization': 'whm root:%s' % token
    }

    response = requests.request("GET", url, headers=headers, verify=False)
    return response


# Function to unsuspend an account
def unsuspend(api_version, filter_resp, token, user):
    url = f"{URL}//json-api/unsuspendacct?api.version=1&user=%s" % user

    headers = {
        'Authorization': 'whm root:%s' % token
    }

    response = requests.request("GET", url, headers=headers, verify=False)
    return response


# Function to list users
def listusers(api_version, filter_resp, token):
    url = f"{URL}//json-api/list_users?api.version=1"

    headers = {
        'Authorization': 'whm root:%s' % token
    }

    response = requests.request("GET", url, headers=headers, verify=False)
    return response


# Function to add a DNS zone record
def addzonerecord(api_version, filter_resp, token, domain, name, dnsclass, ttl, type, address):
    url = f"{URL}//json-api//json-api/addzonerecord?api.version=1&domain=%s&name=%s&dnsclass=%s&ttl=%s&type=%s&address=%s" % (
        domain, name, dnsclass, ttl, type, address)

    headers = {
        'Authorization': 'whm root:%s' % token
    }

    response = requests.request("GET", url, headers=headers, verify=False)
    return response


# Function to remove a DNS zone record
def removezonerecord(api_version, filter_resp, token, zone, line):
    url = f"{URL}//json-api/removezonerecord?api.version=1&zone=%s&line=%s" % (zone, line)

    headers = {
        'Authorization': 'whm root:%s' % token
    }

    response = requests.request("GET", url, headers=headers, verify=False)
    return response


# Function to edit a DNS zone record
def editzonerecord(api_version, filter_resp, token, domain, line, name, dnsclass, ttl, type, address):
    url = f"{URL}//json-api/addzonerecord?api.version=1&domain=%s&line=%s&name=%s&dnsclass=%s&ttl=%s&type=%s&address=%s" % (
        domain, line, name, dnsclass, ttl, type, address)

    headers = {
        'Authorization': 'whm root:%s' % token
    }

    response = requests.request("GET", url, headers=headers, verify=False)
    return response


# Function to configure backup settings
def backupconfig(api_version, filter_resp, token, backup_daily_retention, backup_monthly_enable, backup_monthly_dates,
                 backup_monthly_retention, backup_weekly_day, backup_weekly_enable, backup_weekly_retention, backupdays,
                 backupenable, backuplogs, backupsuspendedaccts, backuptype, maximum_restore_timeout, maximum_timeout,
                 min_free_space, min_free_space_unit, mysqlbackup):
    url = f"{URL}//json-api/backup_config_set?api.version=1&backup_daily_retention=%s&backup_monthly_enable=%s" \
          "&backup_monthly_dates=%s&backup_monthly_retention=%s&backup_weekly_day=%s&backup_weekly_enable=%s" \
          "&backup_weekly_retention=%s&backupdays=%s&backupenable=%s&backuplogs=%s&backupsuspendedaccts=%s&backuptype=%s" \
          "&maximum_restore_timeout=%s&maximum_timeout=%s&min_free_space=%s&min_free_space_unit=%s&mysqlbackup=%s" % \
          (backup_daily_retention, backup_monthly_enable, backup_monthly_dates, backup_monthly_retention,
           backup_weekly_day, backup_weekly_enable, backup_weekly_retention, backupdays, backupenable, backuplogs,
           backupsuspendedaccts, backuptype, maximum_restore_timeout, maximum_timeout, min_free_space,
           min_free_space_unit, mysqlbackup)

    headers = {
        'Authorization': 'whm root:%s' % token
    }

    response = requests.request("GET", url, headers=headers, verify=False)
    return response


# Function to add a backup destination
def backupdestinationadd(api_version, filter_resp, token, name, type, disabled, bucket, aws_access_key_id, password,
                         application_key, application_key_id, bucket_id, bucket_name, script, host, username, client_id,
                         client_secret, authtype, path):
    url = f"{URL}//json-api/backup_destination_add?api.version=1&name=%s&type=%s&disabled=%s" \
          "&bucket=%s&aws_access_key_id=%s&password=%s&application_key=%s&application_key_id=%s&bucket_id=%s" \
          "&bucket_name=%s&script=%s&host=%s&username=%s&client_id=%s&client_secret=%s&authtype=%s&path=%s" % (
              name, type, disabled, bucket, aws_access_key_id, password, application_key, application_key_id, bucket_id,
              bucket_name, script, host, username, client_id, client_secret, authtype, path)

    headers = {
        'Authorization': 'whm root:%s' % token
    }

    response = requests.request("GET", url, headers=headers, verify=False)
    return response


# Function to get backup configuration
def backupconfigget(api_version, filter_resp, token):
    url = f"{URL}/json-api/backup_config_get?api.version=1"

    headers = {
        'Authorization': 'whm root:%s' % token
    }

    response = requests.request("GET", url, headers=headers, verify=False)
    return response


# Function to add a task to the restore queue
def restore_queue_add_task(api_version, filter_resp, token, user, restore_point):
    url = f"{URL}//json-api/restore_queue_add_task?api.version=1&user=%s&restore_point=%s" % (
        user, restore_point)

    headers = {
        'Authorization': 'whm root:%s' % token
    }

    response = requests.request("GET", url, headers=headers, verify=False)
    return response


# Function to activate the restore queue
def restore_queue_activate(api_version, filter_resp, token):
    url = f"{URL}//json-api//json-api/restore_queue_activate?api.version=1"

    headers = {
        'Authorization': 'whm root:%s' % token
    }

    response = requests.request("GET", url, headers=headers, verify=False)
    return response

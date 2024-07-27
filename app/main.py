from flask import Flask, make_response, request
import json
from dotenv import load_dotenv
import os
from source import (listaccts, createaccount, suspend, modifyacct, changepackage, passwd, delete,
                    unsuspend, listusers, addzonerecord, removezonerecord, editzonerecord,
                    backupconfig, backupdestinationadd, backupconfigget, restore_queue_add_task)


# Load environment variables from .env file
load_dotenv()

# Get the URL and token from the environment variables
TOKEN = os.getenv('TOKEN')

# Initialize the Flask application
app = Flask(__name__)

# Route to list accounts
@app.route("/listaccts", methods=["GET"])
def _listaccts():
    try:
        api_version = 1  # Define API version
        response = listaccts(api_version=api_version, filter_resp="eq", token=TOKEN)
        return make_response(json.loads(response.text), 200)
    except BaseException as e:
        print(e)

# Route to create an account
@app.route("/createacct", methods=["POST"])
def _createaccount():
    try:
        api_version = 1
        data = json.loads(request.data)
        domain = data.get("domain")
        username = data.get("username")
        password = data.get("password")
        contactemail = data.get("contactemail")
        plan = data.get("plan")
        dkim = data.get("dkim")
        response = createaccount(api_version=api_version,
                                 filter_resp="eq",
                                 token=TOKEN,
                                 domain=domain,
                                 username=username,
                                 password=password,
                                 contactemail=contactemail,
                                 plan=plan,
                                 dkim=dkim)
        return make_response(json.loads(response.text), 200)
    except BaseException as e:
        print(e)

# Route to suspend an account
@app.route("/suspend", methods=["POST"])
def _suspend():
    try:
        api_version = 1
        user = json.loads(request.data).get("user")
        response = suspend(api_version=api_version, filter_resp="eq", token=TOKEN,
                           user=user)
        return make_response(json.loads(response.text), 200)
    except BaseException as e:
        print(e)

# Route to modify an account
@app.route("/modify", methods=["POST"])
def _modifyacct():
    try:
        api_version = 1
        data = json.loads(request.data)
        user = data.get("user")
        domain = data.get("domain")
        contactemail = data.get("contactemail")
        response = modifyacct(api_version=api_version,
                              filter_resp="eq",
                              token=TOKEN,
                              user=user,
                              domain=domain,
                              contactemail=contactemail)
        return make_response(json.loads(response.text), 200)
    except BaseException as e:
        print(e)

# Route to change account plan/package
@app.route("/changeplan", methods=["POST"])
def _changepackage():
    try:
        api_version = 1
        data = json.loads(request.data)
        user = data.get("user")
        pkg = data.get("pkg")
        response = changepackage(api_version=api_version, filter_resp="eq", token=TOKEN,
                                 user=user, pkg=pkg)
        return make_response(json.loads(response.text), 200)
    except BaseException as e:
        print(e)

# Route to change account password
@app.route("/changepass", methods=["POST"])
def _passwd():
    try:
        api_version = 1
        data = json.loads(request.data)
        user = data.get("user")
        password = data.get("password")
        response = passwd(api_version=api_version, filter_resp="eq", token=TOKEN,
                          user=user, password=password)
        return make_response(json.loads(response.text), 200)
    except BaseException as e:
        print(e)

# Route to delete an account
@app.route("/deleteacct", methods=["POST"])
def _delete():
    try:
        api_version = 1
        username = json.loads(request.data).get("username")
        response = delete(api_version=api_version, filter_resp="eq", token=TOKEN,
                          username=username)
        return make_response(json.loads(response.text), 200)
    except BaseException as e:
        print(e)

# Route to unsuspend an account
@app.route("/unsuspend", methods=["POST"])
def _unsuspend():
    try:
        api_version = 1
        user = json.loads(request.data).get("user")
        response = unsuspend(api_version=api_version, filter_resp="eq", token=TOKEN,
                             user=user)
        return make_response(json.loads(response.text), 200)
    except BaseException as e:
        print(e)

# Route to list users
@app.route("/listusers", methods=["GET"])
def _listusers():
    try:
        api_version = 1
        response = listusers(api_version=api_version, filter_resp="eq", token=TOKEN)
        return make_response(json.loads(response.text), 200)
    except BaseException as e:
        print(e)

# Route to add a DNS zone record
@app.route("/addzonerecord", methods=["POST"])
def _addzonerecord():
    try:
        api_version = 1
        data = json.loads(request.data)
        domain = data.get("domain")
        name = data.get("name")
        dnsclass = data.get("dnsclass")
        ttl = data.get("ttl")
        type = data.get("type")
        address = data.get("address")
        response = addzonerecord(api_version=api_version,
                                 filter_resp="eq",
                                 token=TOKEN,
                                 domain=domain,
                                 name=name,
                                 dnsclass=dnsclass,
                                 ttl=ttl,
                                 type=type,
                                 address=address)
        return make_response(json.loads(response.text), 200)
    except BaseException as e:
        print(e)

# Route to remove a DNS zone record
@app.route("/removezonerecord", methods=["POST"])
def _removezonerecord():
    try:
        api_version = 1
        data = json.loads(request.data)
        zone = data.get("zone")
        line = data.get("line")
        response = removezonerecord(api_version=api_version, filter_resp="eq", token=TOKEN,
                                    zone=zone, line=line)
        return make_response(json.loads(response.text), 200)
    except BaseException as e:
        print(e)

# Route to edit a DNS zone record
@app.route("/editzonerecord", methods=["POST"])
def _editzonerecord():
    try:
        api_version = 1
        data = json.loads(request.data)
        domain = data.get("domain")
        line = data.get("line")
        name = data.get("name")
        dnsclass = data.get("dnsclass")
        ttl = data.get("ttl")
        type = data.get("type")
        address = data.get("address")
        response = editzonerecord(api_version=api_version,
                                  filter_resp="eq",
                                  token=TOKEN,
                                  domain=domain,
                                  line=line,
                                  name=name,
                                  dnsclass=dnsclass,
                                  ttl=ttl,
                                  type=type,
                                  address=address)
        return make_response(json.loads(response.text), 200)
    except BaseException as e:
        print(e)

# Route to configure backup settings
@app.route("/backupconfig", methods=["POST"])
def _backupconfig():
    try:
        api_version = 1
        data = json.loads(request.data)
        # The number of daily backups to retain.
        backup_daily_retention = data.get("backup_daily_retention")
        # Whether to enable monthly backups.
        backup_monthly_enable = data.get("backup_monthly_enable")
        # Which days of the month to run backups.
        backup_monthly_dates = data.get("backup_monthly_dates")
        # The number of monthly backups to retain.
        backup_monthly_retention = data.get("backup_monthly_retention")
        # Which day of the week to run weekly backups.
        backup_weekly_day = data.get("backup_weekly_day")
        # Whether to enable weekly backups.
        backup_weekly_enable = data.get("backup_weekly_enable")
        # The number of weekly backups to retain.
        backup_weekly_retention = data.get("backup_weekly_retention")
        # Which days of the week to run daily backups.
        backupdays = data.get("backupdays")
        # Whether to enable backups.
        backupenable = data.get("backupenable")
        # Whether to back up the error logs.
        backuplogs = data.get("backuplogs")
        # Whether to back up suspended accounts.
        backupsuspendedaccts = data.get("backupsuspendedaccts")
        # The type of backup to create.
        backuptype = data.get("backuptype")
        # How long a restoration will attempt to run, in seconds. If the restoration does not succeed in this amount of time, it will stop.
        maximum_restore_timeout = data.get("maximum_restore_timeout")
        # How long a backup will attempt to run, in seconds. If the backup does not succeed in this amount of time, it will stop.
        maximum_timeout = data.get("maximum_timeout")
        # The minimum amount of free disk to check for on the destination server.
        min_free_space = data.get("min_free_space")
        # The units of measurement of disk space for the min_free_space return. (MB, Percent)
        min_free_space_unit = data.get("min_free_space_unit")
        mysqlbackup = data.get("mysqlbackup")
        response = backupconfig(api_version=api_version,
                                filter_resp="eq",
                                token=TOKEN,
                                backup_daily_retention=backup_daily_retention,
                                backup_monthly_enable=backup_monthly_enable,
                                backup_monthly_dates=backup_monthly_dates,
                                backup_monthly_retention=backup_monthly_retention,
                                backup_weekly_day=backup_weekly_day,
                                backup_weekly_enable=backup_weekly_enable,
                                backup_weekly_retention=backup_weekly_retention,
                                backupdays=backupdays,
                                backupenable=backupenable,
                                backuplogs=backuplogs,
                                backupsuspendedaccts=backupsuspendedaccts,
                                backuptype=backuptype,
                                maximum_restore_timeout=maximum_restore_timeout,
                                maximum_timeout=maximum_timeout,
                                min_free_space=min_free_space,
                                min_free_space_unit=min_free_space_unit,
                                mysqlbackup=mysqlbackup)
        return make_response(json.loads(response.text), 200)
    except BaseException as e:
        print(e)

# Route to add a backup destination
@app.route("/backupdest", methods=["POST"])
def _backupdestinationadd():
    try:
        api_version = 1
        data = json.loads(request.data)
        name = data.get("name")
        type = data.get("type")
        disabled = data.get("disabled")
        bucket = data.get("bucket")
        aws_access_key_id = data.get("aws_access_key_id")
        password = data.get("password")
        application_key = data.get("application_key")
        application_key_id = data.get("application_key_id")
        bucket_id = data.get("bucket_id")
        bucket_name = data.get("bucket_name")
        script = data.get("script")
        host = data.get("host")
        username = data.get("username")
        client_id = data.get("client_id")
        client_secret = data.get("client_secret")
        authtype = data.get("authtype")
        path = data.get("path")
        response = backupdestinationadd(api_version=api_version,
                                        filter_resp="eq",
                                        token=TOKEN,
                                        name=name,
                                        type=type,
                                        disabled=disabled,
                                        bucket=bucket,
                                        aws_access_key_id=aws_access_key_id,
                                        password=password,
                                        application_key=application_key,
                                        application_key_id=application_key_id,
                                        bucket_id=bucket_id,
                                        bucket_name=bucket_name,
                                        script=script,
                                        host=host,
                                        username=username,
                                        client_id=client_id,
                                        client_secret=client_secret,
                                        authtype=authtype,
                                        path=path)
        return make_response(json.loads(response.text), 200)
    except BaseException as e:
        print(e)

# Route to get backup configuration
@app.route("/getbackupconfig", methods=["GET"])
def _backupconfigget():
    try:
        api_version = 1
        response = backupconfigget(api_version=api_version, filter_resp="eq", token=TOKEN)
        return make_response(json.loads(response.text), 200)
    except BaseException as e:
        print(e)

# Route to add a restore task to the queue
@app.route("/restorequeueadd", methods=["POST"])
def _restore_queue_add_task():
    try:
        api_version = 1
        data = json.loads(request.data)
        user = data.get("user")
        restore_point = data.get("restore_point")
        response = restore_queue_add_task(api_version=api_version, filter_resp="eq",
                                          token=TOKEN,
                                          user=user, restore_point=restore_point)
        return make_response(json.loads(response.text), 200)
    except BaseException as e:
        print(e)

# Run the Flask application on host 0.0.0.0 and port 8080
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

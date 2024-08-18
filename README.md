# Flask WHM API Application

This is a Flask application that interacts with the WHM API to manage accounts, DNS records, backups, and other functionalities on a WHM server.

## Features

- List accounts
- Create an account
- Suspend an account
- Modify an account
- Change account plan/package
- Change account password
- Delete an account
- Unsuspend an account
- List users
- Add, remove, and edit DNS zone records
- Configure backups
- Add a backup destination
- Get backup configuration
- Add a restore task to the queue

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. **Clone the repository:**

   ```sh
   git clone https://github.com/alilotfi23/whm-api.git
   cd whm-api

2. **Create a virtual environment (optional but recommended):**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Create a `.env` file in the root directory of your project and add your WHM server URL and token:**

   ```env
   URL=https://server_ip:whm_port# Defualt is 2087
   TOKEN=your_token_here
   ```

5. **Run the application:**

   ```sh
   python app.py
   ```

## Docker container
### Instructions to Build and Run the Docker Container

1. **Ensure you have Docker installed:**
   - [Docker installation instructions](https://docs.docker.com/get-docker/)

2. **Build the Docker image:**
   - Navigate to the directory containing your `Dockerfile` and the application code.
   - Run the following command to build the Docker image:
     ```sh
     docker build -t flask-whm-api .
     ```

3. **Run the Docker container:**
   - Use the following command to run the container:
     ```sh
     docker run -d -p 80:8080 --name flask-whm-api-container flask-whm-api
     ```

4. **Access the application:**
   - Open your web browser and navigate to `http://localhost:8080` to access your Flask application.


## Endpoints

### List Accounts

- **URL:** `/listaccts`
- **Method:** `GET`
- **Response:**
  ```json
  [
    {
      "user": "example_user",
      "domain": "example.com",
      "plan": "basic",
      "email": "user@example.com",
      "backup": "enabled",
      "suspended": "no"
    }
  ]
  ```

### Create an Account

- **URL:** `/createacct`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "domain": "example.com",
    "username": "example_user",
    "password": "password123",
    "contactemail": "user@example.com",
    "plan": "basic",
    "dkim": "enabled"
  }
  ```
- **Response:**
  ```json
  {
    "result": "success",
    "details": "Account created successfully."
  }
  ```

### Suspend an Account

- **URL:** `/suspend`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "user": "example_user"
  }
  ```
- **Response:**
  ```json
  {
    "result": "success",
    "details": "Account suspended successfully."
  }
  ```

### Modify an Account

- **URL:** `/modify`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "user": "example_user",
    "domain": "example.com",
    "contactemail": "new_email@example.com"
  }
  ```
- **Response:**
  ```json
  {
    "result": "success",
    "details": "Account modified successfully."
  }
  ```

### Change Account Plan/Package

- **URL:** `/changeplan`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "user": "example_user",
    "pkg": "premium"
  }
  ```
- **Response:**
  ```json
  {
    "result": "success",
    "details": "Account package changed successfully."
  }
  ```

### Change Account Password

- **URL:** `/changepass`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "user": "example_user",
    "password": "new_password123"
  }
  ```
- **Response:**
  ```json
  {
    "result": "success",
    "details": "Account password changed successfully."
  }
  ```

### Delete an Account

- **URL:** `/deleteacct`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "username": "example_user"
  }
  ```
- **Response:**
  ```json
  {
    "result": "success",
    "details": "Account deleted successfully."
  }
  ```

### Unsuspend an Account

- **URL:** `/unsuspend`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "user": "example_user"
  }
  ```
- **Response:**
  ```json
  {
    "result": "success",
    "details": "Account unsuspended successfully."
  }
  ```

### List Users

- **URL:** `/listusers`
- **Method:** `GET`
- **Response:**
  ```json
  [
    {
      "username": "example_user",
      "email": "user@example.com"
    }
  ]
  ```

### Add a DNS Zone Record

- **URL:** `/addzonerecord`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "domain": "example.com",
    "name": "www",
    "dnsclass": "IN",
    "ttl": "3600",
    "type": "A",
    "address": "192.0.2.1"
  }
  ```
- **Response:**
  ```json
  {
    "result": "success",
    "details": "DNS zone record added successfully."
  }
  ```

### Remove a DNS Zone Record

- **URL:** `/removezonerecord`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "zone": "example.com",
    "line": "1"
  }
  ```
- **Response:**
  ```json
  {
    "result": "success",
    "details": "DNS zone record removed successfully."
  }
  ```

### Edit a DNS Zone Record

- **URL:** `/editzonerecord`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "domain": "example.com",
    "line": "1",
    "name": "www",
    "dnsclass": "IN",
    "ttl": "3600",
    "type": "A",
    "address": "192.0.2.2"
  }
  ```
- **Response:**
  ```json
  {
    "result": "success",
    "details": "DNS zone record edited successfully."
  }
  ```

### Configure Backup Settings

- **URL:** `/backupconfig`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "backup_daily_retention": 7,
    "backup_monthly_enable": "yes",
    "backup_monthly_dates": [1, 15],
    "backup_monthly_retention": 3,
    "backup_weekly_day": "Sunday",
    "backup_weekly_enable": "yes",
    "backup_weekly_retention": 4,
    "backupdays": ["Monday", "Wednesday", "Friday"],
    "backupenable": "yes",
    "backuplogs": "yes",
    "backupsuspendedaccts": "yes",
    "backuptype": "full",
    "maximum_restore_timeout": 3600,
    "maximum_timeout": 1800,
    "min_free_space": 500,
    "min_free_space_unit": "MB",
    "mysqlbackup": "yes"
  }
  ```
- **Response:**
  ```json
  {
    "result": "success",
    "details": "Backup configuration set successfully."
  }
  ```

### Add a Backup Destination

- **URL:** `/backupdest`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "name": "example_backup",
    "type": "S3",
    "disabled": "no",
    "bucket": "example-bucket",
    "aws_access_key_id": "your_access_key_id",
    "password": "your_password",
    "application_key": "your_application_key",
    "application_key_id": "your_application_key_id",
    "bucket_id": "your_bucket_id",
    "bucket_name": "example-bucket",
    "script": "your_script",
    "host": "example.com",
    "username": "your_username",
    "client_id": "your_client_id",
    "client_secret": "your_client_secret",
    "authtype": "your_authtype",
    "path": "/backup/path"
  }
  ```
- **Response:**
  ```json
  {
    "result": "success",
    "details": "Backup destination added successfully."
  }
  ```

### Get Backup Configuration

- **URL:** `/getbackupconfig`
- **Method:** `GET`
- **Response:**
  ```json
  {
    "backup_daily_retention": 7,
    "backup_monthly_enable": "yes",
    "backup_monthly_dates": [1, 15],
    "backup_monthly_retention": 3,
    "backup_weekly_day": "Sunday",
    "backup_weekly_enable": "yes",
    "backup_weekly_retention": "yes",
    "backupdays": ["Monday", "Wednesday", "Friday"],
    "backupenable": "yes",
    "backuplogs": "yes",
    "backupsuspendedaccts": "yes",
    "backuptype": "full",
    "maximum_restore_timeout": 3600,
    "maximum_timeout": 1800,
    "min_free_space": 500,
    "min_free_space_unit": "MB",
    "mysqlbackup": "yes"
  }
  ```

### Add a Restore Task to the Queue

- **URL:** `/restorequeueadd`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "user": "example_user",
    "restore_point": "2022-01-01T00:00:00Z"
  }
  ```
- **Response:**
  ```json
  {
    "result": "success",
    "details": "Restore task added to queue successfully."
  }
  ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contribution

We welcome contributions to improve this project! Here are some ways you can contribute:

1. **Report Bugs:** If you find a bug, please open an issue on GitHub with detailed information on how to reproduce it.
2. **Feature Requests:** If you have ideas for new features or improvements, feel free to open an issue or submit a pull request.
3. **Pull Requests:** If you'd like to contribute code, fork the repository and create a new branch for your feature or bug fix. Submit a pull request with a clear description of your changes.

Please ensure your contributions adhere to our coding standards and include appropriate tests.

Thank you for your contributions!

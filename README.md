# AWS Resource Auditor 🔍

A Python CLI tool that audits your AWS account — lists S3 buckets with region metadata, displays account identity information, and exports reports to JSON or CSV with a clean terminal output powered by `rich`.

---

## Demo

```
$ python3 main.py --output all

Account: 897722688072
UserId:  AIDA5CBDREJEL2DBFFJCF
Arn:     arn:aws:iam::897722688072:user/jcreyescloud

          S3 Buckets Information
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Bucket Name                ┃ Location   ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ my-app-assets              │ eu-north-1 │
│ backup-bucket              │ us-east-1  │
└────────────────────────────┴────────────┘

✓ report.json saved
✓ report.csv saved
```

---

## Features

- 🔐 Authenticates using a named AWS CLI profile (least privilege IAM user)
- 🪣 Lists all S3 buckets with their AWS region
- 👤 Displays account identity via STS (`Account ID`, `UserId`, `ARN`)
- 📊 Renders a formatted table in the terminal using `rich`
- 📁 Exports full audit report to **JSON** and/or **CSV**
- ⚡ Simple CLI interface with `--output` flag

---

## Project Structure

```
AWSResourceAuditor/
├── auditor/
│   ├── __init__.py
│   ├── account.py       # STS identity retrieval
│   ├── s3.py            # S3 bucket listing and metadata
│   └── reporter.py      # Terminal output (rich) and file export
├── main.py              # CLI entry point (argparse)
├── requirements.txt
└── README.md
```

---

## Tech Stack

| Technology   | Description                          |
|--------------|--------------------------------------|
| Python 3.10+ | Primary language                     |
| boto3        | AWS SDK for Python                   |
| rich         | Terminal formatting and tables       |
| argparse     | CLI flag handling                    |
| AWS STS      | Account identity verification        |
| AWS S3       | Bucket listing and region metadata   |

---

## Prerequisites

- Python 3.10+
- AWS CLI v2 installed and configured
- An IAM user with the following permissions:
  - `sts:GetCallerIdentity`
  - `iam:GetUser`
  - `s3:ListAllMyBuckets`
  - `s3:GetBucketLocation`

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/jcreyesDev/AWSResourceAuditor.git
cd AWSResourceAuditor
```

2. Install dependencies:

```bash
pip3 install -r requirements.txt
```

3. Configure your AWS CLI profile:

```bash
aws configure --profile your-profile-name
```

---

## Usage

```bash
# Print account info and S3 buckets to terminal
python3 main.py

# Export report as JSON
python3 main.py --output json

# Export report as CSV
python3 main.py --output csv

# Export both JSON and CSV
python3 main.py --output all

# Show help
python3 main.py --help
```

---

## IAM Policy

Minimum required permissions for the IAM user running this tool:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sts:GetCallerIdentity",
        "iam:GetUser",
        "s3:ListAllMyBuckets",
        "s3:GetBucketLocation"
      ],
      "Resource": "*"
    }
  ]
}
```

---

## Requirements

- Python 3.10+
- AWS CLI v2
- Active AWS account
- IAM user with minimum required permissions

---

## Author

Developed by [@jcreyesDev](https://github.com/jcreyesDev)
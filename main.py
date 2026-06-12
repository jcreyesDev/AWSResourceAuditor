from auditor.account import get_account_info
from auditor.s3 import get_buckets_info

if __name__ == '__main__':
    account_info = get_account_info()
    for key, value in account_info.items():
        print(f"{key}: {value}")

if __name__ == '__main__':
    buckets_info = get_buckets_info()
    print(buckets_info)
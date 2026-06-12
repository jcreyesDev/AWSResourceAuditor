from auditor.account import get_account_info
from auditor.s3 import get_buckets_info
from auditor.reporter import print_account_info
from auditor.reporter import print_buckets_table
from auditor.reporter import export_report

if __name__ == '__main__':
    account_info = get_account_info()
    buckets_info = get_buckets_info()

    print_account_info(account_info)
    print_buckets_table(buckets_info)
    export_report(account_info, buckets_info, output_format='json')
    export_report(account_info, buckets_info, output_format='csv')

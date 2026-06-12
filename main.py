import argparse
from auditor.account import get_account_info
from auditor.s3 import get_buckets_info
from auditor.reporter import print_account_info, print_buckets_table, export_report

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AWS Resource Auditor')
    parser.add_argument('--output', choices=['json', 'csv', 'all'], help='Export format')
    args = parser.parse_args()

    account_info = get_account_info()
    buckets_info = get_buckets_info()
    
    print_account_info(account_info)
    print_buckets_table(buckets_info)

    if args.output == 'json':
        export_report(account_info, buckets_info, output_format='json')
    elif args.output == 'csv':
        export_report(account_info, buckets_info, output_format='csv')
    elif args.output == 'all':
        export_report(account_info, buckets_info, output_format='json')
        export_report(account_info, buckets_info, output_format='csv')
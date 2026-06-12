import json
import csv
from rich.console import Console
from rich.table import Table

def print_account_info(account_info):
    console = Console()

    for key, value in account_info.items():
        console.print(f"[blue]{key}:[/blue] [gray]{value}[/gray]")


def print_buckets_table(buckets_info):
    console = Console()
    table = Table(title="S3 Buckets Information")

    table.add_column("Bucket Name", style="cyan", no_wrap=True)
    table.add_column("Location", style="magenta")

    for bucket in buckets_info:
        table.add_row(bucket['Bucket Name'], bucket['Location'])

    console.print(table)


def export_report(account_info, buckets, output_format):
    if output_format == 'json':
        report = { 'Account Info': account_info, 'Buckets': buckets }

        with open('report.json', 'w') as f:
            json.dump(report, f, indent=4)

    elif output_format == 'csv':
        with open('report.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['Bucket Name', 'Location'])
            writer.writeheader()
            writer.writerows(buckets)
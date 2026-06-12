from auditor.account import get_account_info

if __name__ == '__main__':
    "Get AWS account information and print it to the console."
    account_info = get_account_info()
    for key, value in account_info.items():
        print(f"{key}: {value}")
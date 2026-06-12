from auditor.account import get_account_info

if __name__ == '__main__':
    account_info = get_account_info()
    for key, value in account_info.items():
        print(f"{key}: {value}")
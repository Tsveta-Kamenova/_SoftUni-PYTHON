class BankAccount:
    def __init__(self, name, bank, balance):
        self.name = name
        self.bank = bank
        self.balance = balance


list_bank_accounts = []

data_input = input().split(" | ")

while len(data_input) != 1:
    current_bank = data_input[0]
    current_name = data_input[1]
    current_balance = float(data_input[2])

    current_bank_account = BankAccount(name=current_name, bank=current_bank, balance=current_balance)
    list_bank_accounts.append(current_bank_account)

    data_input = input().split(" | ")

list_bank_accounts.sort(key=lambda x: x.name)
list_bank_accounts.sort(key=lambda x: x.balance, reverse=True)

for i in range(0, len(list_bank_accounts)):
    for j in range(i+1, len(list_bank_accounts)):
        if (list_bank_accounts[i].balance == list_bank_accounts[j].balance) and \
                len(list_bank_accounts[i].bank) >= len(list_bank_accounts[j].bank):
            list_bank_accounts[i], list_bank_accounts[j] = list_bank_accounts[j], list_bank_accounts[i]
        else:
            pass


for i in range(len(list_bank_accounts)):
    print(f"{list_bank_accounts[i].name} -> {list_bank_accounts[i].balance:.2f} ({list_bank_accounts[i].bank})")

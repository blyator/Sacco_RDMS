import requests
import json

BASE = "http://127.0.0.1:5000"

def pretty(resp):
    try:
        print(json.dumps(resp.json(), indent=2))
    except:
        print(resp.text)

print("=== 1. Add members ===")
members = [
    {"member_id": 1, "name": "Billy", "national_id": "12345678"},
    {"member_id": 2, "name": "Kip", "national_id": "87654321"},
    {"member_id": 3, "name": "Mike", "national_id": "55555555"}
]

for m in members:
    resp = requests.post(f"{BASE}/members", json=m)
    pretty(resp)

print("\n=== 2. Create accounts ===")
accounts = [
    {"account_id": 1, "member_id": 1, "balance": 1000},
    {"account_id": 2, "member_id": 2, "balance": 500},
    {"account_id": 3, "member_id": 3, "balance": 1000}
]

for a in accounts:
    resp = requests.post(f"{BASE}/accounts", json=a)
    pretty(resp)

print("\n=== 3. Check accounts ===")
resp = requests.get(f"{BASE}/accounts")
pretty(resp)

print("\n=== 4. Make deposits ===")
deposits = [
    {"txn_id": 1, "account_id": 1, "amount": 500, "txn_type": "deposit"},
    {"txn_id": 2, "account_id": 3, "amount": 500, "txn_type": "deposit"}
]

for d in deposits:
    resp = requests.post(f"{BASE}/transactions", json=d)
    pretty(resp)

print("\n=== 5. Make withdrawals ===")
withdrawals = [
    {"txn_id": 3, "account_id": 1, "amount": 200, "txn_type": "withdraw"},
    {"txn_id": 4, "account_id": 2, "amount": 600, "txn_type": "withdraw"},  # Should fail
    {"txn_id": 5, "account_id": 3, "amount": 200, "txn_type": "withdraw"}
]

for w in withdrawals:
    resp = requests.post(f"{BASE}/transactions", json=w)
    pretty(resp)

print("\n=== 6. Check final accounts ===")
resp = requests.get(f"{BASE}/accounts")
pretty(resp)

print("\n=== 7. Check all transactions ===")
resp = requests.get(f"{BASE}/transactions")
pretty(resp)

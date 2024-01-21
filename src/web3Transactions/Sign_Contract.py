from web3 import Account
import os
import segno

def signContract(to, value, privateKey):
    # w3 = Web3(Web3.WebsocketProvider('wss://eth-sepolia.g.alchemy.com/v2/' + os.environ["Alchemy_API"]))
    value = value*(10**18)
    with open("Nounce.txt", "r") as file:
        #print(file.read())
        nounce = int(file.read().strip())

    nounce += 1
    with open("Nounce.txt", "w") as file:
        file.write(str(nounce))

    contract = {
        "from": Account.from_key(privateKey).address,
        "to": to,
        'gas': 21000,
        'maxFeePerGas': 2000000000,
        'maxPriorityFeePerGas': 1000000000,
        "nonce": nounce,
        'chainId': 11155111,
        "value": int(value)
    }
    # 2. Sign tx with a private key
    signed = Account.sign_transaction(contract, privateKey)
    print(f"Raw tx: {signed.rawTransaction.hex()}")

    segno.make_qr(signed.rawTransaction).save("Transaction_QR_Code.png", scale = 100)
    return signed.rawTransaction



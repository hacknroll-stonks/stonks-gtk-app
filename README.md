# Stonks App
![gallery](https://github.com/user-attachments/assets/60a02ca4-c41b-445b-aada-f6e2f36460ee)

# Inspiration

We have always felt insecure when hodling our cryptocurrency on current hardware wallets. We are never sure of whether the seed phrase for these cryptocurrency wallets are truly random or just one out of a predefined list of seed phrases from a malicious hardware wallet manufacturer. As users have to trust that their hardware wallet is generating a true random number. Which in this case puts our crypto assets in a precarious situation.

Furthermore using bluetooth or usb to transmit transaction data to and from hardware wallets is opaque to the average user, as they are unable to verify the data being transmitted. The worst being their seed phrase leaving their hardware wallets and on to a malicious actor.
What it does

We feed high entropy data from physical sensors (camera) to an industry standard deterministic seed phrase generation algorithm to generate the seed phrase. Users are able to verify the algorithm within our hardware wallet instead of deciphering open source code or trusting a hardware manufacturer’s word. Thereafter users can use our hardware wallet to sign and receive transactions via QR codes which can decoded and are human readable.
How we built it

Using a raspberry pi , Flask, GTK, BIP 44 derivation path, Web3 python libraries
# Challenges we ran into

Understanding the various cryptographic standards and steps to sign transactions and create seed phrases. Integration of using different packages with their own event loops.
# Accomplishments that we're proud of

We built a hardware wallet that we can safely store our seed phrase and sign transactions.
# What we learned

Cryptographic standards Steps involved in signing cryptocurrency transactions

Check out our Devpost here: https://devpost.com/software/trustless-cryptocurrency-seed-phrase-generato

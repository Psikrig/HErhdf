from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import abi, contract_address
w3 = Web3 (Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
contract = w3.eth.contract(address=contract_address, abi=abi)


print(w3.eth.get_balance("0x4b44730418Ec8F63AC95a2c15b0E19D5197d22d2") + ", " + w3.eth.get_balance("0x680DA1CB6e7A112F05c8DA4159D1451B7985da36") + ", " 
      + w3.eth.get_balance("0x091CeF5C66C0d4b86C6108DaAcc6c1213f958Ee9") + ", " + w3.eth.get_balance("0x7db4D0F81d1027c19daf348c1fa740a2bA23DF1E") + ", " + w3.eth.get_balance("0x0EfA6A0d208baac1485908991Ffb789d84d88c75") + ", ")

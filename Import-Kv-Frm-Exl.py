from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential,AzureCliCredential
import argparse
import pyexcel as p
parser = argparse.ArgumentParser()
parser.add_argument("-kv", "--KeyVault", help = "Provide KV name which want to see the value")
#
parser.add_argument("-exl", "--exlsheet", help = "Provide Exl Sheet which contain the Key Values")
#
args = parser.parse_args()
#
keyVaultName = args.KeyVault
ExlName = args.exlsheet
records = p.get_records(file_name=ExlName)
credential = AzureCliCredential()
secret_client = SecretClient(vault_url=f"https://{keyVaultName}.vault.azure.net/", credential=credential)
#
for r in records:
  secret = secret_client.set_secret(r['Key'],r['value'])
  secret = secret_client.get_secret(r['Key'])
  print(secret.name, secret.value)

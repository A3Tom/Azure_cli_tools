import json
import argparse

from tqdm import tqdm
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

client: SecretClient

parser = argparse.ArgumentParser(description='A tool to clone keyvaults into local json files')
name_arg = parser.add_argument('--name', type=str, help='The keyvault name you wish to JSonify')
blank_arg = parser.add_argument('--blank', type=bool, default=False, help='blanks the secret values')
outputdir_arg = parser.add_argument('--outputDir', type=str, default=".", help='The output directory for the settings file(s)')

def run():
    kvSecrets = getAllKvSecrets()
    parsedSecrets = generateSecretDictionary(kvSecrets)
    outputSecretsToJsonFile(parsedSecrets)

def getAllKvSecrets():
    return client.list_properties_of_secrets()

def generateSecretDictionary(kvSecrets):
    result = {}

    for kvSecret in tqdm(kvSecrets, unit=" secrets"):
        secretValue = ""

        if not blankValues:
            secretValue = getSecretValue(kvSecret.name)

        result[kvSecret.name] = secretValue

    return result

def getSecretValue(secretName):
    secret = client.get_secret(secretName)
    return secret.value

def outputSecretsToJsonFile(parsedSecrets):
    jsonString = json.dumps(parsedSecrets) 
    parsed = json.loads(jsonString)
    fileOutput = json.dumps(parsed, indent=4, sort_keys=True)
    outputFullPath = f"{outputDir}\{keyVaultName}.settings.json"

    jsonFile = open(outputFullPath, "w")
    jsonFile.write(fileOutput)
    jsonFile.close()

def setupKvClient() :
    kvUri = f'https://{keyVaultName}.vault.azure.net/'
    credential = DefaultAzureCredential()
    return SecretClient(vault_url=kvUri, credential=credential)

def handleValidation():
    if(args.name is None): 
        raise argparse.ArgumentError(name_arg, 'Keyvault name cannot be null, please pass a --name')

if __name__ == '__main__':
    args = parser.parse_args()

    keyVaultName = args.name
    blankValues = args.blank
    outputDir = args.outputDir

    handleValidation()
    
    client = setupKvClient()
    run()
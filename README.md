# Azure Cli Tools

This is just a collection of wee tools n scripts that reduce the overall amount of scrollin n clickin you have to do in Azure

## Current Tools

- Keyvault To Json 
  - Gets a given keyvault from Az using managed identity and paps it to an output dir

## Installation

Set up your venv of choice 

`pip install tdqm`   
`pip install azure-identity`  
`pip install azure-keyvault-secrets`  

## Running

Currently this repo is in it's most primitive form so I am running each file individually  
Forgive me, this transgression shall be resolved in the near future

`py kv-to-json.py --name <KeyVaultName>`

Optional args:

`--blank` - Gets all the keys and omits all values  
`--outputDir` - Sets the output directory, defaults to `%`

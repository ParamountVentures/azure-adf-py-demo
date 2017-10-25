## Installation
These instructions use a terminal window on OSX.

Install blob storage support

```
pip install azure-storage-blob  
pip3 install azure-storage-blob
```

Init Azure session

```
az login
```

*Follow the instructions to complete login.*

Create a storage account (we assume same values as in config.py):
```
az storage account create -g dev-adf -n livzdevstorage -l westeurope --sku Standard_LRS
```

Get the connection string for this session:

```
StorageConectionString=$(az storage account show-connection-string -g dev-adf -n livzdevstorage)
export AZURE_STORAGE_CONNECTION_STRING="$StorageConectionString"
```

Create input/output containers:

```
az storage container create -n input
az storage container create -n output
```

Upload the sample data file (assumes you are in the copy_blob_file_to_secondary_blob_folder folder):

```
az storage blob upload -c input -f ./data/input.txt -n input.txt
```

Run the pipeline:

```
python3 run.py
```
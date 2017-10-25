from config import *
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import *
from datetime import datetime, timedelta
import time

# create the resource group
def createResourceGroup(credentials):

    resource_client = ResourceManagementClient(credentials, SUBSCRIPTION_ID)

    rg_params = {'location': DEPLOYMENT_REGION}

    # comment out if the resource group already exits
    resource_client.resource_groups.create_or_update(RESOURCE_GROUP, rg_params)

# Create the Data Factory
def createDataFactory(credentials):

    adf_client = DataFactoryManagementClient(credentials, SUBSCRIPTION_ID)

    # Create a data factory
    df_resource = Factory(location=DEPLOYMENT_REGION)
    df = adf_client.factories.create_or_update(RESOURCE_GROUP, DATA_FACTORY_NAME, df_resource)

    while df.provisioning_state != 'Succeeded':
        df = adf_client.factories.get(RESOURCE_GROUP, DATA_FACTORY_NAME)
        time.sleep(1)

    print("Created Data Factory")

def main():

    # Specify your Active Directory client ID, client secret, and tenant ID
    credentials = ServicePrincipalCredentials(client_id=APP_CLIENT_ID, secret=APP_SECRET, tenant=TENANT_ID)

    createResourceGroup(credentials)
    createDataFactory(credentials)

# Start the main method
main()
# Progetto Azure: Sviluppo di App e Interfaccia Web

Questo progetto descrive lo sviluppo di un'applicazione su Azure utilizzando Azure Functions e un'interfaccia web per interagire con l'applicazione.

## Prerequisiti

- **Azure CLI** installato
- **Python 3.10** o versione compatibile
- **jq** (utilizzato per gestire JSON nel terminale)

## Configurazione del Progetto

### Autenticazione su Azure
Accedere ad Azure con il comando seguente:
az login --use-device-code

# Creazione di Variabili d'Ambiente
## Impostare alcune variabili d'ambiente necessarie per il progetto:
export AZURE_RESOURCE_GROUP=`az group list | jq -r ".[].name"`
echo "Il tuo AZURE_RESOURCE_GROUP e' il seguente ${AZURE_RESOURCE_GROUP}"

export COGNOME=fumagalli
echo "Il tuo COGNOME e' il seguente ${COGNOME}"

export AZURE_FUNCTION_STORAGE_ACCOUNT_NAME=storage202325bd$COGNOME
echo "Il tuo AZURE_FUNCTION_STORAGE_ACCOUNT_NAME e' il seguente ${AZURE_FUNCTION_STORAGE_ACCOUNT_NAME}"

export AZURE_FUNCTION_APP_NAME=func-app-2023-25-bd-$COGNOME
echo "Il tuo AZURE_FUNCTION_APP_NAME e' il seguente ${AZURE_FUNCTION_APP_NAME}"

## Creazione dell'Account di Archiviazione
Creare un account di archiviazione su Azure:
az storage account create --name $AZURE_FUNCTION_STORAGE_ACCOUNT_NAME --location westeurope --resource-group $AZURE_RESOURCE_GROUP --sku Standard_LRS
Creazione della Funzione su Azure
Creare un'applicazione serverless con Azure Functions:

az functionapp create --resource-group $AZURE_RESOURCE_GROUP --consumption-plan-location westeurope --runtime python --runtime-version 3.10 --functions-version 4 --name $AZURE_FUNCTION_APP_NAME --os-type linux --storage-account $AZURE_FUNCTION_STORAGE_ACCOUNT_NAME


## Pubblicazione dell'Applicazione
Per pubblicare l'applicazione su Azure, seguire questi passi:

### Posizionarsi nella cartella del progetto:
cd MyProjFolder
Attivare l'ambiente virtuale:

source .venv/bin/activate

### Pubblicare l'applicazione:
func azure functionapp publish $AZURE_FUNCTION_APP_NAME
Avviare l'app localmente:

func start

## Avvio del Server Web Locale
Per testare l'interfaccia, aprire un nuovo terminale e eseguire:

python -m http.server 5500

## Accedere all'interfaccia web e selezionare un ingrediente, quindi cliccare sul pulsante per avviare la funzione.

Nota: Non cercare ingredienti con numeri a due cifre, il motivo verrà spiegato in aula.

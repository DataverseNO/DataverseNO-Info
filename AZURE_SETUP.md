# Azure Infrastructure Setup

One-time setup for deploying the DataverseNO information website to Azure Static Web Apps.
Run these commands once from your machine using the [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli).

---

## Prerequisites

- Azure CLI installed and logged in (`az login`)
- Your Azure subscription ID (`az account show --query id -o tsv`)
- Admin access to this GitHub repository

---

## Step 1 — Set your variables

```bash
SUBSCRIPTION_ID="<your-subscription-id>"
RG="info-dataverse-rg"
LOCATION="norwayeast"
APP="info-dataverseno"
```

---

## Step 2 — Create resource group

```bash
az account set --subscription $SUBSCRIPTION_ID

az group create \
  --name $RG \
  --location $LOCATION
```

---

## Step 3 — Create Azure Static Web Apps resource

```bash
az staticwebapp create \
  --name $APP \
  --resource-group $RG \
  --location $LOCATION \
  --sku Free \
  --source https://github.com/UiT-DataverseNO/Info-Dataverse \
  --branch main \
  --login-with-github
```

This command opens a browser for GitHub authentication and automatically:
- Creates the Static Web Apps resource
- Adds the `AZURE_STATIC_WEB_APPS_API_TOKEN` secret to the GitHub repository
- Generates `.github/workflows/deploy.yml` (already in this repo — decline or replace)

---

## Step 4 — Configure custom domain

```bash
az staticwebapp hostname set \
  --name $APP \
  --resource-group $RG \
  --hostname info.dataverse.no
```

Then add a CNAME record in your DNS:
```
info.dataverse.no → <app>.azurestaticapps.net
```

TLS is provisioned automatically.

---

## Estimated cost

| Resource | SKU | Cost |
|---|---|---|
| Azure Static Web Apps | Free | $0 |
| **Total** | | **$0** |

---

## Updating the site

Push to `main` — the GitHub Actions workflow builds and deploys automatically (~1 minute).

Pull requests get a **preview URL** automatically, useful for reviewing content changes before they go live.

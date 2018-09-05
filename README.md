# cloudpaper
[![Deploy to Azure](http://azuredeploy.net/deploybutton.png)](https://azuredeploy.net/)


Dockerised Azure Deployable version of newspaper3k python app: https://github.com/codelucas/newspaper 

#Deploy using Azure CLI

az login

az account set --subscription SUBSCRIPTION_ID

az container create --resource-group CloudPaperTest --name cloudjournocontainer --image prananth/newspaper3k-docker --dns-name-label cloudjourno --ports 5000

az container show --resource-group CloudPaperTest --name cloudjournocontainer --query "{FQDN:ipAddress.fqdn}" --out table
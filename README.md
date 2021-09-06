# Import/Export to Azure Key Vault from EXL sheet using python scripts
Here is the python scripts to Import the Secret's Key and Values from Exl sheet or Export(Scan) the Secret's Key values from the Azure Key Vault
### Use case:
   -	If you want to extract the Secret's Key and Values from AzureKeyVault and create exl sheet  use **Export-Kv-To-Exl.py** 
   -	If you want create Secret's from exl sheet use **Import-Kv-Frm-Exl.py** ( it will read the Exl sheet and create  Secret's in Key Vault)

## Prerequisite
-	 Key Vault Secret's permission 'get' and 'list' to export the Key Values from Azure-KeyVault and 'set' permission if want Import the values from Exl to Azure-KeyVault
-	 Az login
-	 Python packages if see any package error's 
## Export(Scan) the Azure KeyVult
  ```
   python3 Export-Kv-To-Exl.py -kv=mykeyvault
  ```
  - As Output it show in terminal and as well create EXL as mykeyvault-CurrentDate.xlsx
## Import the Key and Values from Exl sheet to Azure Key Vault
  ```
   python3 Import-Kv-Frm-Exl.py -kv=mykeyvault-import -exl=mykeyvault.xlsx
  ```
  - Exl sheet heading should be **Key** and **value** then it will read the exl sheet 
    - ![This ref Image]( https://github.com/vinshetty/azure-keyvault-import-export/blob/main/exlimage.PNG)

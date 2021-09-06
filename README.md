# Import/Export to Azure Key Vault from EXL sheet using python scripts
Here is the python scripts to Import the Key and Values from Exl sheet or Export(Scan) the Key values from the Azure Key Vault
## Prerequisite
-	 Key Vault permission 'get' and 'list' to export the Key Values from Azure-KeyVault and 'set' permission if want Import the values from Exl to Azure-KeyVault
-	 Az login
-	 Python packages if see any package error's 
## Export(Scan) the Azure KeyVult
  ```
   python3 Export-Kv-To-Exl.py -kv=mykeyvault
  ```
  -- As Output it show in terminal and as well create EXL as mykeyvault-CurrentDate.xlsx
## OutPut/Result

python3 Export-Kv-To-Exl.py -kv=mykeyvault
```

Replace `mykeyvault` with the name of your key vault. The script will output the number of secrets exported and the file name in the terminal. You can open the Excel file and verify that it contains your secrets.

### How to import secrets from an Excel sheet to Azure Key Vault?
To import secrets from an Excel sheet to Azure Key Vault, you can use the **Import-Kv-Frm-Exl.py** script. This script will read an Excel file with two columns: Key and Value, and create secrets in your key vault with the same names and values.

To run the script, open a terminal and type the following command:

```
python3 Import-Kv-Frm-Exl.py -kv=mykeyvault-import -exl=mykeyvault.xlsx
```

Replace `mykeyvault-import` with the name of your destination key vault and `mykeyvault.xlsx` with the name of your source Excel file. The script will output the number of secrets imported and their names in the terminal. You can check your key vault and verify that it contains your secrets.

### Conclusion
In this blog post, I showed you how to import and export secrets to Azure Key Vault from an Excel sheet using Python scripts. This can be handy if you want to backup your secrets, migrate them to another key vault, or create them from a spreadsheet. I hope you found this useful and feel free to leave your feedback or questions in the comments section below.
```

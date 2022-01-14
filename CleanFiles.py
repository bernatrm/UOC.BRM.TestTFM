def cleanSmallFile(file_path:str):
    with open(file_path, 'r', encoding="cp1252") as file :
        file_data = file.read()
    replace_string = '~|'
    if replace_string in file_data:
        file_data = file_data.replace(replace_string, '')

        dest_file = r"data\Test\02_2014-08-01_cleaned.csv" 
        with open(file_path, 'w', encoding="cp1252") as file:
            file.write(file_data)

cleanSmallFile(r"data\Test\02_2014-08-01.csv")

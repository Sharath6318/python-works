file_path = "PYTHON-WORKS\\File-operations\\process_error\\errors.txt"

info_path = "PYTHON-WORKS\\File-operations\\process_error\\info.txt"

warning_path = "PYTHON-WORKS\\File-operations\\process_error\\warning.txt"

error_path = "PYTHON-WORKS\\File-operations\\process_error\\error.txt"

fr = open(file_path, "r")

fw_info = open(info_path, "w")

fw_warning = open(warning_path, "w")

fw_error = open(error_path, "w")


for line in fr:

    errors = line.rstrip("\n")

    if "WARNING" in errors:

        fw_warning.write(errors + "\n")

    elif "INFO" in errors:

        fw_info.write(errors + "\n")
        
    elif "ERROR" in errors:

        fw_error.write(errors + "\n")

print("program End")



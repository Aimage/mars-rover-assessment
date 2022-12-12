def extract_value(line):
    label, value = line.split(":")
    return label.strip(), value.strip()


def read_instruction_from_file(file_name):
    plateau = ""
    rover_landing_insctructions = {}
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            label, value = extract_value(line)
            if "Plateau" in label:
                plateau = value
            if "Landing" in label:
                name = label.split(" ")[0]
                rover_landing_insctructions[name] = {"landing": value}
            if "Instruction" in label:
                name = label.split(" ")[0]
                rover_landing_insctructions[name]["instruction"] = value
    return plateau, rover_landing_insctructions

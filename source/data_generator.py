
def CreateData(data_type, model_type):

    arff_data_set = open("datasets/arff_"+data_type+"_"+model_type+".arff", "w")
    arff_data_set.write("@relation relation1 \n")
    arff_data_set.write("\n")

    numAttributes = input("Enter number of attributes: ")

    print("Enter full attribute list now: ")

    for i in range(int(numAttributes)):
        arff_data_set.write("@attribute " + input() + " real\n")

    arff_data_set.write("\n")

    arff_data_set.write("@data \n")

    print(data_type)

    with open("datasets/"+data_type+".dat", "r") as original_data:
        for line in original_data:
            tokens = line.split()
            if model_type == "CLASSIFICATION" or model_type == "C":
                if int(tokens[len(tokens)-1]) >= 2:
                    tokens[len(tokens)-1] = "fp"
                else:
                    tokens[len(tokens)-1] = "nfp"
            parsed_line = ','.join(tokens)
            arff_data_set.write(parsed_line + "\n")
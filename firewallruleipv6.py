import re

def remove_duplicates(input_file):
    unique_lines = set()

    # Read input file and remove duplicates
    with open(input_file, 'r') as f:
        for line in f:
            unique_lines.add(line.strip())
           
    addipv4firewall(unique_lines)
    # Print all the items

    


def addipv4firewall(unique_lines):
    with open(output_file, "w") as file:
        for line in unique_lines:
            data = "\n" "### tuple ### deny any any ::/0 any " + line + " in"
            file.write(data)
           # data = "\n" "### tuple ### deny any any 0.0.0.0/0 any " + line + " in"
           # file.write(data)
            data2 = "\n" "-A ufw6-user-input -s " + line + " -j DROP"
            file.write(data2)



if __name__ == "__main__":
    input_file = input("Enter the path of the input text file: ")

    output_file = input("Enter the path of the output text file: ")
    
    remove_duplicates(input_file)

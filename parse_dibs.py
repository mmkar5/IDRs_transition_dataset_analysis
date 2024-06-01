import xml.etree.ElementTree as ET
import os
import sys

def main():
    input_file=input("Enter input filepath:")
    output_file=input("Enter output filepath:")
    get_sequence(input_file,output_file)


def get_sequence(input_file,output_file):
    if os.path.exists(output_file):
        sys.exit("Given output file already exists!")       
    output=open(output_file,"w",newline="")

    tree=ET.parse(input_file)
    root=tree.getroot()

    for entry in root.findall("entry"):
        accessions=entry.find("accession").text

        for chain in entry.findall("macromolecules/chain"):
            if chain.find("type").text=="Disordered":
                sequence=chain.find("sequence").text
                name=chain.find("name").text
                id=chain.find("id").text
                
                output.write(">"+name+"_"+accessions+"_"+id+"\n")
                output.write(sequence+"\n")
    output.close()

if __name__=="__main__":
    main()
    
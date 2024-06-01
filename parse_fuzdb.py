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
    output=open(output_file,"w",newline="",encoding='utf-8')

    tree=ET.parse(input_file)
    root=tree.getroot()
    
    for fuzdb in root.findall("fuzdb"):
        id=fuzdb.find("entry_id").text
        sequence=fuzdb.find("sequence").text
        name=fuzdb.find("protein_name").text

        fuzzy_regions=sorted([(int(region.find("start").text),
        int(region.find("end").text)) if region.find("end").text!="null" else (int(region.find("start").text),int(region.find("start").text))
        for region in fuzdb.findall("fuzzy_region")],
        key=lambda x:x[0])

        combined_regions=[]
        for start,end in fuzzy_regions:
            if combined_regions and start - 1 <= combined_regions[-1][1]:
                combined_regions[-1]=(combined_regions[-1][0],max(end,combined_regions[-1][1]))
            elif (start,end) in combined_regions:
                pass
            else:
                combined_regions.append((start,end))
        
        for start,end in combined_regions:
            region=sequence[start-1:end]
            if len(region)>1:
                output.write(">"+name+"_"+id+"_"+str(start)+"-"+str(end)+"\n")
                output.write(sequence+"\n")

    output.close()

if __name__=="__main__":
    main()
    
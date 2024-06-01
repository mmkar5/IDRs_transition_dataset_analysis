score=None
sequence=None
id=None
input_file=input("Enter input filepath:")
output_file=input("Enter output filepath:")
output=open(output_file,"w")
with open(input_file,"r") as file:
    for line in file:
        if not line.startswith(">"):
            if not line.startswith("0") and not line.startswith("1"):
                sequence=line.strip()
                score=None
            else:
                score=line.strip()
            if score and sequence and id:
                result="".join(sequence[i] if score[i] == "1" else " " for i in range(len(sequence)))
                results=result.split()
                for i,r in enumerate(results):
                    #output.write(id+" "+"Disorder_Order"+"_"+str(i+1)+"\n")
                    output.write(id+" "+"Disorder_Disorder"+"_"+str(i+1)+"\n")
                    output.write(r+"\n")
        else:
            if "sequence" in line:
                id=line.strip()
output.close()

def get_all_lines(filename):
    with open(infile, 'rb') as f:
        return f.readlines()
def get_idx(lines, targ_str):
    index = 0
    for line in lines:
        if targ_str in line:
            last_idx = index
            break
        index+=1
def write_afters(lines, last_idx):
    outfilename = 'C:/Users/Erik-PC/Documents/MobaXterm/home/MyDocuments/FioreLab/Processed/Notes/BIBE1_07_26_18.txt'
    with open(outfilename, 'wb') as f:
        for line in lines[last_idx:]:
            f.write(line)
def write_befores(lines, last_idx):
    outfilename = 'C:/Users/Erik-PC/Documents/MobaXterm/home/MyDocuments/FioreLab/Processed/Notes/BIBE1_07_26_18.txt'
    with open(outfilename, 'wb') as f:
        for line in lines[:last_idx]:
            f.write(line)

if __name__=="__main__":
    infilename  = 'C:/Users/Erik-PC/Documents/MobaXterm/home/MyDocuments/FioreLab/IMPROVE/BIBE1_07_26_18'
    lines       = get_all_lines(infilename)
    split_idx   = get_idx(lines, 'Dataset   SiteCode')
    write_befores(lines, split_idx)

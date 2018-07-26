
infile = 'C:/Users/Erik-PC/Documents/MobaXterm/home/MyDocuments/FioreLab/IMPROVE
text = open(infile, "r")
outfile = 'C:/Users/Erik-PC/Documents/MobaXterm/home/MyDocuments/FioreLab/Proces'
output = open(outfile, "w")
split = 'Dataset   SiteCode'
nlines = 0
wlines = 0

for line in text:
    nlines += 1
        if (line.find(split) >= 0):
            breakline = nlines

print breakline

while wlines < breakline:
    wlines += 1
    output.write(line)

text.close()
output.close()


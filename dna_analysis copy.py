import re
import sqlite3

conn = sqlite3.connect('SNPTable.db')
cursor = conn.cursor()

snps = []


with open("mydna.txt", "r") as file:
    for line in file:
        
        match = re.search(r'rs\w+', line)
        if match:
            rsid = match.group()
            alleles = line.split()
            alleles.remove(rsid)
            alleles = [x for x in alleles if not x.isdigit()]
            allele_str = ' '.join(alleles)
            snps.append((rsid, allele_str))
            
matches = []

for item in snps:
    rsid = item[0]
    alleles = item[1]
    cursor.execute(f"SELECT * FROM 'RSID_INFO' WHERE rsid=? AND alleles=?", (rsid, alleles))
    result = cursor.fetchone()
    if result:
        matches.append((rsid, alleles))
        print("ID:", result[0])
        print("rsid:", result[1])
        print("alleles:", result[2])
        print("cancer:", result[3])
        print("risk association:", result[4])
    

    
        
conn.close()

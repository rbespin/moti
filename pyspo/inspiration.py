import random
import shutil

opened_file = open("inspo.txt","r+");
line = opened_file.readline()
line_split = line.split()
quote_count = 0;

quotes_seen = []

for x in line_split:
   quotes_seen.append(int(x))

quotes = {}
while line != '':
   line = opened_file.readline()
   line = line[:-1]
   quotes[quote_count] = line
   quote_count+=1
quotes.pop(len(quotes)-1)

rand = random.randrange(len(quotes))
while(rand in quotes_seen):
   rand = random.randrange(len(quotes))

def printQuote(rand):
   for x in range(4):
        print()
   print(quotes[rand])
   for x in range(4):
        print()
printQuote(rand)
quotes_seen.append(rand)
if(len(quotes_seen) == len(quotes)):
   quotes_seen.clear()

# write seen quotes to first line

opened_file.close()

with open("inspo.txt") as f:
   lines = f.readlines()

#line = opened_file.readlines()
quotes_seen.sort()
string_quotes = ""
for x in quotes_seen:
   string_quotes += str(x)
   string_quotes += " "
string_quotes += '\n'

lines[0] = string_quotes

with open("inspo.txt","w") as f:
   f.writelines(lines)



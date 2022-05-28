#converts excel to text format needed for latex matrices. 
#note: remove final \\ from output manually
import pandas as pd
 
df = pd.read_excel('../tables/table2.xlsx')

text = df.to_csv(index = False, header = False)
text = text.replace(',', ' & ')
text = text.replace('\n', ' \\\\\n')

with open('../tables/table4.txt', 'w+') as outfile:
	outfile.write(text)
	

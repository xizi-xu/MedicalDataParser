import pandas as pd
import csv

def createNewRow():
	return ["",0,0,0,0,0,0]

def main():
	df = pd.read_csv('./abc.csv')
	# only keep ID and event type 
	df = df[['MSIS_ID', 'Event Type']]
	grouped = df.groupby(['MSIS_ID', 'Event Type'])
	# caculate how all the counts
	temp = grouped.size()
	# get all the multi level index
	all_index = temp.index.tolist()
	with open('outputfile.csv', 'wb') as csvfile:
		mywriter = csv.writer(csvfile, delimiter = ",")
		mywriter.writerow(['MSIS_ID', 'CL', 'ER', 'HO', 'NP', 'PO', 'RX'])
		new_row = createNewRow()
		for i in all_index:
			# write out the row if new id appears
			if new_row[0] != i[0]:
				# dont write the first empty row
				if new_row[0] != "":
					mywriter.writerow(new_row)
				new_row = createNewRow()
				new_row[0] = i[0]
			# update count if necessary
			if i[1] == 'CL':
				new_row[1] = temp[i]
			elif i[1] == 'ER':
				new_row[2] = temp[i]
			elif i[1] == 'HO':
				new_row[3] = temp[i]
			elif i[1] == 'NP':
				new_row[4] = temp[i]
			elif i[1] == 'PO':
				new_row[5] = temp[i]
			elif i[1] == 'RX':
				new_row[6] = temp[i]
		# write the last row
		mywriter.writerow(new_row)


if __name__ == "__main__": main()
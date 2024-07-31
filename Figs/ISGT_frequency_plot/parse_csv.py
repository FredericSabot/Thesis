import csv

for i in range(50):
    t = []
    omega = []
    name = "%03d.csv" % i
    with open('It_' + name) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        row = next(reader)
        index = row.index('OMEGA_REF_omegaRef_grp_0_value')
        for row in reader:
            t.append(row[0])
            omega.append(row[index])
    
    with open('omega_' + str(i) + '.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')  # Change delimiter
        writer.writerow(['t', 'omega'])
        for j in range(len(t)):
            writer.writerow([t[j], omega[j]])

import csv

allReviews= []

numberStop = 100
i = 0

with open("DB/Hotel_Reviews.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # TODO: Remove for production
        i+=1
        if(i > numberStop):
            break
        # ------

        allReviews.append(dict(row))

csvfile.close()
import csv


def getReviewsFromCsvFile(path):
    try:
        reviews = []
        with open(path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            # numberStop = 100
            # i = 0
            for row in reader:
                # TODO: Remove for production
                # i+=1
                # if(i > numberStop):
                #     break
                # ------

                reviews.append(dict(row))

        csvfile.close()
        return reviews
    except Exception as exp:
        print("Error opening and reading '" + path + "'" + " : " + exp.args[0])
        return None


if __name__ == "__main__":
    reviews = getReviewsFromCsvFile("DB/Hotel_Reviews.csv")

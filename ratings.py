"""Restaurant rating lister."""

def build_dict(filename):
    # open file
    rating_data = open(filename)

    # create empty dictionary
    rest_dict = {}

    # go through file, line by line
    for line in rating_data:
        
        # clean up line and split with delimiter :
        rest, score = line.rstrip().split(":")

        # save into our dictionary
        rest_dict[rest] = score
    
    return rest_dict


def sort_dict(rest_dict):
    # sort dictionary by keys
    for rest, rating in sorted(rest_dict.items()):
        print(f"{rest} is rated at {rating}.")


def add_rating(rest_dict):
    # ask user for restaurant name and rating
    name = input("What restaurant would you like to add? ")
    rating = input("What its rating? ")
    
    # add name and rating to our dictionary
    rest_dict[name] = rating

    # print new sorted list
    sort_dict(rest_dict) 


rest_dict = build_dict("scores.txt")
sort_dict(rest_dict)
add_rating(rest_dict)
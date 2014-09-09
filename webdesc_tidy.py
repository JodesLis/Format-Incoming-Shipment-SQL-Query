"""
Uses data from the SQL query "new_wholesale_items_for_web.sql" in CSV format.
Returns a tidier version, checking for a recent photograph.
        -Jody 14/08/2014
"""

import os
import csv
import datetime


SUPPLIER_DICT = {"SUM998": "Sumiati",
                 "TRE998": "Trend Center",
                 "INT999": "IDL",
                 "SIA995": "Ayuttaya",
                 "DAL999": "Dalian Jinnee",
                 "RLK999": "Khanna",
                 "NEO999": "Neo Crafts",
                 "MCB998": "Meelarp",
                 "CHI998": "Chiangmai Raem",
                 "FUH999": "Fu Hui",
                 "Qay999": "Qayyum Exports"}


def check_for_photo(new_items):
    """
    crawls images directory and produces a list of all
    photos taken after 2010
    """
    image_dir = 'i:\sales\images\\'
    found = []
    codes = [item[2] for item in new_items]
    for code in codes:
        full_path = image_dir + code + ".jpg"
        if os.path.isfile(full_path):
            if datetime.datetime.fromtimestamp(
                    os.path.getmtime(full_path)).year > 2010:
                found.append(code)
    return found


def read_csv_in(input_file):
    """
    reads the target csv with data from SQL report for line
    non-retail only and produces a list
    """
    with open(input_file, "r") as f_in:
        all_data = list(csv.reader(f_in))
    return all_data


def build_output_list(new_items, photo_list):
    """
    builds the file, with full supplier names and
    if photo has been taken
    """
    tidy_list = []
    for line in new_items:
        photo = ""
        supplier_full = line[4]
        if line[2] in photo_list:
            photo = "Saddhayu"
        if line[4] in SUPPLIER_DICT:
            supplier_full = SUPPLIER_DICT[line[4]]
        tidy_list.append([line[0], line[1], line[2], line[3],
                         supplier_full, " ", photo])
    return tidy_list


def write_csv(tidy_list, input_file):
    """
    writes back to input csv
    """
    with open(input_file, "wb") as f_out:
        writer_file = csv.writer(f_out, delimiter=",")
        writer_file.writerows(tidy_list)


def main():
    """
    main loop
    """
    input_file = raw_input("Enter the csv file name: ")
    new_items = read_csv_in(input_file)
    photo_list = check_for_photo(new_items)
    tidy_list = build_output_list(new_items, photo_list)
    write_csv(tidy_list, input_file)


if __name__ == "__main__":
    main()
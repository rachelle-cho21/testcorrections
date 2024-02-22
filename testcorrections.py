#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 10:54:24 2024

@author: rachellecho
"""

def count_unique_proteins(proteins):
    return len({protein.split('.')[0] for protein in proteins})

def count_proteins(proteins):
    protein_dict = {}
    for protein in proteins:
        if protein in protein_dict:
            protein_dict[protein] += 1
        else:
            protein_dict[protein] = 1
    return protein_dict

def merge_protein_counts(dict_1, dict_2):
    combined_dict = {}
    protein_set = set(dict_1) | set(dict_2)
    for protein in protein_set:
        count_1 = dict_1.get(protein, 0)
        count_2 = dict_2.get(protein, 0)
        combined_dict[protein] = (count_1, count_2)
    return combined_dict

def dates_to_iso8601(dates_list):
    new_format = []
    month_dict = {'January': '01', 'February': '02', 'March': '03',
                  'April': '04', 'May': '05', 'June': '06',
                  'July': '07', 'August': '08', 'September': '09',
                  'October': '10', 'November': '11', 'December': '12'}
    for dates in dates_list:
        temporary = dates.replace(",", "").split(" ")
        month, day, year = temporary[0], temporary[1], temporary[2]
        month = month_dict[month]
        if len(day) < 2:
            day = '0' + day
        formatting = "{}-{}-{}".format(year, month, day)
        new_format.append(formatting)
    return new_format

def sort_dates(new_format):
    length_x = len(new_format)
    for x in range(length_x):
        for y in range(0, length_x - x - 1):
            if new_format[y] > new_format[y + 1]:
                new_format[y], new_format[y + 1] = new_format[y + 1], new_format[y]
    return new_format

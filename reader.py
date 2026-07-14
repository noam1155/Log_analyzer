import os
import csv


def list_from_csv2(file_path):
    with open(file_path, "r") as file:
        all_lines = [line.strip().split(",") for line in file]
        return all_lines











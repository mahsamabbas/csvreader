#Import Modules
import itertools
from collections import OrderedDict
import csv


def getHeaders(csv_file):
    """
    Read the first row and return values in a list
    """
    try:
        with open(csv_file, 'rt') as csvfile:
            file_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            headers = next(file_reader)
    except Exception:
        pass

    return headers

def getFileContent(csv_file, field_names, offset, limit):
    """
    Convert csv rows into an array of dictionaries
    """
    data_rows = []
    try:
        with open(csv_file, 'rt') as csvfile:
            file_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(file_reader)

            for row in itertools.islice(file_reader, offset, limit):
                data_rows.append(((OrderedDict(zip(field_names, row)))))

    except Exception:
        pass

    return data_rows
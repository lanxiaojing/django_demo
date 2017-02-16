# -*- coding: utf-8 -*-

import csv
from os import path
from parser import parse


class Configs(object):
    files_to_models = {"person.csv": "Person",
                       "couple.csv": "Couple",
                       "creditcard.csv": "Creditcard",
                       "loancard.csv": "Loancard",
                       "loan.csv": "Loan",
                       "query.csv": "Query",
                       "special.csv": "Special"}


class CSVLoader(object):

    dict_from_csv = {}

    def csv_to_dict(self, csv_path):
        fname = path.basename(csv_path)

        if fname in Configs.files_to_models.keys():
            with open(csv_path, 'rb') as csv_data:
                reader = csv.reader(csv_data)
                line = next(csv_data)
                fields = self._get_fields(line)
                self.dict_from_csv[fname] = []

                for row in reader:
                    m = {}
                    i = 0
                    for field in fields:
                        m[field] = row[i]
                        i = i + 1
                    self.dict_from_csv[fname].append(m)

    def load_to_mysql(self):
        self._load_person_firstly()
        self._load_other_secondly()

    def _get_fields(self, line):
        line = line.rstrip('\r\n')
        fields = line.split(",")
        return fields

    def _load_person_firstly(self):
        for fname, persons in self.dict_from_csv.iteritems():
            if fname == "person.csv":
                model = Configs.files_to_models[fname]
                self._load_general(model, persons)

    def _load_other_secondly(self):
        for fname, data_list in self.dict_from_csv.iteritems():
            if fname != "person.csv":
                model = Configs.files_to_models[fname]
                self._load_general(model, data_list)

    def _load_general(self, model, data_list):
        for data in data_list:
            m = model()
            for key, val in data.iteritems():
                setattr(m, key, val)
            m.save()


def load_csv():
    from fico863.load_data import CSVLoader
    paths = (
        # "/Users/zhongyid/projects/fico863/docs/csv/person.csv",
        # "/Users/zhongyid/projects/fico863/docs/csv/couple.csv",
        "/Users/zhongyid/projects/fico863/docs/csv/creditcard.csv",
        "/Users/zhongyid/projects/fico863/docs/csv/loancard.csv",
        "/Users/zhongyid/projects/fico863/docs/csv/loan.csv",
        "/Users/zhongyid/projects/fico863/docs/csv/query.csv",
        "/Users/zhongyid/projects/fico863/docs/csv/special.csv",
    )
    loader = CSVLoader()

    for _path in paths:
        loader.csv_to_dict(_path)
        loader.load_to_mysql()


if __name__ == "__main__":
    parse()

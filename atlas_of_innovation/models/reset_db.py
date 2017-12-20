import os
import sys
import transaction
import csv

from sqlalchemy import engine_from_config
from sqlalchemy import Column, String, Integer, Float 

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )
from .meta import DBSession, Base
from .innovation_space import Innovation_Space

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> <data_csv_file>\n'
          '(example: "%s development.ini most_up-to-date_spaces.csv")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) != 3:
        usage(argv)
    config_uri = argv[1]
    data_csv_file = argv[2]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.prepare(engine)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with open(data_csv_file) as csvfile:
        reader = csv.DictReader(csvfile)
        # replace empty strings with None
        complete_spaces = [{key: value if not value == '' else None for key, value in row.items()} for row in reader]
        processed_spaces = []
        for space in complete_spaces:
            processed_space = {}
            for attribute in Innovation_Space._column_names():
                processed_space[attribute]=space.pop(attribute, None)
            processed_space['other'] = space
            processed_spaces.append(processed_space)
        spaces = [Innovation_Space(**space) for space in processed_spaces]
        with transaction.manager:
            DBSession.add_all(spaces)
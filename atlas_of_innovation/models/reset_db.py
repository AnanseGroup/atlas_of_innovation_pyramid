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
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    def dynamic_space_schema():
        with open('atlas_of_innovation/models/most_up-to-date_spaces.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for key in reader.__next__().keys():
                if not getattr(Innovation_Space, key, None):
                    print ("setting "+ key)
                    setattr(Innovation_Space, key, Column(String))
    dynamic_space_schema()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with open('atlas_of_innovation/models/most_up-to-date_spaces.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        spaces = [{key: value if not value == '' else None for key, value in row.items()} for row in reader]
        spaces = [Innovation_Space(**space) for space in spaces]
        with transaction.manager:
            DBSession.add_all(spaces)
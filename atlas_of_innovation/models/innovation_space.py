import sqlalchemy
import psycopg2
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import EmailType

from .meta import Base


class Innovation_Space(Base):
    __tablename__ = "innovation_space"
    
    primary_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    aliases = Column(String)
    street_address = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    phone = Column(String)

    def __repr__(self):
        return "<Innovation_Space(name: %r at street_address: %r and email: %r)>" \
                    % (self.name, self.street_address, self.email)

    _column_names_list = None
    def _column_names(self):
      if not self._column_names_list:
        self._column_names_list = [x.__str__().split('.')[1] for x in self.__table__.columns]
      return self._column_names_list


    def __json__(self, request):
        return { column: getattr(self, column) for column in self._column_names() }



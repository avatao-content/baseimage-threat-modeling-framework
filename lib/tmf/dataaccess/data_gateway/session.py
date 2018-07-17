# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:////home/acsbendi/Documents/example.db', echo=True)

Session = sessionmaker(bind=engine)

session = Session()

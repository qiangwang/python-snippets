# -*- coding: utf-8 -*-

import json

from sqlalchemy import Column
from sqlalchemy.types import TypeDecorator, String

class JSON(TypeDecorator):
    '''
    Custom Column Type: JSON
    '''
    impl = String
    
    def process_bind_param(self, value, dialect):
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        if value:
            return json.loads(value)
        else:
            return value

if __name__ == '__main__':
    items = Column('items', JSON)
    print items.type

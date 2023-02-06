from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import blogs_schemas, models
from typing import List
from ..database import get_db
from ..repository import blogs
import math, random



router = APIRouter(
    prefix= '/settings',
    tags= ['settings']
)


@router.get('/')
def all():
    return {
        'Language' : 'ar',
        'Organization type' : [
            {'name':'Company',
             'mandatory': True},
            {'name' : 'University',
             'mandatory' : True},
            {'name':'Other',
             'mandatory' : False},
        ]
    }
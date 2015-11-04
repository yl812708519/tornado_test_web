#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from app.daos.sup_project_dao import SupProjectDao
from app.services.sup_project_service import SupProjectService

__author__ = 'freeway'


class UserDaoTestCase(unittest.TestCase):
    sup_project_service = SupProjectService()
    print sup_project_service.get_by_id(1)

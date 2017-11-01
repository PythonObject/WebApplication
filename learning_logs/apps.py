# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from models import *

class LearningLogsConfig(AppConfig):
    name = 'learning_logs'

    def ready(self):
        a = MergeBranchSource.objects.get(project_name='sfd')
        
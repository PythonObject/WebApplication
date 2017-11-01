# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class BranchSource(models.Model):
    source_id = models.IntegerField(default=None)
    using = models.NullBooleanField(default=False)
    project = models.OneToOneField('MergeBranchSource',on_delete=models.CASCADE, related_name='source', default=None)


class MergeBranchSource(models.Model):
    project_name = models.CharField(max_length=20, default=None)
    # source = models.ForeignKey(BranchSource, on_delete=models.CASCADE, related_name='project')

class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        """返回模型的字符串表示"""
        return self.text






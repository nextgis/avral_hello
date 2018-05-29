# -*- coding: utf-8 -*-

import os

from celery.utils.log import get_task_logger

from avral import avral
from avral.operation import AvralOperation
from avral.io.types import *

from avral.io.responce import AvralResponce

logger = get_task_logger(__name__)


class HelloWorld(AvralOperation):
    """docstring for HelloWorld"""
    def __init__(self):
        super(HelloWorld, self).__init__(
            name="hello",
            inputs={
                u"name": StringType(length=5),
                # u"names": ArrayType(StringType(length=5)),
                # u"value": FloatType(unsigned=True),
                # u"values": ArrayType(FloatType()),
                # u"bbox": BoundingBoxType(max_n=60),
            },
            outputs={
                u"hello": StringType(length=25),
                # u"hellos": ArrayType(StringType(length=25)), 
                # u"x2": FloatType(unsigned=True),
                # u"x2s": ArrayType(FloatType()),
                # u"bbox_area": FloatType(),
            },
        )
    
    def _do_work(self):
        # Unique code
        task_id = self.task_id

        #Get config option
        greeting = self.get_config_option("GREETING", default="Hello")

        name = self.getInput(u"name")
        # names = self.getInput(u"names")
        # value = self.getInput(u"value")
        # values = self.getInput(u"values")
        # bbox = self.getInput(u"bbox")

        hello = "%s, %s!" % (greeting, name)
        # hellos = ["%s, %s!" % (greeting, name) for name in names]
        # x2 = value * 2
        # x2s = [value * 2 for value in values]
        # bbox_area = (bbox["n"] - bbox["s"]) * (bbox["e"] - bbox["w"])
        
        # Директория для хранения временных файлов
        #   Будет удалена после завершения задачи
        # self.workdir

        self.setOutput(u"hello", hello)
        # self.setOutput(u"hellos", hellos)
        # self.setOutput(u"x2", x2)
        # self.setOutput(u"x2s", x2s)
        # self.setOutput(u"bbox_area", bbox_area)

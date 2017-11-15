# -*- coding: utf-8 -*-

import os

from avral.celery import avral, get_task_logger
from avral.operation import AvralOperation
from avral.io.types import String, Float, ListOfFloats, File

logger = get_task_logger(__name__)


class HelloWorld(AvralOperation):
    """docstring for HelloWorld"""
    def __init__(self):
        super(HelloWorld, self).__init__(
            name="hello",
            inputs={
                u"name": String,
            },
            outputs={
                u"hello": String,  
            },
        )
    
    def _do_work(self):
        name = self.getInput(u"name").value

        hello = "Hello, %s!" % name

        # Директория для хранения временных файлов
        #   Будет удалена после завершения задачи
        # self.workdir

        self.setOutput(u"hello", hello)

# -*- coding: utf-8 -*-

import os
import time

from avral import avral
from avral.operation import AvralOperation
from avral.io.types import *

from avral.io.responce import AvralResponce


class HelloWorld(AvralOperation):
    """docstring for HelloWorld"""
    json_schema1 = {
        "type": "array",
        "items": {
            "type": "object",
            "properties" : {
                "name" : {"type" : "string"},
                "greeting" : {"type" : "string"},
            },
        },
        "minItems" : 2,
        "maxItems" : 5,
    }

    description = {
        'en': 'Operation for <b>test</b> purposes.' +
        ' Return greeting string for given name.',
        'ru': 'Опе рация для проведения <b>теста</b>.' +
        ' Возвращает строку приветствия для заданного имени.',
    }

    #length - это максимальная длинна, а не минимальная
    def __init__(self):
        super(HelloWorld, self).__init__(
            name="hello",
            inputs={
                u"name": StringType(length=5),
                # u"names": ArrayType(StringType(length=5)),
                # u"value": FloatType(unsigned=True),
                # u"values": ArrayType(FloatType()),
                # u"bbox": BoundingBoxType(max_n=60),
                # u"json": JsonType(HelloWorld.json_schema1),
            },
            outputs={
                u"hello": StringType(length=25),
                # u"file": FileType(),
                # u"hellos": ArrayType(StringType(length=25)), 
                # u"x2": FloatType(unsigned=True),
                # u"x2s": ArrayType(FloatType()),
                # u"bbox_area": FloatType(),
                # u"hellos_from_json": ArrayType(StringType()),
            }
        )

    def _do_work(self):
        # Unique code
        task_id = self.task_id

        #Get config option
        greeting = self.get_config_option("GREETING", default="Hello")

        self.logger.info("Start hello!")
        time.sleep(5)
        self.logger.info("Stop hello!")

        name = self.getInput(u"name")
        # names = self.getInput(u"names")
        # value = self.getInput(u"value")
        # values = self.getInput(u"values")
        # bbox = self.getInput(u"bbox")
        # json_data = self.getInput(u"json")

        hello = "%s, %s!" % (greeting, name)
        # hellos = ["%s, %s!" % (greeting, name) for name in names]
        # x2 = value * 2
        # x2s = [value * 2 for value in values]
        # bbox_area = (bbox["n"] - bbox["s"]) * (bbox["e"] - bbox["w"])
        
        # Директория для хранения временных файлов
        #   Будет удалена после завершения задачи
        # self.workdir

        # hellos_from_json = []
        # for options in json_data:
        #     hellos_from_json.append(
        #         "%s, %s!" % (options["greeting"], options["name"])
        #     )

        self.setOutput(u"hello", hello)
        # self.setOutput(u"hellos", hellos)
        # self.setOutput(u"x2", x2)
        # self.setOutput(u"x2s", x2s)
        # self.setOutput(u"bbox_area", bbox_area)
        # self.setOutput(u"hellos_from_json", hellos_from_json)

        # greeting_file = os.path.join(self.workdir, "greeting.txt")
        # with open(greeting_file, "w") as f:
        #     f.write(hello)
        # self.setOutput(u"file", greeting_file)

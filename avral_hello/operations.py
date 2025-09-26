import time

from avral.i18n import LStr
from avral.io import Input, Output, StringType
from avral.operation import AvralOperation


class HelloWorld(AvralOperation):
    avral_name = "hello"

    avral_alias = LStr(
        en="Hello, World!",
        ru="Привет, Мир!",
    )

    avral_description = LStr(
        en="Allows to test Toolbox service. Returns a greeting string for a given name.",
        ru="Тестирование сервиса Toolbox. Возвращает строку приветствия для заданного имени.",
    )

    # Input parameters
    name: Input[StringType] = StringType(
        alias=LStr(en="Name", ru="Имя"),
        description=LStr(
            en="Please, type your name.",
            ru="Пожалуйста, укажите, как к вам обращаться.",
        ),
    )

    sleep: Input[StringType] = StringType(
        alias=LStr(en="Delayed start", ru="Отложенный запуск"),
        description=LStr(
            en="Optional field. You can set a delay for the tool's run in seconds.",
            ru="Опциональное поле. Можно отложить запуск инструмента, указав задержку в секундах.",
        ),
        optional=True,
    )

    # Output parameters
    hello: Output[StringType] = StringType(
        alias=LStr(en="", ru=""),
        description=LStr(
            en="",
            ru="",
        ),
        length=50,
    )

    def _do_work(self):
        # Get config option
        greeting = self.get_config_option("GREETING", default="Hello")
        self.logger.info("Start hello!")
        name = self.get_input("name")
        # names = self.getInput(u"names")
        # value = self.getInput(u"value")
        # values = self.getInput(u"values")
        # bbox = self.getInput(u"bbox")
        # json_data = self.getInput(u"json")
        try:
            sleep = int(self.get_input("sleep"))
            if sleep > 999:
                sleep = 999
            elif sleep < 0:
                sleep = 0
        except Exception:
            sleep = 0

        self.logger.info(f"Sleep {str(sleep)} seconds")
        time.sleep(sleep)
        hello = "%s, %s!" % (greeting, name)
        self.logger.info("Stop hello!")
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

        self.set_output("hello", hello)
        # self.setOutput(u"hellos", hellos)
        # self.setOutput(u"x2", x2)
        # self.setOutput(u"x2s", x2s)
        # self.setOutput(u"bbox_area", bbox_area)
        # self.setOutput(u"hellos_from_json", hellos_from_json)

        # greeting_file = os.path.join(self.workdir, "greeting.txt")
        # with open(greeting_file, "w") as f:
        #     f.write(hello)
        # self.setOutput(u"file", greeting_file)

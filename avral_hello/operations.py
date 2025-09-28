import time

from avral.i18n import LStr
from avral.io import Input, IntType, Output, StringType
from avral.operation import AvralOperation


class HelloTool(AvralOperation):
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

    sleep: Input[IntType] = IntType(
        alias=LStr(en="Delayed start", ru="Отложенный запуск"),
        description=LStr(
            en="You can set a delay for the tool's run in seconds.",
            ru="Можно отложить запуск инструмента, указав задержку в секундах.",
        ),
        optional=True,
    )

    # Output parameters
    result: Output[StringType] = StringType(
        alias=LStr(en="", ru=""),
        description=LStr(
            en="",
            ru="",
        ),
        length=50,
    )

    def _do_work(self):
        name_value = self.get_input("name")

        if sleep_value := self.get_input("sleep"):
            assert type(sleep_value) is int
            sleep_value = min(sleep_value, 600)
            self.logger.info("Sleeping %d seconds", sleep_value)
            time.sleep(sleep_value)

        result = f"Hello, {name_value}"
        self.set_output("result", result)

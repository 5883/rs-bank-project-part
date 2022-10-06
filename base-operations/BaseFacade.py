from steps.StepsOutOperations import *
from common-check-tools import *

class BaseFacade(StepsOutOperations):
    buttons = common-check-tools.HotButtons

    def __init__(self) -> None:
        super().__init__()
        self.buttons = buttons.getButtons()
        self.tools = common-check-tools.HotTools

    # Декортаор для запуска тестов
    def start_test(self, func):
        def prepare_for_testing(*args, **kwargs):
            self.before_test_operation()
            result = func(*args, **kwargs)
            self.after_test_operation()
            return result

        return prepare_for_testing


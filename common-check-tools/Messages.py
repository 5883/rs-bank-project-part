# Декортор. Message

class Msg():

    def __init__(self) -> None:
        self.object_name = "Объект"

    # Метод для вывода сообщений об ошибке в объекте
    def obj_msg(self, func):
        def func_msg(*args, **kwargs):
            function_to_check = func(*args, **kwargs)
            if function_to_check is None or function_to_check != True:
                Log.Warning(f'{self.object_name}  не найден')
            return function_to_check

        return func_msg




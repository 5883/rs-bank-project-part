# Класс для работы с исключениями/обработчик ошибок
class BugHunter:

    def __init__(self) -> None:
        super().__init__()

    #
    def __call__(self, func):
        def errorsHandler(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except:
                Log.Error(f'Исключение "AttributeError". Ожидаемый объект не сформирован!')
                Sys.Process("termw").Terminate()

        return errorsHandler
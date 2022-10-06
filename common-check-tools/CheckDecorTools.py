from Checks import CheckObjectTools


class CheckDecorTools(CheckObjectTools):

    def __init__(self) -> None:
        super().__init__()

    # --------------------- Проверка объекта на наличие, доступность и корректное отображение  ---------------------
    def checked(self, func):
        def check_this_object(*args, **kwargs):
            window_to_check = func(*args, **kwargs)
            window_to_check.Refresh()
            if window_to_check is not None and self.check_object_to_correct_display(window_to_check):
                return window_to_check
            else:
                Log.Warning(f'Объект "{args[1]}" не найден!')

        return check_this_object

    # --------------------- Проверка поля на наличие и на доступность для ввода ---------------------
    def checked_field(object):
        def additional_dec(self, func):
            def check_this_object(object, *args):
                field_to_check = func(object, *args)
                if self.check_field_to_input(field_to_check) != True:
                    return field_to_check
                else:
                    Log.Warning(f'Поле "{len(args)}" недоступно!')

            return check_this_object

        return additional_dec









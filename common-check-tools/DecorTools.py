import Messages
import ObjectTools


class DecorTools(ObjectTools):
    msg_cls = Messages.Msg()
    msg = msg_cls.obj_msg

    def __init__(self) -> None:
        super().__init__()

    # --------------------- Проверка объекта на наличие, доступность и корректное отображение  ---------------------
    # @msg
    def checked(self, func):
        def check_this_object(*args, **kwargs):
            window_to_check = func(*args, **kwargs)
            if window_to_check is not None and self.check_object_to_correct_display(window_to_check):
                return window_to_check
            else:
                Log.Warning(f'Объект "{args[1]}" не найден!')

        return check_this_object

    # --------------------- Проверка поля на наличие и на доступность для ввода ---------------------
    # @msg
    def checked_field(self, func):
        def check_this_object(*args, **kwargs):
            field_to_check = func(*args, **kwargs)
            if self.check_field_to_input(field_to_check) != True:
                return field_to_check
            else:
                Log.Warning(f'Поле "{len(args)}" недоступно!')

        return check_this_object

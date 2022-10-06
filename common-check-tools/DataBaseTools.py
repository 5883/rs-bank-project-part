# CRUD конфигурационными файлами
from configparser import ConfigParser
from BugHunters import BugHunter
import os


class ConfigFile:
    bug = BugHunter

    def __init__(self):
        self.stat = False

    @bug("Создание файла")
    def create_config(self, path):
        """
        Создает файл конфигурации
        """
        config = ConfigParser()

        with open(path, "w") as config_file:
            config.write(config_file)

    @bug("Объект конфигурации")
    def get_config(self, path):
        """
        Возвращает объект конфигурации
        """
        config = ConfigParser()
        if not os.path.exists(path):
            self.create_config(path)
            config = ConfigParser()
        config.read(path)
        return config

    @bug("Получение результата")
    def get_setting(self, section, setting, path):
        """
        Получить результат
        """
        config = self.get_config(path)
        value = config.get(section, setting)
        msg = "{section} {setting} is {value}".format(
            section=section, setting=setting, value=value
        )
        return value

    @bug("Обновление настройки")
    def update_setting(self, path, section, setting, value):
        """
        Обновляет настройку
        """
        config = self.get_config(path)
        config.set(section, setting, value)
        with open(path, "w") as config_file:
            config.write(config_file)

    @bug("Удаление настройки")
    def delete_setting(self, path, section, setting):
        """
        Обновить настройку
        """
        config = self.get_config(path)
        config.remove_option(section, setting)
        with open(path, "w") as config_file:
            config.write(config_file)


class ExcelFile:

    def __init__(self, ):  # def __init__(self, sheet_name) -> None:
        self.counter = 0
        self.status = False
        self.checked_column_value = ''
        self.full_path_to_file = Project.Path + Project.Variables.excel_file_path
        self.sheet_name = "operations"

    # ------------------------------- Метод для возвращения значения необходимого столбца из Excel -------------------------------
    def get_xls(self, desired_value_name):
        try:
            ddtExcel = DDT.ExcelDriver(self.full_path_to_file, self.sheet_name, True)
            while ddtExcel.EOF() != True:
                if str(ddtExcel.Value["OPER_NAME"]) == Project.TestItems.Current.Name:
                    requestValue = str(ddtExcel.Value[desired_value_name])
                    return requestValue
                ddtExcel.Next()
            DDT.CloseDriver(ddtExcel.Name)
            return None
        except:
            raise
            Log.Error(f'Найдена ошибка  необходимо запустить операцию из планировщика')


class Oracle(ConfigFile):

    def __init__(self) -> None:
        self.path = Project.Path + Project.Variables.config_file_path  # f"Data Source={self.data_source}; User id=rsuser; Password=Rbpzr_Rbpzr888"

    # ------------------------------- Получение данных из БД Oracle -------------------------------
    def get_oracle(self, assert_column_name):
        try:
            data_source = self.get_setting("oracle", "data_source", self.path)
            user_id = self.get_setting("oracle", "user_id", self.path)
            psw = self.get_setting("oracle", "psw", self.path)
            used_select = self.get_setting("oracle", "select", self.path)

            Qry = ADO.CreateADOQuery()
            Qry.ConnectionString = f'Data Source={data_source}; User id={user_id} Password={psw}'
            Qry.SQL = str(used_select)

            # Значение параметра
            Qry.Open()
            Qry.First()
            while not Qry.EOF:
                Log.Message(Qry.FieldByName(assert_column_name).Value)
                Qry.Next()

            Qry.Close()
        except:
            Log.Warning(f'Ошибка при соединении с БД (Oracle -> Testcomplete)')


''' Класс для работы с Базами Данных'''


class Database:

    def __init__(self) -> None:
        self.counter = 0
        self.status = False
        self.checked_column_value = ''
        self.data_source = get_setting("project", "stand", Project.Path + "ConfigFiles\setting.ini")
        self.connExcell = "\\mainDB.xlsx"

    # -------------------------------Метод для оперделния листа в Excel-------------------------------

    def setSheetToExcel(self, sheetName):

        # Передать наименование листа в Excel

        Project.Variables.ExcelSheet = sheetName
        Log.Message(f'Config file sheet name: "{Project.Variables.ExcelSheet}"')

    # ------------------------------- Метод для возвращения значения необходимого столбца из Excel-------------------------------
    def getXls(self, valToExcel):

        # valToExcel -  наименование столбца из Excel

        # connExcell = "\\mainDB.xlsx" # Путь до эксель
        thisXlsSheet = str(Project.Variables.ExcelSheet)
        ddtExcel = DDT.ExcelDriver(Project.Path + self.connExcell, thisXlsSheet, True)
        iterCount = str(1)  # Project.TestItems.Current.Iteration
        requestValue = f'Данный "{valToExcel}" отсутсвует'

        while ddtExcel.EOF() != True:
            if str(ddtExcel.Value["ID"]) == iterCount:
                requestValue = str(ddtExcel.Value[valToExcel])
            ddtExcel.Next()
        DDT.CloseDriver(ddtExcel.Name)
        return requestValue

    # ------------------------------- Метод для возвращения значения столбца из Excel (пока для операции "Ввод платежного поручения")-------------------------------II
    def getXlsX(self, valToExcel):

        # valToExcel -  наименование столбца из Excel

        connExcell = get_setting("forms", "path_to_formEnteringPaymentOrder")  # Путь до эксель
        ddtExcel = DDT.ExcelDriver(Project.Path + connExcell, "entering_payment_orders", True)
        iterCount = Project.TestItems.Current.Iteration
        requestValue = f'Данный "{valToExcel}" отсутсвует'
        operation_name = Project.TestItems.Current.Parent.Name

        while ddtExcel.EOF() != True:
            if str(ddtExcel.Value["OPERATION"]) == str(operation_name):
                requestValue = str(ddtExcel.Value[valToExcel])
            ddtExcel.Next()
        DDT.CloseDriver(ddtExcel.Name)
        return requestValue

    # ------------------------------- Получение данных из БД Oracle -------------------------------
    def getOracle(self):

        Qry = ADO.CreateADOQuery()
        Qry.ConnectionString = f"Data Source={self.data_source}; User id=rsuser; Password=Rbpzr_Rbpzr888"
        Qry.SQL = "select pr.t_requestid, pr.t_iin, pr.t_account, pr.t_account, pr.t_amount_available from PAYROLL_REPAYM PR where t_account in ('KZ879480012A02701621','KZ299480012A02726139') order by PR.t_paymentid"  # , "

        #  # Значение параметра
        # Log.Checkpoint(Qry.Parameters.ParamByName("test")).Value = "id"
        Qry.Open()

        # Log.AppendFolder("id value from tableName")
        Qry.First()
        while not Qry.EOF:
            Log.Message(Qry.FieldByName("t_requestid").Value)
            Qry.Next()

        Qry.Close()

    # ------------------------------- №4. Проверка зачисления сумм в WAY4 на уровне БД -------------------------------
    # Метод обращается к БД, проверяет на наличие значении в указанном столбце
    def check_in_database(self, select, column_name, compare_value):

        """ select - выборка
            column_name - наименование столбца
            compare_value - значение с для проверки/сравнения """

        Qry = ADO.CreateADOQuery()
        Qry.ConnectionString = f"Data Source={self.data_source}; User id; Password"
        Qry.SQL = select
        i = 0
        while (self.status == False) or (i <= 5):

            Log.AppendFolder("Результат проверки БД / Данные из таблицы")
            Qry.Open()
            Qry.First()

            while not Qry.EOF:
                self.checked_column_value = str(Qry.FieldByName(column_name).Value)
                if (self.checked_column_value == str(compare_value)):
                    Log.Checkpoint(f'Значение "{compare_value}" найдено')
                    Log.Message(f'Поиск завершен. Закрытие БД')
                    self.status = True
                    Qry.Close()
                    break
                Qry.Next()
            Qry.Close()
            # Log.Message("Конец таблицы. Закрытие БД")
            Delay(15000)
            i += 1
            if self.status == True:
                return self.status

    # ------------------------------- Получение данных из текстового файла -------------------------------
    # Читать весь файл
    def ReadWholeFile(self, filePath):
        string = aqFile.ReadWholeTextFile(filePath, aqFile.ctANSI)
        checkString = string
        if checkString:
            return checkString

    # Читать файл построчно
    def ReadFileLines(self, AFileName):
        F = aqFile.OpenTextFile(AFileName, aqFile.faRead, aqFile.ctANSI)
        F.Cursor = 0
        Log.Message("File by lines:")
        while not F.IsEndOfFile():
            s = F.ReadLine()
            Log.Message(s)
        F.Close()

    # ------------------------------- Получение данных из БД Oracle -------------------------------
    def getOracleTest(self, select, *args):

        Qry = ADO.CreateADOQuery()
        Qry.ConnectionString = f"Data Source={self.data_source}; User id=rsuser; Password=Rbpzr_Rbpzr888"
        Qry.SQL = select

        #  # Значение параметра
        # Log.Checkpoint(Qry.Parameters.ParamByName("test")).Value = "id"
        Qry.Open()

        # Log.AppendFolder("id value from tableName")
        Qry.First()
        Log.Message(f'type: {type(Qry.First())}')
        while not Qry.EOF:
            for i in args:
                val = Qry.FieldByName(i).Value
                Log.Message(type(val))
                if isinstance(val, str):
                    Log.Message(f'{val}')
                else:
                    Log.Warning("Пусто")
                Qry.Next()
        Qry.Close()
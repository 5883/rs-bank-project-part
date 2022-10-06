from ConfigFile import ConfigFile


class ExcelTools(ConfigFile):

    def __init__(self, sheet_name):
        super().__init__()
        self.file_path = self.get_setting("forms", "path_to_customer_input_window")
        self.sheet_name = sheet_name

    # метод получения данных из Excel
    def getXls(self):
        DDT.ExcelDriver(self.file_path, self.sheet_name)

        while not DDT.CurrentDriver.EOF():
            Log.Message(DDT.CurrentDriver.Value[0])
            DDT.CurrentDriver.Next()

        DDT.CloseDriver(DDT.CurrentDriver.Name)




class ObjectPage():
    @staticmethod
    def login_span():
        return "//span[text()='Register/Login']"

    @staticmethod
    def login_email():
        return "//*[@id='loginEmail']"

    @staticmethod
    def login_password():
        return "//*[@id='password']"

    @staticmethod
    def remember_check():
        return "//*[@name='remember']"

    @staticmethod
    def login_button():
        return "//*[@id='submit']"

    @staticmethod
    def forgot_password_button():
        return "//*[text()='Forgot password?']"

    @staticmethod
    def alert_login():
        return "/html/body/div[2]/div/p[1]/strong"

    @staticmethod
    def verify_login_success():
        return "/html/body/div[2]/div/p[1]/strong"

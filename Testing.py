from WebInterface import WebInterface
from ObjectPage import  ObjectPage

#Parameter
link = "https://anotepad.com/"
loginEmail = "nhntuong@shopee.com"
loginPassword = "12345678"
invalidEmail = "abc@123"
invalidPassword = "1234"
invalidSyntaxemail = "12345"

############Testing login function of website anotepad.com ################

#Testcase 1: check login span is exited
def testcase1():
    #step 1: start web and go to link anotepad.com
    try:
        tc1 = WebInterface()
        tc1.start_browser(link)
        #verify 1: verify login button is exist:
        if tc1.check_element_exist(ObjectPage.login_span()):
            print("Passed: Login span is existed")
        else:
            print("Failed: Login span does not exist")
    except:
        print("Failed: Something wrong, please check this function")
    finally:
        tc1.close_browser()

#Testcase 2: Check all information is displays after click login span
    #step 1: start web and go to link anotepad.com
def testcase2():
    try:
        tc2 = WebInterface()
        tc2.start_browser(link)
        # verify 1: verify login button is exist:
        if tc2.check_element_exist(ObjectPage.login_span()):
            print("Passed: Login span is existed")
        else:
            print("Failed: Login span does not exist")
        # step 2: click on login span:
        tc2.click_on_xpath(ObjectPage.login_span())
        # step 2: verify all information is displays after click login
        if tc2.check_element_exist(ObjectPage.login_password()):
            print("Passed: Login span is existed")
        else:
            print("Failed: Element does not exist")
        if tc2.check_element_exist(ObjectPage.login_email()):
            print("Passed: Element is existed")
        else:
            print("Failed: Login span does not exist")
        if tc2.check_element_exist(ObjectPage.login_button()):
            print("Passed: Element is existed")
        else:
            print("Failed: Element does not exist")
        if tc2.check_element_exist(ObjectPage.remember_check()):
            print("Passed: Element is existed")
        else:
            print("Failed: Element does not exist")
        if tc2.check_element_exist(ObjectPage.forgot_password_button()):
            print("Passed: Element is existed")
        else:
            print("Failed: Element does not exist")
    except:
        print("Failed: Something wrong, please check this function")
    finally:
        tc2.close_browser()

#Testcase 3: Login successful with user and pass
def testcase3():
    try:
        tc3 = WebInterface()
        tc3.start_browser(link)
        # verify 1: verify login button is exist:
        if tc3.check_element_exist(ObjectPage.login_span()):
            print("Passed: Login span is existed")
        else:
            print("Failed: Login span does not exist")
        # step 2: click on login span:
        tc3.click_on_xpath(ObjectPage.login_span())
        # step 2: verify all information is displays after click login
        if tc3.check_element_exist(ObjectPage.login_password()):
            print("Passed: Login span is existed")
        else:
            print("Failed: Element does not exist")
        if tc3.check_element_exist(ObjectPage.login_email()):
            print("Passed: Element is existed")
        else:
            print("Failed: Login span does not exist")
        if tc3.check_element_exist(ObjectPage.login_button()):
            print("Passed: Element is existed")
        else:
            print("Failed: Element does not exist")
        if tc3.check_element_exist(ObjectPage.remember_check()):
            print("Passed: Element is existed")
        else:
            print("Failed: Element does not exist")
        if tc3.check_element_exist(ObjectPage.forgot_password_button()):
            print("Passed: Element is existed")
        else:
            print("Failed: Element does not exist")

        #step 3: input all information
        tc3.send_key_on_element(ObjectPage.login_email(),loginEmail)
        tc3.send_key_on_element(ObjectPage.login_password(),loginPassword)
        tc3.click_on_xpath(ObjectPage.login_button())

        #Verify 3: Verify can login in this page (notepad login failed)
        if tc3.check_element_exist(ObjectPage.verify_login_success()):
            print("Passed: Element is existed")
        else:
            print("Failed: Element does not exist")
    except:
        print("Failed: Something wrong, please check this function")
    finally:
        tc3.close_browser()

#Testcase 4: Login Failed with wrong email
def testcase4():
    try:
        tc4 = WebInterface()
        tc4.start_browser(link)
        # verify 1: verify login button is exist:
        if tc4.check_element_exist(ObjectPage.login_span()):
            print("Passed: Login span is existed")
        else:
            print("Failed: Login span does not exist")
        # step 2: click on login span:
        tc4.click_on_xpath(ObjectPage.login_span())
        # step 2: verify all information is displays after click login
        if tc4.check_element_exist(ObjectPage.login_password()):
            print("Passed: Login span is existed")
        else:
            print("Failed: Element does not exist")
        if tc4.check_element_exist(ObjectPage.login_email()):
            print("Passed: Element is existed")
        else:
            print("Failed: Login span does not exist")
        if tc4.check_element_exist(ObjectPage.login_button()):
            print("Passed: Element is existed")
        else:
            print("Failed: Element does not exist")
        if tc4.check_element_exist(ObjectPage.remember_check()):
            print("Passed: Element is existed")
        else:
            print("Failed: Element does not exist")
        if tc4.check_element_exist(ObjectPage.forgot_password_button()):
            print("Passed: Element is existed")
        else:
            print("Failed: Element does not exist")

        #step 3: input all information
        tc4.send_key_on_element(ObjectPage.login_email(),invalidEmail)
        tc4.send_key_on_element(ObjectPage.login_password(),loginPassword)
        tc4.click_on_xpath(ObjectPage.login_button())

        #Verify 3: Verify cannot login in this page, alert is displays
        if tc4.check_element_exist(ObjectPage.alert_login()):
            print("Passed: Element is existed")
        else:
            print("Failed: Element does not exist")
    except:
        print("Failed: Something wrong, please check this function")
    finally:
        tc4.close_browser()

#Testcase 5: Login failed with wrong password
def testcase5():
    try:
        tc5 = WebInterface()
        tc5.start_browser(link)
        # verify 1: verify login button is exist:
        if tc5.check_element_exist(ObjectPage.login_span()):
            print("Passed: Login span is existed")
        else:
            print("Failed: Login span does not exist")
        # step 2: click on login span:
        tc5.click_on_xpath(ObjectPage.login_span())
        # step 2: verify all information is displays after click login
        if tc5.check_element_exist(ObjectPage.login_password()):
            print("Passed: Login span is existed")
        else:
            print("Failed: Element does not exist")
        if tc5.check_element_exist(ObjectPage.login_email()):
            print("Passed: Element is existed")
        else:
            print("Failed: Login span does not exist")
        if tc5.check_element_exist(ObjectPage.login_button()):
            print("Passed: Element is existed")
        else:
            print("Failed: Element does not exist")
        if tc5.check_element_exist(ObjectPage.remember_check()):
            print("Passed: Element is existed")
        else:
            print("Failed: Element does not exist")
        if tc5.check_element_exist(ObjectPage.forgot_password_button()):
            print("Passed: Element is existed")
        else:
            print("Failed: Element does not exist")

        #step 3: input all information
        tc5.send_key_on_element(ObjectPage.login_email(),loginEmail)
        tc5.send_key_on_element(ObjectPage.login_password(),invalidPassword)
        tc5.click_on_xpath(ObjectPage.login_button())

        #Verify 3: Verify cannot login in this page, alert is displays
        if tc5.check_element_exist(ObjectPage.verify_login_success()):
            print("Passed: Element is existed")
        else:
            print("Failed: Element does not exist")
    except:
        print("Failed: Something wrong, please check this function")
    finally:
        tc5.close_browser()

#Testcase 6: Login failed with both wrong email and password
def testcase6():
    try:
        tc6 = WebInterface()
        tc6.start_browser(link)
        # verify 1: verify login button is exist:
        if tc6.check_element_exist(ObjectPage.login_span()):
            print("Passed: Login span is existed")
        else:
            print("Failed: Login span does not exist")
        # step 2: click on login span:
        tc6.click_on_xpath(ObjectPage.login_span())
        # step 2: verify all information is displays after click login
        if tc6.check_element_exist(ObjectPage.login_password()):
            print("Passed: Login span is existed")
        else:
            print("Failed: Element does not exist")
        if tc6.check_element_exist(ObjectPage.login_email()):
            print("Passed: Element is existed")
        else:
            print("Failed: Login span does not exist")
        if tc6.check_element_exist(ObjectPage.login_button()):
            print("Passed: Element is existed")
        else:
            print("Failed: Element does not exist")
        if tc6.check_element_exist(ObjectPage.remember_check()):
            print("Passed: Element is existed")
        else:
            print("Failed: Element does not exist")
        if tc6.check_element_exist(ObjectPage.forgot_password_button()):
            print("Passed: Element is existed")
        else:
            print("Failed: Element does not exist")

        #step 3: input all information
        tc6.send_key_on_element(ObjectPage.login_email(),invalidEmail)
        tc6.send_key_on_element(ObjectPage.login_password(),invalidPassword)
        tc6.click_on_xpath(ObjectPage.login_button())

        #Verify 3: Verify cannot login in this page, alert is displays
        if tc6.check_element_exist(ObjectPage.verify_login_success()):
            print("Passed: Element is existed")
        else:
            print("Failed: Element does not exist")
    except:
        print("Failed: Something wrong, please check this function")
    finally:
        tc6.close_browser()

#Execute testscripts:
if __name__ == '__main__':
    testcase1()
    testcase2()
    testcase3()
    testcase4()
    testcase5()
    testcase6()

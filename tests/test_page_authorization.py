import pytest
import pages.Ver
from pages.RosTeleCom_page import RosTelecomPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Тест 1 позитивный авторизация по телефону
def test_authorization_phone_successfully(web_browser):

    page = RosTelecomPage(web_browser)
    page.phone.send_keys(pages.Ver.phone_valid)
    page.password.send_keys(pages.Ver.pass_valid)
    page.btn.click()
    #Проверяем что перешли на страницу с учетными данными пользователя
    assert WebDriverWait(web_browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'lk-btn')))


# Тест 2 позитивный авторизация по эл.почте
def test_authorization_email_successfully(web_browser):

    page = RosTelecomPage(web_browser)
    page.email.send_keys(pages.Ver.email_valid)
    page.password.send_keys(pages.Ver.pass_valid)
    page.btn.click()
    #Проверяем что перешли на страницу с учетными данными пользователя
    assert WebDriverWait(web_browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'lk-btn')))


# Тест 3 позитивный авторизация по логину
def test_authorization_login_successfully(web_browser):

    page = RosTelecomPage(web_browser)
    page.phone.send_keys(pages.Ver.login_valid)
    page.password.send_keys(pages.Ver.pass_valid)
    page.btn.click()
    #Проверяем что перешли на страницу с учетными данными пользователя
    assert WebDriverWait(web_browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'lk-btn')))


# Тест 4 позитивный авторизация по лицевому счету
def test_authorization_personal_account_successfully(web_browser):

    page = RosTelecomPage(web_browser)
    page.phone.send_keys(pages.Ver.account_valid)
    page.password.send_keys(pages.Ver.pass_valid)
    page.btn.click()
    #Проверяем что перешли на страницу с учетными данными пользователя
    assert WebDriverWait(web_browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'lk-btn')))


# Тест 5 позитивный авторизация по телефону введеных в разных форматах
@pytest.mark.parametrize('phone', pages.Ver.phones_valid)
def test_authorization_phones_successfully(web_browser, phone, password=pages.Ver.pass_valid):
    page = RosTelecomPage(web_browser)
    page.phone.send_keys(phone)
    page.password.send_keys(pages.Ver.pass_valid)
    page.btn.click()
    assert WebDriverWait(web_browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'lk-btn')))


# Тест 6 позитивный авторизация через одноклассники
def test_authorization_odnoclassnik_successfully(web_browser):

    page = RosTelecomPage(web_browser)
    page.btn_wndclass.click()
    # Переходим на страницу авторизации соцсети и вводим данные для авторизации
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.ID, 'field_email'))).send_keys(pages.Ver.email_odnoclass)
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.ID, 'field_password'))).send_keys(pages.Ver.pass_odnoclass)
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.button-pro[type="submit"]'))).click()
    #Проверяем что перешли на страницу с учетными данными пользователя
    assert WebDriverWait(web_browser, 10).until(EC.element_to_be_clickable((By.ID, 'lk-btn')))


# Тест 7 позитивный авторизация через соц.сеть В Контакте
def test_authorization_VKontakt_successfully(web_browser):

    page = RosTelecomPage(web_browser)
    page.btn_vk.click()
    # Проверяем переход на страницу авторизации соцсети
    assert WebDriverWait(web_browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'box_msg_padded')))


# Тест 8 позитивный авторизация через соц.сеть МэйлРу
def test_authorization_mail_successfully(web_browser):

    page = RosTelecomPage(web_browser)
    page.btn_mail.click()
    # Проверяем переход на страницу авторизации соцсети
    assert WebDriverWait(web_browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'header__logo')))


# Тест 9 позитивный авторизация через Гугл аакаунт
def test_authorization_google_successfully(web_browser):

    page = RosTelecomPage(web_browser)
    page.btn_google.click()
    # Проверяем переход на страницу авторизации соцсети
    assert WebDriverWait(web_browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'kHn9Lb')))


# Тест 10 позитивный авторизация через Яндекс ID
def test_authorization_yandex_successfully(web_browser):

    page = RosTelecomPage(web_browser)
    page.btn_yandex.click()
    # Проверяем переход на страницу авторизации соцсети
    assert WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'passp-add-account-page-title')))


#  Тест 11 негативный авторизация по телефону с не зарегистрировнным паролем
def test_auth_phone_negative_not_valid_password(web_browser):
    page = RosTelecomPage(web_browser)
    page.phone.send_keys(pages.Ver.phone_valid)
    page.password.send_keys(pages.Ver.pass_valid_1)
    page.btn.click()
    #Проверяем что нет перехода на страницу с учетными данными пользователя
    assert WebDriverWait(web_browser, 10).until(EC.element_to_be_clickable((By.ID, 'lk-btn')))


# Тест 12 негативный авторизация по эл.почте с не зарегистрировнным паролем
def test_auth_email_negative_not_valid_password(web_browser):

    page = RosTelecomPage(web_browser)
    page.email.send_keys(pages.Ver.email_valid)
    page.password.send_keys(pages.Ver.pass_valid_1)
    page.btn.click()
    #Проверяем что нет перехода на страницу с учетными данными пользователя
    assert WebDriverWait(web_browser, 10).until(EC.element_to_be_clickable((By.ID, 'lk-btn')))


# Тест 13 негативный авторизация по логину с не зарегистрировнным паролем
def test_auth_login_negative_not_valid_password(web_browser):

    page = RosTelecomPage(web_browser)
    page.phone.send_keys(pages.Ver.login_valid)
    page.password.send_keys(pages.Ver.pass_valid_1)
    page.btn.click()
    #Проверяем что нет перехода на страницу с учетными данными пользователя
    assert WebDriverWait(web_browser, 10).until(EC.element_to_be_clickable((By.ID, 'lk-btn')))


# Тест 14 негативный авторизация по лицевому счету с не зарегистрировнным паролем
def test_auth_personal_account_negative_not_valid_password(web_browser):

    page = RosTelecomPage(web_browser)
    page.phone.send_keys(pages.Ver.account_valid)
    page.password.send_keys(pages.Ver.pass_valid_1)
    page.btn.click()
    #Проверяем что нет перехода на страницу с учетными данными пользователя
    assert WebDriverWait(web_browser, 10).until(EC.element_to_be_clickable((By.ID, 'lk-btn')))


# Тест 15 негативный авторизация по телефону с пустым полем пароля
def test_auth_phone_negative_not_valid_password(web_browser):
    page = RosTelecomPage(web_browser)
    page.phone.send_keys(pages.Ver.phone_valid)
    page.password.send_keys('')
    page.btn.click()
    #Проверяем что нет перехода на страницу с учетными данными пользователя
    assert WebDriverWait(web_browser, 10).until(EC.element_to_be_clickable((By.ID, 'lk-btn')))


# Тест 16 негативный попытка авторизации с пустыми полями телефону и пароля
def test_auth_phone_negative_not_valid_password(web_browser):
    page = RosTelecomPage(web_browser)
    page.phone.send_keys('')
    page.password.send_keys('')
    page.btn.click()
    #Проверяем что нет перехода на страницу с учетными данными пользователя
    assert WebDriverWait(web_browser, 10).until(EC.element_to_be_clickable((By.ID, 'lk-btn')))


# Тест 17 негативный авторизация по эл.почте с пустым полем пароля
def test_auth_email_negative_not_valid_password(web_browser):
    page = RosTelecomPage(web_browser)
    page.email.send_keys(pages.Ver.email_valid)
    page.password.send_keys('')
    page.btn.click()
    #Проверяем что нет перехода на страницу с учетными данными пользователя
    assert WebDriverWait(web_browser, 10).until(EC.element_to_be_clickable((By.ID, 'lk-btn')))


# Тест 18 негативный авторизация по логину с пустым полем пароля
def test_auth_login_negative_not_valid_password(web_browser):
    page = RosTelecomPage(web_browser)
    page.phone.send_keys(pages.Ver.login_valid)
    page.password.send_keys('')
    page.btn.click()
    #Проверяем что нет перехода на страницу с учетными данными пользователя
    assert WebDriverWait(web_browser, 10).until(EC.element_to_be_clickable((By.ID, 'lk-btn')))


# Тест 19 негативный авторизация по лицевому счету с пустым полем пароля
def test_auth_account_negative_not_valid_password(web_browser):
    page = RosTelecomPage(web_browser)
    page.phone.send_keys(pages.Ver.account_valid)
    page.password.send_keys('')
    page.btn.click()
    #Проверяем что нет перехода на страницу с учетными данными пользователя
    assert WebDriverWait(web_browser, 10).until(EC.element_to_be_clickable((By.ID, 'lk-btn')))


# Тест 20 негативный авторизация с пустым полем телефона
def test_auth_phone_negative_not_valid_password(web_browser):
    page = RosTelecomPage(web_browser)
    page.phone.send_keys('')
    page.password.send_keys(pages.Ver.pass_valid)
    page.btn.click()
    #Проверяем что нет перехода на страницу с учетными данными пользователя
    assert WebDriverWait(web_browser, 10).until(EC.element_to_be_clickable((By.ID, 'lk-btn')))


# Тест 21 Негативный невалидные форматы имени
@pytest.mark.parametrize('names', pages.Ver.Name_not_valid)
def test_register_firstName_negative (web_browser,names):
    page = RosTelecomPage(web_browser)
    page.btn_reg.click()
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(names)
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.NAME, "lastName"))).send_keys(pages.Ver.lastName_valid)
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.ID,"address"))).send_keys(pages.Ver.phone_valid)
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))).send_keys(pages.Ver.pass_valid)
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.ID, 'password-confirm'))).send_keys(pages.Ver.pass_valid)
    WebDriverWait(web_browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.rt-btn[name="register"]'))).click()
    #Проверяем что нет перехода на страницу с учетными данными пользователя
    assert WebDriverWait(web_browser, 10).until(EC.element_to_be_clickable((By.ID, 'lk-btn')))


# Тест 22 Негативный невалидные форматы фамилии
@pytest.mark.parametrize('names', pages.Ver.Name_not_valid)
def test_register_lastName_negative(web_browser, names):
    page = RosTelecomPage(web_browser)
    page.btn_reg.click()
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(pages.Ver.firstName_valid)
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.NAME, "lastName"))).send_keys(names)
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.ID, "address"))).send_keys(pages.Ver.phone_valid)
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))).send_keys(pages.Ver.pass_valid)
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.ID, 'password-confirm'))).send_keys(pages.Ver.pass_valid)
    WebDriverWait(web_browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.rt-btn[name="register"]'))).click()
    #Проверяем что нет перехода на страницу с учетными данными пользователя
    assert WebDriverWait(web_browser, 10).until(EC.element_to_be_clickable((By.ID, 'lk-btn')))


# # Тест 23 Негативный невалидные форматы телефона или эл.почты
@pytest.mark.parametrize('addr', pages.Ver.address_not_valid)
def test_register_address_negative(web_browser, addr):
    page = RosTelecomPage(web_browser)
    page.btn_reg.click()
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(pages.Ver.firstName_valid)
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.NAME, "lastName"))).send_keys(pages.Ver.lastName_valid)
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.ID, "address"))).send_keys(addr)
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))).send_keys(pages.Ver.pass_valid)
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.ID, 'password-confirm'))).send_keys(pages.Ver.pass_valid)
    WebDriverWait(web_browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.rt-btn[name="register"]'))).click()
    #Проверяем что нет перехода на страницу с учетными данными пользователя
    assert WebDriverWait(web_browser, 10).until(EC.element_to_be_clickable((By.ID, 'lk-btn')))


# Тест 24 Негативный невалидные форматы пароля
@pytest.mark.parametrize('passwords', pages.Ver.passwords_not_valid)
def test_register_password_negative(web_browser, passwords):
    page = RosTelecomPage(web_browser)
    page.btn_reg.click()
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(pages.Ver.firstName_valid)
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.NAME, "lastName"))).send_keys(pages.Ver.lastName_valid)
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.ID, "address"))).send_keys(pages.Ver.phone_valid)
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))).send_keys(passwords)
    WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.ID, 'password-confirm'))).send_keys(passwords)
    WebDriverWait(web_browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.rt-btn[name="register"]'))).click()
    #Проверяем что нет перехода на страницу с учетными данными пользователя
    assert WebDriverWait(web_browser, 10).until(EC.element_to_be_clickable((By.ID, 'lk-btn')))


# python -m pytest -v --driver Chrome --driver-path /GoogleDriver/chromedriver.exe tests/test_page_authorization.py

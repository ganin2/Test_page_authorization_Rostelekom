from pages.base import WebPage
from pages.elements import WebElement


class RosTelecomPage (WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)

    phone = WebElement(id='username')
    email = WebElement(id='username')
    password = WebElement(id='password')
    btn = WebElement(class_name='rt-btn.rt-btn--orange')
    captcha_field = WebElement(id='captcha')
    captcha = WebElement(css_selector=".rt-captcha__image")


    btn_vk = WebElement(class_name='rt-base-icon--fill-path[alt="ВКонтакте"]')
    btn_wndclass = WebElement(class_name='rt-base-icon--fill-path[alt="Одноклассники.ru"]')
    btn_wndclass_email = WebElement(id="field_email")
    btn_wndclass_pass = WebElement(id="field_password")
    btn_mail = WebElement(class_name='rt-base-icon--fill-path[alt="Mail.ru"]')
    btn_google = WebElement(class_name='rt-base-icon--fill-path[alt="Google+"]')
    btn_yandex = WebElement(class_name='rt-base-icon--fill-path[alt="Yandex.ru"]')

    btn_agreement = WebElement(class_name='rt-link[target="_blank"]')
    btn_reg = WebElement(id="kc-register")



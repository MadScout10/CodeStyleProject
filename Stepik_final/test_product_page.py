import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import time


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_cart()  # добавляем товар в корзину
    page.solve_quiz_and_get_code()  # отправляем решение в alert для получения проверочного кода
    page.check_price()  # сверяем цену товара и цену в корзине
    page.check_product_name()  # сверяем имя товара и имя добавленного в корзину товара
    time.sleep(5)  # доп.ожидание, чтобы убедиться что все ок


@pytest.mark.skip
@pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket_promolinks(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_cart()  # добавляем товар в корзину
    page.solve_quiz_and_get_code()  # отправляем решение в alert для получения проверочного кода
    page.check_price()  # сверяем цену товара и цену в корзине
    page.check_product_name()  # сверяем имя товара и имя добавленного в корзину товара
    time.sleep(5)  # доп.ожидание, чтобы убедиться что все ок


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # проверяем, что ссылка на логин пейдж работает корректно


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_cart()  # добавляем в корзину
    page.should_not_be_success_message()  # ожидаем, что там нет сообщения об успешном добавлении в корзину


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_be_login_link()  # проверяем, что ссылка на логин пейдж присутствует на странице


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_cart()  # добавляем в корзину
    page.success_message_should_disappear()  # ожидаем, что там нет сообщения об успешном добавлении в корзину


@pytest.mark.skip
def test_success_message_should_not_be(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_not_be_success_message()  # ожидаем, что там нет сообщения об успешном добавлении в корзину
    page.add_to_cart()  # добавляем в корзину
    page.check_product_name()  # Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
    page.success_message_should_disappear()  # элемент присутствует на странице и должен исчезнуть


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_basket_page()  # переходим в корзину
    basket_page = BasketPage(browser, browser.current_url)  # инициализируем Page Object
    basket_page.empty_basket_check()  # проверяем, что корзина пуста
    basket_page.basket_is_empty_mark_check()  # проверяем наличие надписи "корзина пуста"


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "12345QAAuto"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.should_not_be_success_message()  # ожидаем, что там нет сообщения об успешном добавлении в корзину

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, setup):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.add_to_cart()  # добавляем товар в корзину
        page.check_price()  # сверяем цену товара и цену в корзине
        page.check_product_name()  # сверяем имя товара и имя добавленного в корзину товара
        time.sleep(5)  # доп.ожидание, чтобы убедиться что все ок

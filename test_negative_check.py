import pytest
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

@pytest.mark.xfail
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_basket()  # добавляем товар в корзину
    page.should_not_be_success_message()    # проверяем, что нет сообщения об успехе


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_not_be_success_message()    # проверяем, что нет сообщения об успехе


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_basket()  # добавляем товар в корзину
    page.should_be_disappeareded_message()  # проверяем, что нет сообщение пропало

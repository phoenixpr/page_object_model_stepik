from .pages.product_page import ProductPage

def test_guest_can_add_item_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_book_title_on_page("Coders at Work")     # проверяем что на странице есть название книги
    page.should_be_book_price_on_page("19,99")
    page.should_be_book_title_on_page_title("Coders at Work | Oscar - Sandbox")
    page.add_to_basket()        # добавляем товар в корзину
    page.solve_quiz_and_get_code()      # считаем результат
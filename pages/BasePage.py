from playwright.sync_api import Page

class BasePage:
    def __init__(self,page:Page):
        self.page=page
    def click(self,locator:str):
        self.page.wait_for_selector(locator, state="visible")
        self.page.click(locator)

    def fill(self,locator:str, value:str):
        self.page.wait_for_selector(locator, state="visible")
        self.page.fill(locator,value)

    def wait_for_element(self,locator:str):
        self.page.wait_for_selector(locator,state="visible")

    def get_text(self,locator:str)->str:
        return self.page.inner_text(locator)

    def retry_click(self, locator:str, retries:int = 3):
        for i in range(retries):
            try: 
                self.click(locator)
                return
            except:
                if i==retries-1:
                    raise
                self.page.wait_for_timeout(1000)

    def select_dropdown(self,locator:str, value:str):
        self.page.select_option(locator,value)

    def scroll_to(self,locator:str):
        self.page.eval_on_selector(locator,"el => el.scrollIntoView()")

    def press_enter(self,locator:str):
        self.page.press(locator,"Enter")

    def is_visible(self,locator:str):
        self.page.is_visible(locator)
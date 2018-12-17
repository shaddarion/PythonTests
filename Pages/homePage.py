class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.home_categories_block_class = 'home1-categories-block-content'

    def getHomeCategoriesBlock(self):
        return self.driver.find_element_by_class_name(self.home_categories_block_class)
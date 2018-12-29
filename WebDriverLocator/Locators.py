from WebDriver.UIElementLocator import UIElementLocator

class Locators:
    class NavigationBarChildPages:
        pageTitle                   = (UIElementLocator.CLASS_NAME, 'page-title')
        categoryContainer           = (UIElementLocator.CLASS_NAME, 'catalog-layred-tabs')
    class HomePage:
        class NavigationBar:
            bedRoomButton           = (UIElementLocator.ID, 'menu3')
            livingRoomButton        = (UIElementLocator.ID, 'menu5')
            diningAndKitchenButton  = (UIElementLocator.ID, 'menu4')
            officeButton            = (UIElementLocator.ID, 'menu117')
            barAndGameRoomButton    = (UIElementLocator.ID, 'menu7')
            accessoriesButton       = (UIElementLocator.ID, 'menu158')
            outdoorButton           = (UIElementLocator.ID, 'menu182')
            shopByBrandButton       = (UIElementLocator.ID, 'menubrand')
        

from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import account


def start():

    options = Options()
    options.headless = False
    fp = FirefoxProfile()
    fp.set_preference('geo.enabled', False)
    driver = webdriver.Firefox(firefox_profile=fp, options=options)
    wait = WebDriverWait(driver, 20)

    def word_entry(element, word):
        for char in word:
            element.send_keys(char)

    # checks if survey pops up
    def survey():
        print("Survey")
        checking_survey = True
        while checking_survey:
            try:
                driver.find_element_by_id('survey_invite_no').click()
                checking_survey = False
                print("   Declined")
                sleep(1)
            except NoSuchElementException:
                print("   No Survey")
                checking_survey = False

    # checks if spinner is invisible to continue to check out
    def spinner_check():
        try:
            WebDriverWait(driver, 4).until(ec.invisibility_of_element_located
                                           ((By.CLASS_NAME, "page-spinner")))
            print("Gone")

        except:
            print("Spinner Not There")
            pass

    print('Loading...')

    # Item of choice
    driver.get('https://www.bestbuy.com/site/evga-nvidia-geforce-rtx-3060'
               '-xc-gaming-12gb-gddr6-pci-express-4-0-graphics-card/6454329.p?skuId=6454329')
    # driver.get('https://www.bestbuy.com/site/nvidia-geforce-rtx-3080'
    #            '-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and'
    #            '-black/6429440.p?skuId=6429440')
    sleep(5)
    survey()

    # Account button drop down
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.account-button')))
    driver.find_element_by_css_selector('.account-button').click()
    print("***Found Account Button***")

    # Sign in button from drop down
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.sign-in-btn')))
    driver.find_element_by_css_selector('.sign-in-btn').click()
    print("***Found Sign-In Button***")
    #

    # ENTER EMAIL
    wait.until(ec.presence_of_element_located((By.ID, "fld-e")))
    email_address_el = driver.find_element_by_id("fld-e")
    word_entry(email_address_el, account.check_files_2()['Login Email'])
    print("***Entered Email***")
    #

    # ENTER PASSWORD
    wait.until(ec.presence_of_element_located((By.ID, "fld-p1")))
    email_password_el = driver.find_element_by_id("fld-p1")
    word_entry(email_password_el, account.check_files_2()['Login Pass'])
    print("***Entered Password***")
    #
    survey()

    # SUBMIT
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.c-button-secondary')))
    driver.find_element_by_css_selector('.c-button-secondary').click()
    print("***Logged In***")
    #
    survey()

    # CHECKING ADD TO CART
    i = 0
    sleep(5)
    buy_button = True
    while buy_button:
        sleep(0.5)
        print('    Checking {}'.format(i))
        survey()
        try:
            driver.find_element_by_class_name(".c-button-disabled")
            print('Sold Out')
            i += 1
            if i % 100 == 0:
                driver.refresh()
                print('Refreshed')
            if i == 1000:
                i = 0
        except:
            add_button = driver.find_element_by_class_name(".c-button-primary")
            sleep(0.8)
            add_button.click()
            buy_button = False

    spinner_check()
    print("***Found add to cart***")
    print('Checking for second button...Waiting Up to 25min ')
    WebDriverWait(driver, 1500).until(ec.element_to_be_clickable((By.CLASS_NAME, ".c-button-primary")))
    driver.find_element_by_class_name('btn-primary').click()
    print('Clicked second Add To Cart')
    sleep(1)
    driver.get("https://www.bestbuy.com/cart")
    print("***Loading Cart***")
    # Selects store pickup
    spinner_check()
    wait.until(ec.element_to_be_clickable((By.XPATH,
                                           '/html/body/div[1]/main/div/div[2]/div[1]/'
                                           'div/div[1]/div[1]/section[1]/div[4]/ul/li/'
                                           'section/div[2]/div[2]/form/div[2]/fieldset/'
                                           'div[1]/div[1]/div/div/div/input')))

    driver.find_element_by_xpath('/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]'
                                 '/div[1]/section[1]/div[4]/ul/li/section/div[2]/div[2]'
                                 '/form/div[2]/fieldset/div[1]/div[1]/div/div/div/input').click()

    wait.until(ec.element_to_be_clickable((By.CLASS_NAME, ".c-button-primary")))
    driver.find_element_by_xpath("/html/body").click()
    ship = driver.find_element_by_class_name(".c-button-primary")
    driver.execute_script("arguments[0].scrollIntoView(true);", ship)
    ship.click()
    print("***Checkout Button Hit***")

    # INFORMATION FOR SHOPPING CART
    wait.until(ec.element_to_be_clickable((By.XPATH,
                                           '/html/body/div[1]/div[2]/div/'
                                           'div[2]/div[1]/div[1]/main/div[2]'
                                           '/div[2]/form/section/div/div[2]/'
                                           'div/div/button')))

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]'
                                 '/div[1]/div[1]/main/div[2]/div[2]/form/section/'
                                 'div/div[2]/div/div/button').click()
    sleep(0.5)
    wait.until(ec.presence_of_element_located((By.ID, 'optimized-cc-card-number')))
    card = driver.find_element_by_id('optimized-cc-card-number')
    word_entry(card, account.check_files_2()['Card Number'])

    # ADDRESS
    wait.until(ec.presence_of_element_located((By.ID, 'payment.billingAddress.street')))
    address = driver.find_element_by_id('payment.billingAddress.street')
    word_entry(address, account.check_files_2()['Address'])
    print("**Added Street Address**")

    # FIRST NAME
    first_name = driver.find_element_by_id('payment.billingAddress.firstName')
    word_entry(first_name, account.check_files_2()['First Name'])
    print("**Added First Name**")

    # LAST NAME
    last_name = driver.find_element_by_id('payment.billingAddress.lastName')
    word_entry(last_name, account.check_files_2()['Last Name'])
    print("**Added Last Name**")

    # CITY
    city = driver.find_element_by_id('payment.billingAddress.city')
    word_entry(city, account.check_files_2()['City'])
    print("**Added City**")

    # ZIP CODE
    city_zip_code = driver.find_element_by_id('payment.billingAddress.zipcode')
    word_entry(city_zip_code, account.check_files_2()['ZipCode'])
    print("**Added ZipCode**")

    # SELECT STATE
    driver.find_element_by_id('payment.billingAddress.state').send_keys('CC')
    print("**Selected State**")

    # BUTTON TO CONTINUE
    security = driver.find_element_by_id('credit-card-cvv')
    word_entry(security, account.check_files_2()['Card CVV 3 Digits'])
    month = Select(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]"
                                                "/main/div[2]/div[3]/div/section/div[1]/div/section"
                                                "/div[2]/div[1]/div/div[1]/label/div/div/select"))
    month.select_by_value(account.check_files_2()['Card Expire Month'])

    year = Select(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]"
                                               "/main/div[2]/div[3]/div/section/div[1]/div/section"
                                               "/div[2]/div[1]/div/div[2]/label/div/div/select"))
    year.select_by_value(account.check_files_2()['Card Expire Year'])

    place_order = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]'
                                               '/main/div[2]/div[3]/div/section/div[4]/button')
    place_order.click()
    print('Purchase Completed! Thank you for using this code!')

class locators:
    # Login page webelements
    Logout_btn = "//*[@id='logout_sidebar_link']"
    Menu_btn = "//*[@id='react-burger-menu-btn']"
    About_btn = "//*[@id='about_sidebar_link']"
    Pwd = "password"
    uid = "user-name"
    Loginbtn = "login-button"
    Resetbtn = "btnReset"

    # Homepage or Landing page
    Add_to_Cart_product1 = "add-to-cart-sauce-labs-backpack"
    Add_to_Cart_product2 = "add-to-cart-sauce-labs-bike-light"
    Add_to_Cart_product3 = "add-to-cart-sauce-labs-bolt-t-shirt"
    Add_to_Cart_product4 = "add-to-cart-sauce-labs-fleece-jacket"
    Add_to_Cart_product5 = "add-to-cart-sauce-labs-onesie"
    Add_to_Cart_product6 = "add-to-cart-test.allthethings()-t-shirt-(red)"

    maincart_items = "//*[@id='shopping_cart_container']/a"
    Product1 = "//*[@id='item_4_title_link']/div"
    Product2 = "//*[@id='item_0_title_link']/div"
    Product3 = "//*[@id='item_1_title_link']/div"
    Product4 = "//*[@id='item_5_title_link']/div"
    Product5 = "//*[@id='item_2_title_link']/div"
    Product6 = "//*[@id='item_3_title_link']/div"

    # New Customer page web elements
    Newcustomerlink = "/html/body/div[3]/div/ul/li[2]/a"
    custname = "name"
    Gendermale = "/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]"
    Genderfemale = "/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]"
    Dob = "dob"
    Address = "addr"
    City = "city"
    State = "state"
    Pin = "pinno"
    mobilenum = "telephoneno"
    emailid = "emailid"
    password_txt = "password"
    submit_btn = "sub"
    reset_btn = "res"
    Confirmmesg = "//*[contains(text(),'Customer Registered Successfully!!!')]"
    custid = "//*[@id='customer']/tbody/tr[4]/td[2]"

    # Edit Customer page web elements
    Editcustomerlink = "/html/body/div[3]/div/ul/li[3]/a"
    Edit_custid = "cusid"
    Edit_submit = "AccSubmit"
    Reset = "reset"

from selenium import webdriver
import time


un_required = ['filters', 'categories', 'popular related searches', 'shop by category', 'gamer', 'wii', 'asus', 'acer',
               'acer', 'mac', 'dell', 'tablette', 'hp', 'clavier', 'casque', 'airpod', 'gaming', 'gameur', 'amd', 'pro',
               'ipad', 'iphone', 'pavé', 'samsung', 'écran', 'corsair', 'apple', 'i3', 'i7', 'ecran', 'geforce', 'rtx',
               'amilo', 'huawei', 'conteur', 'sony', 'enfant', 'magique', 'echange',
               'enceinte', "souris", "bureautique", 'bureau', "philips", 'tour', 'boitier', 'boîtier', 'touch',
               'clementoni', 'console', 'consoles', 'barette', 'bureau', 'clavier', 'souri', 'packard bell', 'packard',
               'xp', 'parleurs', 'maxxter', 'haut-parleurs', 'pieces', 'pièce', 'xeon', 'nvidia', 'zalman',
               'maintenance', 'schneider', 'micro', 'barrette', 'barrettes']

htmlItems = ''

htmlSetup = f""" <!DOCTYPE html>
<html>
<head>
	<title>Scrape</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<div>
		<h2 id="title">Possible Products</h2>
	</div>
	<div id="subtitle">Computers:
	</div>
	<div id="items">
            {htmlItems}
	</div>

</body>
</html>
            """


driver = webdriver.Chrome(executable_path='//Users/francesco/Desktop/Programming and Engineering/Python/Facebook '
                                          'Marketplace/chromedriver')


def setup():
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    url = 'https://www.facebook.com/marketplace/114881545191743/computers'
    driver.get(url)


def scrolling():
    last_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(1):
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(10)
        print(i)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def retrieve_lenovo():
    global htmlItems
    global htmlSetup

    items = driver.find_elements_by_xpath("//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz "
                                          "rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x "
                                          "jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl "
                                          "gmql0nx0 p8dawk7l']")

    for item in items:
        line_container = item.find_element_by_xpath(".//div[@class='a8nywdso e5nlhep0 rz4wbd8a linoseic']")
        line = line_container.find_element_by_xpath(".//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7']")

        text = line.text
        print(text)

        if any(word in text.lower() for word in un_required) is False:
            print(any(word in text.lower() for word in un_required))
            if check_description(item) is True:
                img = item.find_element_by_xpath(f".//img")

                temp = f"""<div id="object">
                <a class="title" href="{item.get_attribute('href')}">{text}</a>
                <img class="images" src="{img.get_attribute('src')}"></div> \n"""

                htmlItems = htmlItems + temp
                print(f"Name: {text}         img: {img.get_attribute('src')}")



    htmlSetup = f""" <!DOCTYPE html>
    <html>
    <head>
    	<title>Scrape</title>
    	<link rel="stylesheet" type="text/css" href="style.css">
    </head>
    <body>
    	<div>
    		<h2 id="title">Possible Products</h2>
    	</div>
    	<div id="subtitle">Computers:
    	</div>
    	<div id="items">
                {htmlItems}
    	</div>

    </body>
    </html>
                """

    print("--- END ---")


def check_description(item):
    time.sleep(3)
    item.click()
    time.sleep(3)

    try:
        description_div = driver.find_element_by_xpath("//div[@class='ii04i59q a8nywdso f10w8fjw rz4wbd8a pybr56ya']")
        description_actual = description_div.find_element_by_xpath(".//span[@class='d2edcug0 hpfvmrgz qv66sw1b "
                                                                   "c1et5uql oi732d6d ik7dh3pa ht8s03o8 a8c37x1j "
                                                                   "keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r "
                                                                   "mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v "
                                                                   "knj5qynh oo9gr5id']")
        print('in checking')

    except:
        print("not checked")
        driver.find_element_by_xpath("//div[@class='oajrlxb2 tdjehn4e qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv "
                                     "nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a "
                                     "qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l "
                                     "bp9cbjyn s45kfl79 emlxlaya bkmhp75w spb7xbtv rt8b4zig n8ej3o3l agehan2d sk4xxmp2 "
                                     "taijpn5t qypqp5cg q676j6op']").click()
        return True

    text = description_actual.text
    text = text.lower()
    print(f"Description is: {text}")

    if any(word in text for word in un_required):
        driver.find_element_by_xpath("//div[@class='oajrlxb2 tdjehn4e qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv "
                                     "nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a "
                                     "qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l "
                                     "bp9cbjyn s45kfl79 emlxlaya bkmhp75w spb7xbtv rt8b4zig n8ej3o3l agehan2d sk4xxmp2 "
                                     "taijpn5t qypqp5cg q676j6op']").click()
        return False
    else:
        driver.find_element_by_xpath("//div[@class='oajrlxb2 tdjehn4e qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv "
                                     "nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a "
                                     "qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l "
                                     "bp9cbjyn s45kfl79 emlxlaya bkmhp75w spb7xbtv rt8b4zig n8ej3o3l agehan2d sk4xxmp2 "
                                     "taijpn5t qypqp5cg q676j6op']").click()
        time.sleep(3)
        return True


def radius(rad):
    time.sleep(5)
    driver.find_element_by_xpath("//div[@class='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 "
                                 "goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv"
                                 " nhd2j8a9 j83agx80 mg4g778l btwxx1t3 pfnyh3mw p7hjln8o aov4n071 cxmmr5t8 oygrvhab"
                                 " hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h"
                                 " esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//div[@class='dwo3fsh8 g5ia77u1 ow4ym5g4 auili1gw nhd2j8a9 oygrvhab cxmmr5t8 "
                                  "hcukyx3x kvgmc6g5 l9j0dhe7 i1ao9s8h du4w35lb rq0escxv oo9gr5id j83agx80 jagab5yi "
                                  "knj5qynh fo6rh5oj lzcic4wl osnr6wyh hv4rvrfc dati1w0a p0x8y401 k4urcfbm']").click()
    time.sleep(1)
    options = driver.find_elements_by_xpath("//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa "
                                            "ht8s03o8 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w"
                                            " c8b282yb iv3no6db jq4qci2q a3bd9o3v ekzkrbhg oo9gr5id hzawbc8m']")
    for option in options:
        if rad in option.text:
            option.click()
            break
    time.sleep(1)
    driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn "
                                 "owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d "
                                 "sk4xxmp2 ni8dbmo4 stjgntxs d1544ag0 tw6a2znq s1i5eluu tv7at329']").click()
    time.sleep(5)


def write_website():
    global htmlSetup
    output = open('output.html', "w")
    output.write(htmlSetup)
    output.close()
    url = "file:///Users/francesco/Desktop/Programming%20and%20Engineering/Python/Facebook%20Marketplace/output.html"
    driver.get(url)


def check_lines(lines):

    line = lines.find_element_by_xpath(".//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa "
                                       "ht8s03o8 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w "
                                       "c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh oo9gr5id']")

    text = line.text



setup()
radius("10")
scrolling()
retrieve_lenovo()
write_website()






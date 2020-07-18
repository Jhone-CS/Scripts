from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def tracking():

        search = str(input('insira o codigo de rastreio: '))

        print('Buscando informações de rastreio...')

        #remove window from chrome
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        op.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=op)
        driver.get("https://www.linkcorreios.com.br/?id={}".format(search))

        #pagina inicial sem parametro por link        
        #element = driver.find_element_by_xpath("/html/body/div[1]/div[1]/main/section/div/div/form/div/div[1]/div/input")
        #element.clear()
        #element.send_keys(search)
        #element.send_keys(Keys.RETURN) 

        result = driver.find_element_by_xpath("/html/body/div[1]/div[1]/main/div[4]/div/div/div[1]/div/div/ul").text

        print('\n{}'.format(result))

        assert "Algo deu errado, tente novamente" not in driver.page_source

        driver.close()

def start():

    tracking()
    alter = ''
    alter = str(input('\nDe novo? (s/n) '))

    if alter == 's':
        tracking()
        alter = ''
        alter = str(input('\nDe novo? (s/n) '))
    elif alter == 'n':
        print('Sair')
    else:
        while alter != 's' and alter != 'n':
            print('Valor invalido')
            alter = ''
            alter = str(input('\nDe novo? (s/n) '))        

    while alter == 's':
        if alter == 's':
            tracking()
            alter = ''
            alter = str(input('\nDe novo? (s/n) '))
        elif alter == 'n':
            print('Sair')
        else:
            while alter != 's' and alter != 'n':
                print('Valor invalido')
                alter = ''
                alter = str(input('\nDe novo? (s/n) '))
    else:
        print('Saiu')

start()
        


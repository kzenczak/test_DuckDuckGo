import json
import pytest
import selenium.webdriver

@pytest.fixture
def config(scope='session'):
    with open('config.json') as config_file:
        config = json.load(config_file)

    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Firefox', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    return config


@pytest.fixture
def browser(config):
    # webdriver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Firefox':
        opts = selenium.webdriver.FirefoxOptions()
        opts.headless = True
        b = selenium.webdriver.Firefox(options=opts)
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # wait for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # return webdriver instance for the setup
    yield b

    b.quit()

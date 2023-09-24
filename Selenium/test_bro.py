
import yaml
from module import Site

with open('testdata.yaml') as fy:
    testdata = yaml.safe_load(fy)

site = Site(testdata['address'])


def test_authorize_invalid(selector_login, selector_password, selector_botton, selector_error, result_error):
    input_login = site.find_element(selector_login[0], selector_login[1])
    input_login.send_keys('test')
    input_pass = site.find_element(selector_password[0], selector_password[1])
    input_pass.send_keys('test')
    input_botton = site.find_element(selector_botton[0], selector_botton[1])
    input_botton.click()
    input_error = site.find_element(selector_error[0], selector_error[1])

    assert input_error.text == result_error


def test_authorize_valid(selector_login, selector_password, selector_botton, selector_hello, result_hello):
    input_login = site.find_element(selector_login[0], selector_login[1])
    input_login.clear()
    input_login.send_keys(testdata['username'])
    input_pass = site.find_element(selector_password[0], selector_password[1])
    input_pass.clear()
    input_pass.send_keys(testdata['password'])
    input_botton = site.find_element(selector_botton[0], selector_botton[1])
    input_botton.click()
    input_hello = site.find_element(selector_hello[0], selector_hello[1])

    assert input_hello.text == result_hello, 'not enty'
    site.driver.quit()


def test_add_new_post(selector_login, selector_password, selector_botton, selector_botton_new_post,
                      selector_title_new_post, selector_content_new_post, selector_description_new_post,
                      selector_bottonsave_new_post, selector_title_save_post):
    site = Site(testdata['address'])
    # site.driver.get(testdata['address'])
    input_login = site.find_element(selector_login[0], selector_login[1])
    input_login.clear()
    input_login.send_keys(testdata['username'])
    input_pass = site.find_element(selector_password[0], selector_password[1])
    input_pass.clear()
    input_pass.send_keys(testdata['password'])
    input_botton = site.find_element(selector_botton[0], selector_botton[1])
    input_botton.click()

    botton_new_post = site.find_element(selector_botton_new_post[0], selector_botton_new_post[1])
    botton_new_post.click()

    new_post_title = site.find_element(selector_title_new_post[0], selector_title_new_post[1])
    new_post_title.send_keys(testdata['title'])
    new_post_descr = site.find_element(selector_description_new_post[0], selector_description_new_post[1])
    new_post_descr.send_keys(testdata['description'])
    new_post_content = site.find_element(selector_content_new_post[0], selector_content_new_post[1])
    new_post_content.send_keys(testdata['content'])

    botton_save = site.find_element(selector_bottonsave_new_post[0], selector_bottonsave_new_post[1])
    site.driver.implicitly_wait(5)
    botton_save.click()
    site.driver.implicitly_wait(5)
    title_save_post = site.find_element(selector_title_save_post[0], selector_title_save_post[1])


    assert title_save_post.text == testdata['title']



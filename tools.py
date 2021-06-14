'''
@Auth: Xinsheng.guo
@Date: 2021-6-12
'''
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.select import Select
import pandas as pd

def detect_alert(driver, alert_text='已到最后一页！'):
    '''
    检测是否有弹窗弹出，并检测弹窗的内容
    '''
    try:
        alert = driver.switch_to.alert
        if alert.text == alert_text:
            alert.accept()
            return True
        else:
            raise Exception("弹出警告非指定内容！")
    except NoAlertPresentException:
        return False

def get_data(driver, result):
    '''
    获取每一行数据存入dataframe
    '''
    result_table = driver.find_elements_by_class_name('common')[1]
    rows_list = result_table.find_elements_by_class_name('common1')
    for row in rows_list:
        result_text = row.text
        result_text = result_text.split(' ')
        detail_button = row.find_element_by_class_name('button')
        detail = detail_button.get_attribute('onclick')
        detail_text = detail[10:-2].split("','")
        detail_url = detail_text[-1]+detail_text[0]+'.html'
        row_data = pd.DataFrame(data={'ID':[result_text[0]],
                                    'COMPANY':[result_text[1]],
                                    'PRODUCTION':[result_text[2]],
                                    'DETAIL':[detail_url]})
        result = result.append(row_data)
    return result

def select_prod_type(browser, element_id, insurance_type):
    '''
    根据element_id找到下拉框，然后选择insurance_type对应的值
    '''
    select_table = browser.find_element_by_class_name('common')
    pull_down_menu = select_table.find_element_by_id(element_id)
    Select(pull_down_menu).select_by_value(insurance_type)

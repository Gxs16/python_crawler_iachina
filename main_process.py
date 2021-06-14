'''
@Auth: Xinsheng.guo
@Date: 2021-6-12
'''
from selenium import webdriver
from selenium.webdriver.support.select import Select
import pandas as pd
from tools import detect_alert, get_data, select_prod_type
from parameter import target_url, executable_path, option_list, file_save_path

# 创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
browser = webdriver.Edge(executable_path=executable_path)

# 通过浏览器向服务器发送URL请求
browser.get(target_url)

# 找到选择框
select_table = browser.find_element_by_class_name('common')

# 找到选择在售状态的下拉菜单
sale_status = select_table.find_element_by_id('saleStatus')
# 选择产品类型为在售
Select(sale_status).select_by_value('01')

# 依次选择parameter中的产品类型组合
for type_one, type_two, type_three, type_four in option_list:

    file_name = type_one+type_two+type_three+type_four
    # 第1级下拉框
    if type_one:
        select_prod_type(browser, 'prodTypeCode1', type_one)
    # 第2级下拉框
    if type_two:
        select_prod_type(browser, 'prodTypeCode2', type_one+type_two)
    # 第3级下拉框
    if type_three:
        select_prod_type(browser, 'prodTypeCode3', type_one+type_two+type_three)
    # 第4级下拉框
    if type_four:
        select_prod_type(browser, 'prodTypeCode4', type_one+type_two+type_three+type_four)
    total_result = pd.DataFrame(data=None, columns=['ID', 'COMPANY', 'PRODUCTION', 'DETAIL'])
    # 找到查询按钮
    buttons = browser.find_element_by_class_name('button')
    query_button = buttons.find_element_by_id('but1')
    # 点击查询
    query_button.click()
    while not detect_alert(driver=browser):
        total_result = get_data(browser, total_result)
        # 寻找页面底部区域
        bottom_areas = browser.find_elements_by_class_name('common')[-1]
        # 找到‘下一页’按钮
        button_next_page = bottom_areas.find_elements_by_tag_name('td')[3]
        button_next_page.click()
    total_result.to_csv(file_save_path+file_name+'.csv', index=False)

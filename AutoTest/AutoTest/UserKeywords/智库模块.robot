*** Settings ***
Resource          通用模块.robot
Resource          智库模块.robot
Resource          ../UserVariable/智库模块.robot
Library           ../Library/ApiLib/get_kemulist.py
Library           ../Library/ApiLib/get_shoplist.py
Library           ../Library/ApiLib/get_ruleid.py
Library           SeleniumLibrary    timeout=10

*** Keywords ***
店铺列表
    [Arguments]    ${cookie}
    ${response}    common.my request    GET    ${domain}/kmzk/common/shopList/v2?api_name=kmzk_common_shopList_v2&platformIds=    None    ${cookie}
    ${shop_list}    analyse_shoplist    ${response}
    [Return]    ${shop_list}

科目列表
    [Arguments]    ${cookie}    ${categoryType}
    ${response}    common.my request    POST    ${domain}/kmzk/categoryManage/getCategoryList    {"api_name":"kmzk_categoryManage_getCategoryList","queryContent":1,"categoryType":"shop"}    ${cookie}
    ${kemu_list}    get_kemulist    ${response}
    [Return]    ${response}

获取规则
    [Arguments]    ${cookie}
    ${response}    common.my request    GET    ${domain}/kmzk/categoryValuePlan/list/concise?api_name=kmzk_categoryValuePlan_list_concise    None    ${cookie}
    ${ruleid}    get ruleid    ${response}
    [Return]    ${ruleid}

页面登录
    [Arguments]    ${company}    ${account}    ${passwords}
    Open Browser    https://puberp.superboss.cc/login.html    chrome
    Maximize Browser Window
    Input Text    id=login-company    ${company}
    Input Text    id=login-account    ${account}
    Input Text    id=login-password    ${passwords}
    click Button    id=login-btn
    Wait Until Element Is Enabled    xpath=//span[contains(text(),'店铺状态异常确认')]/../span[@class='el-dialog__headerbtnGroup']
    click Element    xpath=//span[contains(text(),'店铺状态异常确认')]/../span[@class='el-dialog__headerbtnGroup']
    title should be    快麦ERP--首页

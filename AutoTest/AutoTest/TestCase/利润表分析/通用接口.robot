*** Settings ***
Suite Setup       登录获取cookie    ${CompanyName}    ${UserName}    ${Password}
Resource          ../../UserKeywords/通用模块.robot
Resource          ../../UserKeywords/智库模块.robot
Resource          ../../UserVariable/智库模块.robot
Library           ../../Library/ApiLib/get_kemulist.py
Library           ../../Library/ApiLib/get_shoplist.py
Library           ../../Library/ApiLib/get_ruleid.py

*** Test Cases ***
获取店铺列表
    [Setup]
    ${response}    common.my request    GET    ${domain}/kmzk/common/shopList/v2?api_name=kmzk_common_shopList_v2&platformIds=    None    ${cookie}
    ${shop_list}    analyse_shoplist    ${response}

获取店铺利润表科目
    ${response}    common.my request    POST    ${domain}/kmzk/categoryManage/getCategoryList    {"api_name":"kmzk_categoryManage_getCategoryList","queryContent":1,"categoryType":"shop"}    ${cookie}
    ${kemu_list}    get_kemulist    ${response}

获取取值方案
    ${response}    common.my request    GET    ${domain}/kmzk/categoryValuePlan/list/concise?api_name=kmzk_categoryValuePlan_list_concise    None    ${cookie}
    ${ruleid}    get ruleid    ${response}

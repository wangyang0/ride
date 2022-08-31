*** Settings ***
Suite Setup       登录获取cookie    ${CompanyName}    ${UserName}    ${Password}
Resource          ../../UserKeywords/智库模块.robot
Resource          ../../UserKeywords/通用模块.robot
Resource          ../../UserVariable/智库模块.robot

*** Test Cases ***
店铺利润表-付款维度
    #获取时间戳
    ${date}    双日时间戳    2022-03-28    2022-04-01
    ${startTime}    Set Variable    ${date[1]}    #获取开始时间
    ${endTime}    Set Variable    ${date[0]}    #获取结束时间
    #获取店铺id
    log    ${cookie}
    ${shoplist}    店铺列表    ${cookie}
    ${shopUniIds}    Evaluate    random.choice(${shoplist})    random
    #获取取值规则
    ${ruleId}    获取规则    ${cookie}
    #请求列表
    ${response}    common.my request    GET    ${domain}/kmzk/profit/report/shop?api_name=kmzk_profit_report_shop&sysStatus=1&startTime=${startTime}&endTime=${endTime}&shopUniIds=${shopUniIds}&timeOrderType=asc&showDimension=0&ruleId=${ruleId}&showSuit=1&refundSumType=0&consignBeforeRate=&consignAfterRate=&isTrusted=true    None    ${cookie}
    log    ${response}
    log    ---开始断言验证---
    ${exp}    common.GetResonseValue    ${response}    suc
    ${true}    Convert to boolean    True
    Should Be Equal As Strings    ${exp}    ${true}

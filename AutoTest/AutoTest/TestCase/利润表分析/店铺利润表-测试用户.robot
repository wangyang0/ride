*** Settings ***
Suite Setup       登录获取cookie    ${CompanyName}    ${UserName}    ${Password}
Library           DateTime
Resource          ../../UserKeywords/智库模块.robot
Resource          ../../UserKeywords/通用模块.robot
Resource          ../../UserVariable/智库模块.robot

*** Test Cases ***
店铺利润表-付款维度-数据检查
    #获取时间戳
    ${date}    双日时间戳    2022-03-28    2022-04-01
    ${startTime}    Set Variable    ${date[1]}    #获取开始时间
    ${endTime}    Set Variable    ${date[0]}    #获取结束时间
    #获取店铺id
    ${shoplist}    店铺列表    ${cookie}
    ${shopUniIds}    Evaluate    random.choice(${shoplist})    random
    #获取取值规则
    ${ruleId}    获取规则    ${cookie}
    #请求列表
    ${response}    common.my request    GET    ${domain}/kmzk/profit/report/shop?api_name=kmzk_profit_report_shop&sysStatus=1&startTime=${startTime}&endTime=${endTime}&shopUniIds=${shopUniIds}&timeOrderType=asc&showDimension=0&ruleId=${ruleId}&showSuit=1&refundSumType=0&consignBeforeRate=&consignAfterRate=&isTrusted=true    None    ${cookie}

销售主题报表-付款
    #获取时间戳
    ${date}    双日时间戳    2022-06-23    2022-07-29
    ${startTime}    Set Variable    ${date[1]}    #获取开始时间
    ${endTime}    Set Variable    ${date[0]}    #获取结束时间
    ${param}    Set Variable    api_name=report_sale_dimensions_finance_getFinanceAmount&pageNo=1&pageSize=50&pageId=1121&queryFlag=shop&startTime=${startTime}&endTime=${endTime}&vipSign=true&sysStatus=pay&sellerFlags=&tradeTypes=&containTagIds=&exceptTagIds=&userIds=15256&warehouseIds=&isAccurate=&itemFlag=0&tradeSysStatus=&scalping=&sysSkuIds=&sysItemIds=&outerIds=&cids=&brandIds=&containTradeOut=true&onlyTradeOut=false&destIds=&sourceIds=&supplyIds=&buyerNicks=&templateIds=&showProcessItemDetail=&showGroupItemDetail=&isOuterIdFuzzy=0&shipper=&queryByCake=&matchFlag=1&virtualFlag=1&showSuit=0&createdStartTime=&createdEndTime=&buyerNick=&classifyIds=&afterSaleTimeType=finish&shouldSort=false&sortField=&sortType
    ${response}    common.other_request    ${domain}/report/sale/dimensions/finance/getFinanceAmount    ${cookies}    ${param}

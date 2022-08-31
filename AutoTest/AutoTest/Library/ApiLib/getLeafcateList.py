# -*- coding: UTF-8 -*-
import json


# 拿到全部科目信息
def get_kemulist(Res):
    kemulist = json.loads(Res)
    kemulist = kemulist["data"]
    kemulist = kemulist["list"]
    kemu_list = []
    for item in kemulist:
        if item["hasChd"] == 1:
            for childlist2 in item["childList"]:
                if childlist2["hasChd"] == 1 and "childList" in childlist2:
                    for childlist3 in childlist2["childList"]:
                        if childlist3["hasChd"] == 1 and "childList" in childlist3:
                            for childlist4 in childlist3["childList"]:
                                if childlist4["hasChd"] == 1 and "childList" in childlist4:
                                    for childlist5 in childlist4["childList"]:
                                        print('最后11111层')
                                elif childlist4["hasChd"] == 0:
                                    categoryname = childlist4["detailId"]
                                    kemu_list.append(categoryname)
                        elif childlist3["hasChd"] == 0:
                            categoryname = childlist3["detailId"]
                            kemu_list.append(categoryname)
                elif childlist2["hasChd"] == 0:
                    categoryname = childlist2["detailId"]
                    kemu_list.append(categoryname)
        elif item["hasChd"] == 0:
            categoryname = item["detailId"]
            kemu_list.append(categoryname)
    print(kemu_list)
    print(len(kemu_list))


if __name__ == "__main__":
    Res = '{"api_name":"fix","clueId":"477806216067584724","data":{"list":[{"budgetDirection":"in",' \
          '"categoryCode":"1","categoryName":"收入: 合计(排除特殊单)","categoryType":"none","childList":[{' \
          '"budgetDirection":"in","categoryCode":"1-0003","categoryName":"退款","categoryType":"none","childList":[{' \
          '"budgetDirection":"in","categoryCode":"zzz-test-01","categoryName":"zzztest01","categoryType":"fix",' \
          '"created":1651822849000,"detailId":"DL_7OrC9S","enableStatus":1,"fillType":"day","hasChd":0,"height":2,' \
          '"id":28136,"index":389,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"1-0003-0005","manualFillType":4,' \
          '"modified":1654683461000,"parentCategoryName":"退款","parentId":7575,"showType":7,"showTypeMap":{"all":1,' \
          '"total":1,"shop":1,"link":1},"sort":5,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"in","categoryCode":"tkzkm","categoryName":"退款子科目固定测试","categoryType":"fix",' \
          '"created":1651905458000,"detailId":"DL_ZKJb8s","enableStatus":1,"fillType":"day","hasChd":0,"height":2,' \
          '"id":28198,"index":392,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"1-0003-0006","manualFillType":4,' \
          '"modified":1654683461000,"parentCategoryName":"退款","parentId":7575,"showType":7,"showTypeMap":{"all":1,' \
          '"total":1,"shop":1,"link":1},"sort":7,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"in","categoryCode":"tkzkm8899","categoryName":"退款子科目灰度5","categoryType":"fix",' \
          '"created":1652354835000,"detailId":"DL_AaCYyq","enableStatus":1,"fillType":"month","hasChd":0,"height":2,' \
          '"id":28569,"index":415,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"1-0003-0008","manualFillType":4,' \
          '"modified":1654683461000,"parentCategoryName":"退款","parentId":7575,"showType":7,"showTypeMap":{"all":1,' \
          '"total":1,"shop":1,"link":1},"sort":8,"symbol":1,"table":"category_manage_info_domain","userId":10438}],' \
          '"created":1612354923000,"detailId":"refund","enableStatus":1,"hasChd":1,"height":1,"id":7575,"index":4,' \
          '"isEdit":"0","isShow":1,"keyId":"1-0003","manualFillType":4,"modified":1654670026000,' \
          '"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,"showType":7,"showTypeMap":{"all":1,"total":1,' \
          '"shop":1,"link":1},"sort":2,"symbol":0,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"in","categoryCode":"321","categoryName":"32132121","categoryType":"fix",' \
          '"created":1628048809000,"detailId":"DL_v3Elet","enableStatus":1,"fillType":"day","hasChd":0,"height":1,' \
          '"id":11694,"index":168,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"1-0011","manualFillType":4,' \
          '"modified":1654670026000,"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,"showType":4,"showTypeMap":{' \
          '"all":1,"total":1,"shop":0,"link":0},"sort":3,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"in","categoryCode":"88888","categoryName":"88888",' \
          '"categoryType":"none","childList":[{"budgetDirection":"in","categoryCode":"dashun",' \
          '"categoryName":"陈永顺日记账收入","categoryType":"fix","context":"日记账联调测试","created":1637822047000,' \
          '"detailId":"DL_krcZP6","enableStatus":1,"fillType":"month","hasChd":0,"height":2,"id":16301,"index":253,' \
          '"isEdit":"1","isFillType":1,"isShow":1,"keyId":"1-0005-0003","manualFillType":2,"modified":1655262145000,' \
          '"parentCategoryName":"88888","parentId":11682,"showType":3,"showTypeMap":{"all":1,"total":0,"shop":1,' \
          '"link":1},"sort":2,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"in","categoryCode":"0011","categoryName":"小青蒿","categoryType":"fix",' \
          '"created":1648709011000,"detailId":"DL_IPWjg7","enableStatus":1,"fillType":"month","hasChd":0,"height":2,' \
          '"id":25531,"index":326,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"1-0005-0007","manualFillType":4,' \
          '"modified":1654679923000,"parentCategoryName":"88888","parentId":11682,"showType":5,"showTypeMap":{' \
          '"all":1,"total":1,"shop":0,"link":1},"sort":4,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"in","categoryCode":"00001","categoryName":"日常收入q",' \
          '"categoryType":"fix","created":1654757768000,"detailId":"DL_SWd8a8","enableStatus":1,"fillType":"day",' \
          '"hasChd":0,"height":2,"id":30426,"index":458,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"1-0005-0015",' \
          '"manualFillType":2,"modified":1655262293000,"parentCategoryName":"88888","parentId":11682,"showType":3,' \
          '"showTypeMap":{"all":1,"total":0,"shop":1,"link":1},"sort":999,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438}],"context":"88888888","created":1627976057000,' \
          '"detailId":"DL_EmakD5","enableStatus":1,"hasChd":1,"height":1,"id":11682,"index":167,"isEdit":"1",' \
          '"isFillType":0,"isShow":1,"keyId":"1-0005","manualFillType":4,"modified":1654670026000,' \
          '"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,"showType":6,"showTypeMap":{"all":1,"total":1,' \
          '"shop":1,"link":0},"sort":4,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"in","categoryCode":"21313123","categoryName":"手工填报","categoryType":"fix",' \
          '"created":1637745138000,"detailId":"DL_6p34AN","enableStatus":1,"fillType":"day","hasChd":0,"height":1,' \
          '"id":16190,"index":251,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"1-0028","manualFillType":4,' \
          '"modified":1654670026000,"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,"showType":7,"showTypeMap":{' \
          '"all":1,"total":1,"shop":1,"link":1},"sort":8,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"in","categoryCode":"213131","categoryName":"手工收入",' \
          '"categoryType":"fix","created":1637745516000,"detailId":"DL_c7ZaJJ","enableStatus":1,"fillType":"day",' \
          '"hasChd":0,"height":1,"id":16191,"index":252,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"1-0029",' \
          '"manualFillType":4,"modified":1654670026000,"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,' \
          '"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":9,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"in","categoryCode":"cs001",' \
          '"categoryName":"测试","categoryType":"fix","context":"测试","created":1639481483000,"detailId":"DL_V1TzPJ",' \
          '"enableStatus":1,"fillType":"week","hasChd":0,"height":1,"id":18026,"index":260,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"1-0031","manualFillType":4,"modified":1654670026000,' \
          '"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,"showType":4,"showTypeMap":{"all":1,"total":1,' \
          '"shop":0,"link":0},"sort":11,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"in","categoryCode":"11233","categoryName":"zjh测试","categoryType":"fix",' \
          '"created":1641892191000,"detailId":"DL_Mbp4RP","enableStatus":1,"fillType":"day","hasChd":0,"height":1,' \
          '"id":20489,"index":285,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"1-0032","manualFillType":4,' \
          '"modified":1654670026000,"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,"showType":7,"showTypeMap":{' \
          '"all":1,"total":1,"shop":1,"link":1},"sort":12,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"in","categoryCode":"166","categoryName":"常山","categoryType":"fix",' \
          '"context":"工资","created":1642833842000,"detailId":"DL_7AHNWN","enableStatus":1,"fillType":"day",' \
          '"hasChd":0,"height":1,"id":21165,"index":291,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"1-0034",' \
          '"manualFillType":4,"modified":1654670026000,"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,' \
          '"showType":6,"showTypeMap":{"all":1,"total":1,"shop":1,"link":0},"sort":14,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"in","categoryCode":"12399",' \
          '"categoryName":"嗯嗯嗯","categoryType":"fix","created":1647005050000,"detailId":"DL_zgKK5f","enableStatus":1,' \
          '"fillType":"day","hasChd":0,"height":1,"id":23941,"index":309,"isEdit":"1","isFillType":1,"isShow":1,' \
          '"keyId":"1-0036","manualFillType":4,"modified":1654670026000,"parentCategoryName":"收入: 合计(排除特殊单)",' \
          '"parentId":7551,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":16,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"in","categoryCode":"857",' \
          '"categoryName":"xw","categoryType":"fix","context":"临时工","created":1647006621000,"detailId":"DL_GZ9PZr",' \
          '"enableStatus":1,"fillType":"day","hasChd":0,"height":1,"id":23945,"index":312,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"1-0037","manualFillType":4,"modified":1654670026000,' \
          '"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,"showType":7,"showTypeMap":{"all":1,"total":1,' \
          '"shop":1,"link":1},"sort":17,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"in","categoryCode":"a1","categoryName":"11","categoryType":"fix",' \
          '"created":1648443527000,"detailId":"DL_PN0cfS","enableStatus":1,"fillType":"week","hasChd":0,"height":1,' \
          '"id":24956,"index":320,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"1-0038","manualFillType":2,' \
          '"modified":1654670026000,"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,"showType":2,"showTypeMap":{' \
          '"all":1,"total":0,"shop":1,"link":0},"sort":18,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"in","categoryCode":"1111111","categoryName":"11111111",' \
          '"categoryType":"fix","created":1649234854000,"detailId":"DL_TginkI","enableStatus":1,"fillType":"day",' \
          '"hasChd":0,"height":1,"id":26170,"index":336,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"1-0040",' \
          '"manualFillType":4,"modified":1654670026000,"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,' \
          '"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":19,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"in","categoryCode":"qyp04",' \
          '"categoryName":"qyptest收入固定","categoryType":"fix","created":1649929587000,"detailId":"DL_T9oJqg",' \
          '"enableStatus":1,"fillType":"day","hasChd":0,"height":1,"id":26570,"index":350,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"1-0042","manualFillType":1,"modified":1654670026000,' \
          '"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,"showType":1,"showTypeMap":{"all":1,"total":0,' \
          '"shop":0,"link":1},"sort":21,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"in","categoryCode":"zyygdcslll","categoryName":"zyy固定测试","categoryType":"fix",' \
          '"created":1650013085000,"detailId":"DL_nPp2I4","enableStatus":1,"hasChd":0,"height":1,"id":26693,' \
          '"index":353,"isEdit":"1","isFillType":0,"isShow":1,"keyId":"1-0043","manualFillType":4,' \
          '"modified":1654670026000,"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,"showType":7,"showTypeMap":{' \
          '"all":1,"total":1,"shop":1,"link":1},"sort":22,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"in","categoryCode":"4a3","categoryName":"1d5","categoryType":"fix",' \
          '"created":1650254836000,"detailId":"DL_cDIQcY","enableStatus":1,"fillType":"day","hasChd":0,"height":1,' \
          '"id":26854,"index":355,"isEdit":"1","isShow":1,"keyId":"1-0045","manualFillType":4,' \
          '"modified":1654670026000,"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,"showType":4,"showTypeMap":{' \
          '"all":1,"total":1,"shop":0,"link":0},"sort":24,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"in","categoryCode":"6h7","categoryName":"h2g","categoryType":"fix",' \
          '"created":1650254891000,"detailId":"DL_pMjlu7","enableStatus":1,"hasChd":1,"height":1,"id":26855,' \
          '"index":356,"isEdit":"1","isShow":1,"keyId":"1-0046","manualFillType":4,"modified":1654670026000,' \
          '"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,"showType":4,"showTypeMap":{"all":1,"total":1,' \
          '"shop":0,"link":0},"sort":25,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"in","categoryCode":"1f1","categoryName":"33d","categoryType":"fix",' \
          '"created":1650265506000,"detailId":"DL_9U3Aoi","enableStatus":1,"fillType":"month","hasChd":0,"height":1,' \
          '"id":26882,"index":358,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"1-0047","manualFillType":4,' \
          '"modified":1654670026000,"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,"showType":4,"showTypeMap":{' \
          '"all":1,"total":1,"shop":0,"link":0},"sort":26,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"in","categoryCode":"r31","categoryName":"13","categoryType":"fix",' \
          '"created":1650265535000,"detailId":"DL_byWRDb","enableStatus":1,"hasChd":1,"height":1,"id":26883,' \
          '"index":359,"isEdit":"1","isFillType":0,"isShow":1,"keyId":"1-0048","manualFillType":4,' \
          '"modified":1654670026000,"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,"showType":4,"showTypeMap":{' \
          '"all":1,"total":1,"shop":0,"link":0},"sort":27,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"in","categoryCode":"1231g","categoryName":"31f","categoryType":"fix",' \
          '"created":1650265939000,"detailId":"DL_EFEZeN","enableStatus":1,"fillType":"day","hasChd":0,"height":1,' \
          '"id":26887,"index":360,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"1-0049","manualFillType":4,' \
          '"modified":1655186080000,"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,"showType":7,"showTypeMap":{' \
          '"all":1,"total":1,"shop":1,"link":1},"sort":28,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"in","categoryCode":"3244","categoryName":"333","categoryType":"fix",' \
          '"created":1651201648000,"detailId":"DL_GBhMAA","enableStatus":1,"fillType":"day","hasChd":0,"height":1,' \
          '"id":27691,"index":385,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"1-0050","manualFillType":2,' \
          '"modified":1654670026000,"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,"showType":3,"showTypeMap":{' \
          '"all":1,"total":0,"shop":1,"link":1},"sort":29,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"in","categoryCode":"23233","categoryName":"23233",' \
          '"categoryType":"fix","created":1651906865000,"detailId":"DL_7vIUDi","enableStatus":1,"fillType":"month",' \
          '"hasChd":0,"height":1,"id":28200,"index":394,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"1-0052",' \
          '"manualFillType":4,"modified":1654670026000,"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,' \
          '"showType":6,"showTypeMap":{"all":1,"total":1,"shop":1,"link":0},"sort":30,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"in","categoryCode":"srzkm",' \
          '"categoryName":"收入的子科目","categoryType":"fix","created":1651908345000,"detailId":"DL_mYBPSg",' \
          '"enableStatus":1,"fillType":"month","hasChd":0,"height":1,"id":28253,"index":397,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"1-0053","manualFillType":2,"modified":1654670026000,' \
          '"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,"showType":3,"showTypeMap":{"all":1,"total":0,' \
          '"shop":1,"link":1},"sort":31,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"in","categoryCode":"test1234","categoryName":"test1234","categoryType":"fix",' \
          '"created":1653444562000,"detailId":"DL_fAih3S","enableStatus":1,"hasChd":1,"height":1,"id":29331,' \
          '"index":437,"isEdit":"1","isFillType":0,"isShow":1,"keyId":"1-0056","manualFillType":4,' \
          '"modified":1654670026000,"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,"showType":4,"showTypeMap":{' \
          '"all":1,"total":1,"shop":0,"link":0},"sort":34,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"in","categoryCode":"000000000000000001",' \
          '"categoryName":"啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊",' \
          '"categoryType":"fix","context":"yyyyyyyyyyyyyyyyyyy","created":1653989176000,"detailId":"DL_Yg2W6v",' \
          '"enableStatus":1,"fillType":"day","hasChd":0,"height":1,"id":29745,"index":451,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"1-0058","manualFillType":4,"modified":1654670026000,' \
          '"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,"showType":7,"showTypeMap":{"all":1,"total":1,' \
          '"shop":1,"link":1},"sort":36,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"in","categoryCode":"3232","categoryName":"323232","categoryType":"fix",' \
          '"created":1654742552000,"detailId":"DL_Ifgr1r","enableStatus":1,"hasChd":0,"height":1,"id":30321,' \
          '"index":457,"isEdit":"1","isFillType":0,"isShow":1,"keyId":"1-0059","manualFillType":4,' \
          '"modified":1654742552000,"parentCategoryName":"收入: 合计(排除特殊单)","parentId":7551,"showType":4,"showTypeMap":{' \
          '"all":1,"total":1,"shop":0,"link":0},"sort":999,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438}],"created":1612354924000,"detailId":"incoming","enableStatus":1,"hasChd":1,"height":0,' \
          '"id":7551,"index":1,"isEdit":"0","isShow":1,"keyId":"1","manualFillType":4,"modified":1612354924000,' \
          '"parentId":0,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":999,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"2",' \
          '"categoryName":"成本: 合计(排除特殊单)","categoryType":"none","childList":[{"budgetDirection":"out",' \
          '"categoryCode":"2-0001","categoryName":"货品成本","categoryType":"none","childList":[{"budgetDirection":"out",' \
          '"categoryCode":"2-0001-0004","categoryName":"手动成本","categoryType":"fix","created":1624439988000,' \
          '"detailId":"DL_dDcXHG","enableStatus":1,"fillType":"month","hasChd":0,"height":2,"id":9406,"index":92,' \
          '"isEdit":"1","isFillType":1,"isShow":1,"keyId":"2-0001-0007","manualFillType":4,"modified":1654670026000,' \
          '"parentCategoryName":"货品成本","parentId":7552,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,' \
          '"link":1},"sort":3,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"xGratuity","categoryName":"商品小费","categoryType":"fix",' \
          '"created":1625795402000,"detailId":"DL_pXkb53","enableStatus":1,"fillType":"day","hasChd":0,"height":2,' \
          '"id":10777,"index":111,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"2-0001-0008","manualFillType":2,' \
          '"modified":1654670026000,"parentCategoryName":"货品成本","parentId":7552,"showType":3,"showTypeMap":{"all":1,' \
          '"total":0,"shop":1,"link":1},"sort":4,"symbol":1,"table":"category_manage_info_domain","userId":10438}],' \
          '"created":1612354923000,"detailId":"item_cost","enableStatus":1,"hasChd":1,"height":1,"id":7552,"index":8,' \
          '"isEdit":"0","isShow":1,"keyId":"2-0001","manualFillType":4,"modified":1654670026000,' \
          '"parentCategoryName":"成本: 合计(排除特殊单)","parentId":7541,"showType":7,"showTypeMap":{"all":1,"total":1,' \
          '"shop":1,"link":1},"sort":1,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"2-0002","categoryName":"退货成本","categoryType":"none","childList":[' \
          '{"budgetDirection":"out","categoryCode":"gfhjdf","categoryName":"运费险","categoryType":"fix",' \
          '"created":1647502351000,"detailId":"DL_oXHLis","enableStatus":1,"hasChd":0,"height":2,"id":24328,' \
          '"index":316,"isEdit":"1","isFillType":0,"isShow":1,"keyId":"2-0002-0004","manualFillType":4,' \
          '"modified":1654670026000,"parentCategoryName":"退货成本","parentId":7576,"showType":7,"showTypeMap":{"all":1,' \
          '"total":1,"shop":1,"link":1},"sort":6,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"1221","categoryName":"测试123","categoryType":"fix",' \
          '"created":1652064949000,"detailId":"DL_G2az2d","enableStatus":1,"hasChd":0,"height":2,"id":28273,' \
          '"index":402,"isEdit":"1","isFillType":0,"isShow":1,"keyId":"2-0002-0007","manualFillType":4,' \
          '"modified":1654670026000,"parentCategoryName":"退货成本","parentId":7576,"showType":7,"showTypeMap":{"all":1,' \
          '"total":1,"shop":1,"link":1},"sort":8,"symbol":0,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"tkcbzkmcs01","categoryName":"退款成本子科目固定测试","categoryType":"fix",' \
          '"created":1652238429000,"detailId":"DL_C0pBoM","enableStatus":1,"fillType":"month","hasChd":0,"height":2,' \
          '"id":28334,"index":409,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"2-0002-0009","manualFillType":2,' \
          '"modified":1654670026000,"parentCategoryName":"退货成本","parentId":7576,"showType":3,"showTypeMap":{"all":1,' \
          '"total":0,"shop":1,"link":1},"sort":10,"symbol":1,"table":"category_manage_info_domain","userId":10438}],' \
          '"created":1612354923000,"detailId":"refund_cost","enableStatus":1,"hasChd":1,"height":1,"id":7576,' \
          '"index":12,"isEdit":"0","isShow":1,"keyId":"2-0002","manualFillType":4,"modified":1654670026000,' \
          '"parentCategoryName":"成本: 合计(排除特殊单)","parentId":7541,"showType":7,"showTypeMap":{"all":1,"total":1,' \
          '"shop":1,"link":1},"sort":2,"symbol":0,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"60012","categoryName":"二狗子费用","categoryType":"fix",' \
          '"context":"test","created":1637464428000,"detailId":"DL_mTMcx5","enableStatus":1,"fillType":"day",' \
          '"hasChd":0,"height":1,"id":15767,"index":249,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"2-0006",' \
          '"manualFillType":4,"modified":1654670026000,"parentCategoryName":"成本: 合计(排除特殊单)","parentId":7541,' \
          '"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":3,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"123234242",' \
          '"categoryName":"123秦莞尔","categoryType":"fix","created":1641385396000,"detailId":"DL_Te9egH",' \
          '"enableStatus":1,"hasChd":1,"height":1,"id":19930,"index":282,"isEdit":"1","isFillType":0,"isShow":1,' \
          '"keyId":"2-0015","manualFillType":4,"modified":1654670026000,"parentCategoryName":"成本: 合计(排除特殊单)",' \
          '"parentId":7541,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":4,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"11111",' \
          '"categoryName":"房租111","categoryType":"fix","created":1645448957000,"detailId":"DL_j9Mu15",' \
          '"enableStatus":1,"fillType":"month","hasChd":0,"height":1,"id":22269,"index":296,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"2-0017","manualFillType":4,"modified":1654670026000,' \
          '"parentCategoryName":"成本: 合计(排除特殊单)","parentId":7541,"showType":4,"showTypeMap":{"all":1,"total":1,' \
          '"shop":0,"link":0},"sort":6,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"qyp05","categoryName":"qyp成本固定","categoryType":"fix",' \
          '"created":1649929607000,"detailId":"DL_xc9vX2","enableStatus":1,"fillType":"day","hasChd":0,"height":1,' \
          '"id":26571,"index":351,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"2-0020","manualFillType":1,' \
          '"modified":1654763192000,"parentCategoryName":"成本: 合计(排除特殊单)","parentId":7541,"showType":1,"showTypeMap":{' \
          '"all":1,"total":0,"shop":0,"link":1},"sort":9,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"000011111","categoryName":"佣金",' \
          '"categoryType":"fix","created":1651891997000,"detailId":"DL_D5ULPp","enableStatus":1,"fillType":"day",' \
          '"hasChd":0,"height":1,"id":28141,"index":390,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"2-0021",' \
          '"manualFillType":4,"modified":1654670026000,"parentCategoryName":"成本: 合计(排除特殊单)","parentId":7541,' \
          '"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":10,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438}],"created":1612354924000,"detailId":"cost",' \
          '"enableStatus":1,"hasChd":1,"height":0,"id":7541,"index":7,"isEdit":"0","isShow":1,"keyId":"2",' \
          '"manualFillType":4,"modified":1612354924000,"parentId":0,"showType":7,"showTypeMap":{"all":1,"total":1,' \
          '"shop":1,"link":1},"sort":999,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"3","categoryName":"费用: 合计","categoryType":"none","childList":[{' \
          '"budgetDirection":"out","categoryCode":"sd_charge","categoryName":"特殊单佣金","categoryType":"none",' \
          '"childList":[{"budgetDirection":"out","categoryCode":"dj","categoryName":"dj","categoryType":"fix",' \
          '"created":1646017688000,"detailId":"DL_FwklFF","enableStatus":1,"fillType":"day","hasChd":0,"height":2,' \
          '"id":22767,"index":306,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0049-0001","manualFillType":2,' \
          '"modified":1654678483000,"parentCategoryName":"特殊单佣金","parentId":7581,"showType":2,"showTypeMap":{"all":1,' \
          '"total":0,"shop":1,"link":0},"sort":1,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"SD1","categoryName":"刷单1","categoryType":"fix",' \
          '"created":1652697035000,"detailId":"DL_y6gA0R","enableStatus":1,"fillType":"day","hasChd":0,"height":2,' \
          '"id":28839,"index":429,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0049-0003","manualFillType":4,' \
          '"modified":1654678483000,"parentCategoryName":"特殊单佣金","parentId":7581,"showType":7,"showTypeMap":{"all":1,' \
          '"total":1,"shop":1,"link":1},"sort":3,"symbol":1,"table":"category_manage_info_domain","userId":10438}],' \
          '"created":1616483582000,"detailId":"sd_charge","enableStatus":1,"hasChd":1,"height":1,"id":7581,' \
          '"index":16,"isEdit":"1","isShow":1,"keyId":"3-0049","manualFillType":4,"modified":1654678483000,' \
          '"parentCategoryName":"费用: 合计","parentId":7540,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,' \
          '"link":1},"sort":1,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"category_change_test8","categoryName":"科目变动测试8",' \
          '"categoryType":"none","childList":[{"budgetDirection":"out","categoryCode":"category_change_2",' \
          '"categoryName":"科目变动测试2","categoryType":"fix","created":1639386667000,"detailId":"DL_MmugV2",' \
          '"enableStatus":1,"fillType":"day","hasChd":0,"height":2,"id":18005,"index":256,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"3-0054-0001","manualFillType":4,"modified":1654678483000,' \
          '"parentCategoryName":"科目变动测试8","parentId":18004,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,' \
          '"link":1},"sort":1,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"category_change_test_4","categoryName":"科目变动测试4",' \
          '"categoryType":"fix","created":1639472611000,"detailId":"DL_FP1A3x","enableStatus":1,"fillType":"day",' \
          '"hasChd":0,"height":2,"id":18017,"index":258,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0055-0002",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"科目变动测试8","parentId":18004,"showType":7,' \
          '"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":2,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out",' \
          '"categoryCode":"category_change_test7","categoryName":"科目变动测试7","categoryType":"fix",' \
          '"created":1639473571000,"detailId":"DL_JpU8bV","enableStatus":1,"fillType":"day","hasChd":0,"height":2,' \
          '"id":18018,"index":259,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0058-0003","manualFillType":4,' \
          '"modified":1654678483000,"parentCategoryName":"科目变动测试8","parentId":18004,"showType":7,"showTypeMap":{' \
          '"all":1,"total":1,"shop":1,"link":1},"sort":3,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"category_change_test_9","categoryName":"科目变动测试9",' \
          '"categoryType":"fix","created":1640057066000,"detailId":"DL_iFIjkl","enableStatus":1,"fillType":"day",' \
          '"hasChd":0,"height":2,"id":18438,"index":271,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0058-0004",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"科目变动测试8","parentId":18004,"showType":4,' \
          '"showTypeMap":{"all":1,"total":1,"shop":0,"link":0},"sort":4,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out",' \
          '"categoryCode":"123123123213","categoryName":"1231231231","categoryType":"fix","created":1646989501000,' \
          '"detailId":"DL_KFrH6t","enableStatus":1,"hasChd":0,"height":2,"id":23937,"index":308,"isEdit":"1",' \
          '"isFillType":0,"isShow":1,"keyId":"3-0058-0005","manualFillType":4,"modified":1654678483000,' \
          '"parentCategoryName":"科目变动测试8","parentId":18004,"showType":6,"showTypeMap":{"all":1,"total":1,"shop":1,' \
          '"link":0},"sort":5,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"00003","categoryName":"日常费用q","categoryType":"fix",' \
          '"created":1654757858000,"detailId":"DL_r0scX3","enableStatus":1,"fillType":"day","hasChd":0,"height":2,' \
          '"id":30427,"index":459,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0058-0006","manualFillType":4,' \
          '"modified":1654757858000,"parentCategoryName":"科目变动测试8","parentId":18004,"showType":7,"showTypeMap":{' \
          '"all":1,"total":1,"shop":1,"link":1},"sort":999,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438}],"created":1639386639000,"detailId":"DL_P32ZUn","enableStatus":1,"hasChd":1,"height":1,' \
          '"id":18004,"index":255,"isEdit":"1","isFillType":0,"isShow":1,"keyId":"3-0058","manualFillType":4,' \
          '"modified":1654678483000,"parentCategoryName":"费用: 合计","parentId":7540,"showType":7,"showTypeMap":{' \
          '"all":1,"total":1,"shop":1,"link":1},"sort":2,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"alipay_charge","categoryName":"支付宝账单费用",' \
          '"categoryType":"none","childList":[{"budgetDirection":"out","categoryCode":"zfb_foodie_channel",' \
          '"categoryName":"吃货频道","categoryType":"fix","created":1628674348000,"detailId":"DL_ql7k2r",' \
          '"enableStatus":1,"fillType":"day","hasChd":0,"height":2,"id":12038,"index":181,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"3-0005-0036","manualFillType":4,"modified":1654678483000,' \
          '"parentCategoryName":"支付宝账单费用","parentId":7535,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,' \
          '"link":1},"sort":33,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"zhuanzhangfuwufei","categoryName":"转账服务费","categoryType":"none",' \
          '"childList":[{"budgetDirection":"out","categoryCode":"sdfj","categoryName":"啥打法上","categoryType":"fix",' \
          '"created":1645586699000,"detailId":"DL_4JmnDI","enableStatus":1,"fillType":"week","hasChd":0,"height":3,' \
          '"id":22442,"index":298,"isEdit":"1","isFillType":0,"isShow":1,"keyId":"3-0005-0052-0001",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"转账服务费","parentId":22441,"showType":7,' \
          '"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":1,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"sdhfj",' \
          '"categoryName":"啥打法上的","categoryType":"fix","created":1645586732000,"detailId":"DL_X5DfDX",' \
          '"enableStatus":1,"hasChd":1,"height":3,"id":22443,"index":299,"isEdit":"1","isFillType":0,"isShow":1,' \
          '"keyId":"3-0005-0052-0002","manualFillType":4,"modified":1654678483000,"parentCategoryName":"转账服务费",' \
          '"parentId":22441,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":2,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438}],"created":1645586684000,"detailId":"DL_ix0s4j",' \
          '"enableStatus":1,"hasChd":1,"height":2,"id":22441,"index":297,"isEdit":"1","isShow":1,' \
          '"keyId":"3-0005-0052","manualFillType":4,"modified":1654678483000,"parentCategoryName":"支付宝账单费用",' \
          '"parentId":7535,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":48,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"ztcznjh",' \
          '"categoryName":"直通车智能计划","categoryType":"fix","created":1647330710000,"detailId":"DL_wM18S8",' \
          '"enableStatus":1,"fillType":"day","hasChd":0,"height":2,"id":24039,"index":313,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"3-0005-0053","manualFillType":1,"modified":1654678483000,' \
          '"parentCategoryName":"支付宝账单费用","parentId":7535,"showType":1,"showTypeMap":{"all":1,"total":0,"shop":0,' \
          '"link":1},"sort":49,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"gzc_user_defined_test","categoryName":"葛志城测试1",' \
          '"categoryType":"fix","created":1652060489000,"detailId":"DL_o2FydQ","enableStatus":1,"hasChd":0,' \
          '"height":2,"id":28270,"index":401,"isEdit":"1","isFillType":0,"isShow":1,"keyId":"3-0005-0054",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"支付宝账单费用","parentId":7535,"showType":6,' \
          '"showTypeMap":{"all":1,"total":1,"shop":1,"link":0},"sort":50,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438}],"created":1616482982000,"detailId":"alipay_charge",' \
          '"enableStatus":1,"hasChd":1,"height":1,"id":7535,"index":34,"isEdit":"1","isShow":1,"keyId":"3-0005",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"费用: 合计","parentId":7540,"showType":7,' \
          '"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":4,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"0001",' \
          '"categoryName":"人员工资","categoryType":"fix","created":1622367300000,"detailId":"DL_kniA8v",' \
          '"enableStatus":1,"fillType":"day","hasChd":0,"height":1,"id":7954,"index":78,"isEdit":"1","isFillType":1,' \
          '"isShow":1,"keyId":"3-0014","manualFillType":1,"modified":1654678483000,"parentCategoryName":"费用: 合计",' \
          '"parentId":7540,"showType":1,"showTypeMap":{"all":1,"total":0,"shop":0,"link":1},"sort":10,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"0009",' \
          '"categoryName":"荞麦工资","categoryType":"fix","created":1623403520000,"detailId":"DL_JcJMnF",' \
          '"enableStatus":1,"fillType":"month","hasChd":0,"height":1,"id":8810,"index":79,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"3-0015","manualFillType":4,"modified":1654678483000,' \
          '"parentCategoryName":"费用: 合计","parentId":7540,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,' \
          '"link":1},"sort":11,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"test","categoryName":"测试科目","categoryType":"fix",' \
          '"created":1624267385000,"detailId":"DL_UHmzt8","enableStatus":1,"fillType":"day","hasChd":0,"height":1,' \
          '"id":9223,"index":80,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0051","manualFillType":4,' \
          '"modified":1654678483000,"parentCategoryName":"费用: 合计","parentId":7540,"showType":7,"showTypeMap":{' \
          '"all":1,"total":1,"shop":1,"link":1},"sort":12,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"test0","categoryName":"测试科目2",' \
          '"categoryType":"none","childList":[{"budgetDirection":"out","categoryCode":"44","categoryName":"44",' \
          '"categoryType":"fix","context":"1","created":1624282650000,"detailId":"DL_9Pa8q8","enableStatus":1,' \
          '"fillType":"","hasChd":1,"height":2,"id":9226,"index":81,"isEdit":"1","isFillType":0,"isShow":1,' \
          '"keyId":"3-0018-0006","manualFillType":4,"modified":1654678483000,"parentCategoryName":"测试科目2",' \
          '"parentId":9224,"showType":4,"showTypeMap":{"all":1,"total":1,"shop":0,"link":0},"sort":1,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"test01",' \
          '"categoryName":"科目01","categoryType":"fix","created":1624268692000,"detailId":"DL_eiHNPe",' \
          '"enableStatus":1,"fillType":"day","hasChd":0,"height":2,"id":9225,"index":82,"isEdit":"1","isFillType":1,' \
          '"isShow":1,"keyId":"3-0018-0009","manualFillType":4,"modified":1654678483000,"parentCategoryName":"测试科目2",' \
          '"parentId":9224,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":2,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438}],"created":1624268640000,"detailId":"DL_Uvx7Gr",' \
          '"enableStatus":1,"hasChd":1,"height":1,"id":9224,"index":81,"isEdit":"1","isFillType":0,"isShow":1,' \
          '"keyId":"3-0018","manualFillType":4,"modified":1654678483000,"parentCategoryName":"费用: 合计",' \
          '"parentId":7540,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":13,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"0090",' \
          '"categoryName":"仓库工资","categoryType":"fix","created":1624355414000,"detailId":"DL_DjL5OL",' \
          '"enableStatus":1,"fillType":"day","hasChd":0,"height":1,"id":9326,"index":83,"isEdit":"1","isFillType":1,' \
          '"isShow":1,"keyId":"3-0023","manualFillType":4,"modified":1654678483000,"parentCategoryName":"费用: 合计",' \
          '"parentId":7540,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":14,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out",' \
          '"categoryCode":"fxg_bill_charge","categoryName":"放心购账单费用","categoryType":"none","childList":[{' \
          '"budgetDirection":"out","categoryCode":"fxg_ddtk","categoryName":"订单退款","categoryType":"fix",' \
          '"created":1624417581000,"detailId":"DL_ERwxZn","enableStatus":1,"fillType":"day","hasChd":0,"height":2,' \
          '"id":9330,"index":87,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0024-0003","manualFillType":4,' \
          '"modified":1654678483000,"parentCategoryName":"放心购账单费用","parentId":9327,"showType":7,"showTypeMap":{' \
          '"all":1,"total":1,"shop":1,"link":1},"sort":3,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"fxg_ptfwf","categoryName":"平台服务费",' \
          '"categoryType":"fix","created":1624417764000,"detailId":"DL_mZxEDu","enableStatus":1,"fillType":"day",' \
          '"hasChd":0,"height":2,"id":9331,"index":88,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0024-0004",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"放心购账单费用","parentId":9327,"showType":7,' \
          '"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":4,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"fxg_yj",' \
          '"categoryName":"佣金2","categoryType":"fix","created":1624417789000,"detailId":"DL_8KA0E9","enableStatus":1,' \
          '"fillType":"day","hasChd":0,"height":2,"id":9332,"index":89,"isEdit":"1","isFillType":1,"isShow":1,' \
          '"keyId":"3-0024-0013","manualFillType":4,"modified":1654678483000,"parentCategoryName":"放心购账单费用",' \
          '"parentId":9327,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":5,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"fxg_hhxx",' \
          '"categoryName":"好好学习分成","categoryType":"fix","created":1624417813000,"detailId":"DL_0Y6AOm",' \
          '"enableStatus":1,"fillType":"week","hasChd":0,"height":2,"id":9333,"index":90,"isEdit":"1","isFillType":1,' \
          '"isShow":1,"keyId":"3-0024-0006","manualFillType":4,"modified":1654678483000,' \
          '"parentCategoryName":"放心购账单费用","parentId":9327,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,' \
          '"link":1},"sort":6,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"fxg_zsfw","categoryName":"招商服务费","categoryType":"fix",' \
          '"created":1624417840000,"detailId":"DL_x4VOsD","enableStatus":1,"fillType":"day","hasChd":0,"height":2,' \
          '"id":9334,"index":91,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0024-0007","manualFillType":4,' \
          '"modified":1654678483000,"parentCategoryName":"放心购账单费用","parentId":9327,"showType":7,"showTypeMap":{' \
          '"all":1,"total":1,"shop":1,"link":1},"sort":7,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438}],"created":1624417411000,"detailId":"DL_sY0A7V","enableStatus":1,"hasChd":1,"height":1,' \
          '"id":9327,"index":84,"isEdit":"1","isFillType":0,"isShow":1,"keyId":"3-0024","manualFillType":4,' \
          '"modified":1654678483000,"parentCategoryName":"费用: 合计","parentId":7540,"showType":7,"showTypeMap":{' \
          '"all":1,"total":1,"shop":1,"link":1},"sort":15,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"test_share","categoryName":"测试分摊",' \
          '"categoryType":"none","childList":[{"budgetDirection":"out","categoryCode":"test01_01",' \
          '"categoryName":"测试商品-不分摊","categoryType":"fix","created":1625556589000,"detailId":"DL_xl2Rex",' \
          '"enableStatus":1,"fillType":"day","hasChd":0,"height":2,"id":10582,"index":96,"isEdit":"1","isFillType":1,' \
          '"isShow":1,"keyId":"3-0029-0032","manualFillType":4,"modified":1654678483000,"parentCategoryName":"测试分摊",' \
          '"parentId":10581,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":1,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"test01_02",' \
          '"categoryName":"测试商品-按销售额","categoryType":"fix","created":1625556623000,"detailId":"DL_JlNRcT",' \
          '"enableStatus":1,"fillType":"day","hasChd":0,"height":2,"id":10583,"index":97,"isEdit":"1","isFillType":1,' \
          '"isShow":1,"keyId":"3-0029-0033","manualFillType":4,"modified":1654678483000,"parentCategoryName":"测试分摊",' \
          '"parentId":10581,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":2,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"test01_03",' \
          '"categoryName":"测试商品-按销售数量","categoryType":"fix","created":1625556663000,"detailId":"DL_Ms0nUT",' \
          '"enableStatus":1,"fillType":"day","hasChd":0,"height":2,"id":10584,"index":98,"isEdit":"1","isFillType":1,' \
          '"isShow":1,"keyId":"3-0029-0034","manualFillType":4,"modified":1654678483000,"parentCategoryName":"测试分摊",' \
          '"parentId":10581,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":3,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"test01_04",' \
          '"categoryName":"测试商品-按销售成本","categoryType":"fix","created":1625556696000,"detailId":"DL_mJmnV8",' \
          '"enableStatus":1,"fillType":"day","hasChd":0,"height":2,"id":10585,"index":99,"isEdit":"1","isFillType":1,' \
          '"isShow":1,"keyId":"3-0029-0035","manualFillType":4,"modified":1654678483000,"parentCategoryName":"测试分摊",' \
          '"parentId":10581,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":4,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"test02_01",' \
          '"categoryName":"测试订单-按订单数-订单商品销售额","categoryType":"fix","created":1625558449000,"detailId":"DL_ZPCMiD",' \
          '"enableStatus":1,"fillType":"day","hasChd":0,"height":2,"id":10592,"index":100,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"3-0029-0036","manualFillType":4,"modified":1654678483000,' \
          '"parentCategoryName":"测试分摊","parentId":10581,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,' \
          '"link":1},"sort":5,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"test02_02","categoryName":"测试订单-按订单数-订单商品销售数",' \
          '"categoryType":"fix","created":1625558514000,"detailId":"DL_iMqAvj","enableStatus":1,"fillType":"day",' \
          '"hasChd":0,"height":2,"id":10593,"index":101,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0029-0037",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"测试分摊","parentId":10581,"showType":7,' \
          '"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":6,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"test02_03",' \
          '"categoryName":"测试订单-按订单数-订单商品成本","categoryType":"fix","created":1625558592000,"detailId":"DL_MMLMop",' \
          '"enableStatus":1,"fillType":"day","hasChd":0,"height":2,"id":10594,"index":102,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"3-0029-0038","manualFillType":4,"modified":1654678483000,' \
          '"parentCategoryName":"测试分摊","parentId":10581,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,' \
          '"link":1},"sort":7,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"test03_01","categoryName":"测试订单-按订单销售额-订单商品销售额",' \
          '"categoryType":"fix","created":1625558628000,"detailId":"DL_Oh158d","enableStatus":1,"fillType":"day",' \
          '"hasChd":0,"height":2,"id":10595,"index":103,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0029-0039",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"测试分摊","parentId":10581,"showType":7,' \
          '"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":8,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"test03_02",' \
          '"categoryName":"测试订单-按订单销售额-订单商品销售数","categoryType":"fix","created":1625560442000,"detailId":"DL_7rzOZ1",' \
          '"enableStatus":1,"fillType":"day","hasChd":0,"height":2,"id":10597,"index":104,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"3-0029-0040","manualFillType":4,"modified":1654678483000,' \
          '"parentCategoryName":"测试分摊","parentId":10581,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,' \
          '"link":1},"sort":9,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"test03_03","categoryName":"测试订单-按订单销售额-订单商品成本",' \
          '"categoryType":"fix","created":1625560478000,"detailId":"DL_pN7h3t","enableStatus":1,"fillType":"day",' \
          '"hasChd":0,"height":2,"id":10598,"index":105,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0029-0041",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"测试分摊","parentId":10581,"showType":7,' \
          '"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":10,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"test00x",' \
          '"categoryName":"测试订单-按订单销售额-订单商品销售额2","categoryType":"fix","created":1626661049000,"detailId":"DL_rxjkoj",' \
          '"enableStatus":1,"fillType":"day","hasChd":0,"height":2,"id":11126,"index":119,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"3-0029-0042","manualFillType":4,"modified":1654678483000,' \
          '"parentCategoryName":"测试分摊","parentId":10581,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,' \
          '"link":1},"sort":11,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"zyykmcs111101","categoryName":"zyy测试_按费用发生时间_不分摊",' \
          '"categoryType":"fix","created":1636623697000,"detailId":"DL_nHWF2j","enableStatus":1,"fillType":"day",' \
          '"hasChd":0,"height":2,"id":15274,"index":221,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0029-0095",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"测试分摊","parentId":10581,"showType":7,' \
          '"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":22,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out",' \
          '"categoryCode":"zyykmcs111102","categoryName":"zyy测试_按费用发生时间_按商品_按销售额占比","categoryType":"fix",' \
          '"created":1636625539000,"detailId":"DL_E2q0Vh","enableStatus":1,"fillType":"day","hasChd":0,"height":2,' \
          '"id":15275,"index":222,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0029-0116","manualFillType":2,' \
          '"modified":1654678483000,"parentCategoryName":"测试分摊","parentId":10581,"showType":3,"showTypeMap":{"all":1,' \
          '"total":0,"shop":1,"link":1},"sort":23,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"zyybmcs003","categoryName":"zyy测试_按费用发生时间_按商品_按销售数量占比",' \
          '"categoryType":"fix","created":1636629701000,"detailId":"DL_KpFy6N","enableStatus":1,"fillType":"day",' \
          '"hasChd":0,"height":2,"id":15276,"index":223,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0029-0101",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"测试分摊","parentId":10581,"showType":7,' \
          '"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":24,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out",' \
          '"categoryCode":"zyybmcs001","categoryName":"zyy测试_按费用发生时间_按商品_按销售成本占比","categoryType":"fix",' \
          '"created":1636629867000,"detailId":"DL_QbIXHh","enableStatus":1,"fillType":"day","hasChd":0,"height":2,' \
          '"id":15277,"index":224,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0029-0083","manualFillType":2,' \
          '"modified":1654678483000,"parentCategoryName":"测试分摊","parentId":10581,"showType":3,"showTypeMap":{"all":1,' \
          '"total":0,"shop":1,"link":1},"sort":25,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"zyybmcs111105",' \
          '"categoryName":"zyy测试_按费用发生时间_先订单后商品_按订单销售额占比_按订单商品销售额占比","categoryType":"fix","created":1636630897000,' \
          '"detailId":"DL_uZrCQ1","enableStatus":1,"fillType":"day","hasChd":0,"height":2,"id":15278,"index":225,' \
          '"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0029-0094","manualFillType":2,"modified":1654678483000,' \
          '"parentCategoryName":"测试分摊","parentId":10581,"showType":3,"showTypeMap":{"all":1,"total":0,"shop":1,' \
          '"link":1},"sort":26,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"zyybmcs111106",' \
          '"categoryName":"zyy测试_按费用发生时间_先订单后商品_按订单销售额占比_按订单商品数量占比","categoryType":"fix","created":1636631187000,' \
          '"detailId":"DL_oUgqav","enableStatus":1,"fillType":"day","hasChd":0,"height":2,"id":15279,"index":226,' \
          '"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0029-0085","manualFillType":2,"modified":1654678483000,' \
          '"parentCategoryName":"测试分摊","parentId":10581,"showType":3,"showTypeMap":{"all":1,"total":0,"shop":1,' \
          '"link":1},"sort":27,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"zyybmcs111107",' \
          '"categoryName":"zyy测试_按费用发生时间_先订单后商品_按订单销售额占比_按订单商品成本占比","categoryType":"fix","created":1636631224000,' \
          '"detailId":"DL_taeSzs","enableStatus":1,"fillType":"day","hasChd":0,"height":2,"id":15280,"index":227,' \
          '"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0029-0086","manualFillType":2,"modified":1654678483000,' \
          '"parentCategoryName":"测试分摊","parentId":10581,"showType":3,"showTypeMap":{"all":1,"total":0,"shop":1,' \
          '"link":1},"sort":28,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"zyybmcs111108",' \
          '"categoryName":"zyy测试_按费用发生时间_先订单后商品_按订单数占比_按订单商品销售额占比","categoryType":"fix","created":1636631510000,' \
          '"detailId":"DL_5sxFqh","enableStatus":1,"fillType":"week","hasChd":0,"height":2,"id":15281,"index":228,' \
          '"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0029-0087","manualFillType":2,"modified":1654678483000,' \
          '"parentCategoryName":"测试分摊","parentId":10581,"showType":3,"showTypeMap":{"all":1,"total":0,"shop":1,' \
          '"link":1},"sort":29,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"zyybmcs111109",' \
          '"categoryName":"zyy测试_按费用发生时间_先订单后商品_按订单数占比_按订单商品数量占比","categoryType":"fix","created":1636631547000,' \
          '"detailId":"DL_Y6xarg","enableStatus":1,"fillType":"day","hasChd":0,"height":2,"id":15282,"index":229,' \
          '"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0029-0088","manualFillType":2,"modified":1654678483000,' \
          '"parentCategoryName":"测试分摊","parentId":10581,"showType":3,"showTypeMap":{"all":1,"total":0,"shop":1,' \
          '"link":1},"sort":30,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"zyybmcs111110",' \
          '"categoryName":"zyy测试_按费用发生时间_先订单后商品_按订单数占比_按订单商品成本占比","categoryType":"fix","created":1636631586000,' \
          '"detailId":"DL_XkTNbU","enableStatus":1,"fillType":"day","hasChd":0,"height":2,"id":15283,"index":230,' \
          '"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0029-0089","manualFillType":2,"modified":1654678483000,' \
          '"parentCategoryName":"测试分摊","parentId":10581,"showType":3,"showTypeMap":{"all":1,"total":0,"shop":1,' \
          '"link":1},"sort":31,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"zyybmcs111111","categoryName":"zyy测试_跟随订单_按商品",' \
          '"categoryType":"fix","created":1636631610000,"detailId":"DL_D6dAFy","enableStatus":1,"fillType":"day",' \
          '"hasChd":0,"height":2,"id":15284,"index":231,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0029-0090",' \
          '"manualFillType":2,"modified":1654678483000,"parentCategoryName":"测试分摊","parentId":10581,"showType":3,' \
          '"showTypeMap":{"all":1,"total":0,"shop":1,"link":1},"sort":32,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out",' \
          '"categoryCode":"zyybmcs111112","categoryName":"zyy测试_跟随订单_先订单后商品","categoryType":"fix",' \
          '"created":1636631657000,"detailId":"DL_5wdIHB","enableStatus":1,"fillType":"day","hasChd":0,"height":2,' \
          '"id":15285,"index":232,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0029-0091","manualFillType":1,' \
          '"modified":1654678483000,"parentCategoryName":"测试分摊","parentId":10581,"showType":1,"showTypeMap":{"all":1,' \
          '"total":0,"shop":0,"link":1},"sort":33,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"test-lxs","categoryName":"lxs-分摊","categoryType":"fix",' \
          '"context":"wq","created":1636976008000,"detailId":"DL_qdLWEN","enableStatus":1,"fillType":"day",' \
          '"hasChd":0,"height":2,"id":15345,"index":236,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0029-0131",' \
          '"manualFillType":1,"modified":1654678483000,"parentCategoryName":"测试分摊","parentId":10581,"showType":1,' \
          '"showTypeMap":{"all":1,"total":0,"shop":0,"link":1},"sort":34,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438}],"created":1625556479000,"detailId":"DL_vdKyPJ",' \
          '"enableStatus":1,"hasChd":1,"height":1,"id":10581,"index":95,"isEdit":"1","isFillType":0,"isShow":1,' \
          '"keyId":"3-0029","manualFillType":4,"modified":1654678483000,"parentCategoryName":"费用: 合计",' \
          '"parentId":7540,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":16,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"sfdfdaaaa",' \
          '"categoryName":"手工填报-aa","categoryType":"fix","created":1625746367000,"detailId":"DL_VA3FRJ",' \
          '"enableStatus":1,"fillType":"day","hasChd":0,"height":1,"id":10776,"index":110,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"3-0033","manualFillType":2,"modified":1654678483000,' \
          '"parentCategoryName":"费用: 合计","parentId":7540,"showType":3,"showTypeMap":{"all":1,"total":0,"shop":1,' \
          '"link":1},"sort":18,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"CommonFillShare","categoryName":"公共费用分摊测试","categoryType":"none",' \
          '"childList":[{"budgetDirection":"out","categoryCode":"CommonFillShare_fixValue_month",' \
          '"categoryName":"公共费用分摊测试-固定金额-月","categoryType":"fix","created":1627607534000,"detailId":"DL_Rdw6MQ",' \
          '"enableStatus":1,"fillType":"month","hasChd":0,"height":2,"id":11575,"index":134,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"3-0038-0002","manualFillType":4,"modified":1654678483000,' \
          '"parentCategoryName":"公共费用分摊测试","parentId":11573,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,' \
          '"link":1},"sort":1,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"CommonFillShare_fixValue_week","categoryName":"公共费用分摊测试-固定金额-周",' \
          '"categoryType":"fix","created":1627607594000,"detailId":"DL_o1R27z","enableStatus":1,"fillType":"week",' \
          '"hasChd":0,"height":2,"id":11576,"index":135,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0038-0003",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"公共费用分摊测试","parentId":11573,"showType":7,' \
          '"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":2,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out",' \
          '"categoryCode":"CommonFillShare_fixValue_day","categoryName":"公共费用分摊测试-固定金额-日","categoryType":"fix",' \
          '"created":1627607616000,"detailId":"DL_zDA3AD","enableStatus":1,"fillType":"day","hasChd":0,"height":2,' \
          '"id":11577,"index":136,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0038-0004","manualFillType":4,' \
          '"modified":1654678483000,"parentCategoryName":"公共费用分摊测试","parentId":11573,"showType":7,"showTypeMap":{' \
          '"all":1,"total":1,"shop":1,"link":1},"sort":3,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"CommonFillShare_fixProp_month",' \
          '"categoryName":"公共费用分摊测试-固定比例-月","categoryType":"fix","created":1627607663000,"detailId":"DL_srXio7",' \
          '"enableStatus":1,"fillType":"month","hasChd":0,"height":2,"id":11578,"index":137,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"3-0038-0005","manualFillType":4,"modified":1654678483000,' \
          '"parentCategoryName":"公共费用分摊测试","parentId":11573,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,' \
          '"link":1},"sort":4,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"CommonFillShare_fixProp_week","categoryName":"公共费用分摊测试-固定比例-周",' \
          '"categoryType":"fix","created":1627607685000,"detailId":"DL_nhZ064","enableStatus":1,"fillType":"week",' \
          '"hasChd":0,"height":2,"id":11579,"index":138,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0038-0006",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"公共费用分摊测试","parentId":11573,"showType":7,' \
          '"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":5,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out",' \
          '"categoryCode":"CommonFillShare_fixProp_day","categoryName":"公共费用分摊测试-固定比例-日","categoryType":"fix",' \
          '"created":1627607733000,"detailId":"DL_CIWor9","enableStatus":1,"fillType":"day","hasChd":0,"height":2,' \
          '"id":11580,"index":139,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0038-0007","manualFillType":4,' \
          '"modified":1654678483000,"parentCategoryName":"公共费用分摊测试","parentId":11573,"showType":7,"showTypeMap":{' \
          '"all":1,"total":1,"shop":1,"link":1},"sort":6,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"CommonFillShare_orderNum_month",' \
          '"categoryName":"公共费用分摊测试-订单数量-月","categoryType":"fix","created":1627607864000,"detailId":"DL_J1IAic",' \
          '"enableStatus":1,"fillType":"month","hasChd":0,"height":2,"id":11581,"index":140,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"3-0038-0008","manualFillType":4,"modified":1654678483000,' \
          '"parentCategoryName":"公共费用分摊测试","parentId":11573,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,' \
          '"link":1},"sort":7,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"CommonFillShare_orderNum_week","categoryName":"公共费用分摊测试-订单数量-周",' \
          '"categoryType":"fix","created":1627607890000,"detailId":"DL_syLO2x","enableStatus":1,"fillType":"week",' \
          '"hasChd":0,"height":2,"id":11582,"index":141,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0038-0009",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"公共费用分摊测试","parentId":11573,"showType":7,' \
          '"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":8,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out",' \
          '"categoryCode":"CommonFillShare_orderNum_day","categoryName":"公共费用分摊测试-订单数量-日","categoryType":"fix",' \
          '"created":1627607920000,"detailId":"DL_aeaIvw","enableStatus":1,"fillType":"day","hasChd":0,"height":2,' \
          '"id":11583,"index":142,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0038-0010","manualFillType":4,' \
          '"modified":1654678483000,"parentCategoryName":"公共费用分摊测试","parentId":11573,"showType":7,"showTypeMap":{' \
          '"all":1,"total":1,"shop":1,"link":1},"sort":9,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"CommonFillShare_orderCost_month",' \
          '"categoryName":"公共费用分摊测试-订单成本-月","categoryType":"fix","created":1627608030000,"detailId":"DL_rK8dPg",' \
          '"enableStatus":1,"fillType":"month","hasChd":0,"height":2,"id":11587,"index":146,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"3-0038-0022","manualFillType":4,"modified":1654678483000,' \
          '"parentCategoryName":"公共费用分摊测试","parentId":11573,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,' \
          '"link":1},"sort":10,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"CommonFillShare_orderCost_week","categoryName":"公共费用分摊测试-订单成本-周",' \
          '"categoryType":"fix","created":1627608064000,"detailId":"DL_YJK9IW","enableStatus":1,"fillType":"week",' \
          '"hasChd":0,"height":2,"id":11588,"index":147,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0038-0023",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"公共费用分摊测试","parentId":11573,"showType":7,' \
          '"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":11,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out",' \
          '"categoryCode":"CommonFillShare_orderCost_day","categoryName":"公共费用分摊测试-订单成本-日","categoryType":"fix",' \
          '"created":1627608085000,"detailId":"DL_hQNU2O","enableStatus":1,"fillType":"day","hasChd":0,"height":2,' \
          '"id":11589,"index":148,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0038-0016","manualFillType":4,' \
          '"modified":1654678483000,"parentCategoryName":"公共费用分摊测试","parentId":11573,"showType":7,"showTypeMap":{' \
          '"all":1,"total":1,"shop":1,"link":1},"sort":12,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"CommonFillShare_orderFee_month",' \
          '"categoryName":"公共费用分摊测试-订单金额-月","categoryType":"fix","created":1627872679000,"detailId":"DL_TM8sTI",' \
          '"enableStatus":1,"fillType":"month","hasChd":0,"height":2,"id":11626,"index":163,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"3-0038-0026","manualFillType":4,"modified":1654678483000,' \
          '"parentCategoryName":"公共费用分摊测试","parentId":11573,"showType":6,"showTypeMap":{"all":1,"total":1,"shop":1,' \
          '"link":0},"sort":13,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"CommonFillShare_orderFee_week","categoryName":"公共费用分摊测试-订单金额-周",' \
          '"categoryType":"fix","created":1627872705000,"detailId":"DL_0TtXCr","enableStatus":1,"fillType":"day",' \
          '"hasChd":0,"height":2,"id":11627,"index":164,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0038-0018",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"公共费用分摊测试","parentId":11573,"showType":7,' \
          '"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":14,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out",' \
          '"categoryCode":"CommonFillShare_orderFee_day","categoryName":"公共费用分摊测试-订单金额-日","categoryType":"fix",' \
          '"created":1627872731000,"detailId":"DL_b7RhSJ","enableStatus":1,"fillType":"day","hasChd":0,"height":2,' \
          '"id":11628,"index":165,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0038-0021","manualFillType":4,' \
          '"modified":1654678483000,"parentCategoryName":"公共费用分摊测试","parentId":11573,"showType":7,"showTypeMap":{' \
          '"all":1,"total":1,"shop":1,"link":1},"sort":15,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"test333","categoryName":"公共费用分摊测试-固定金额-周-跨月",' \
          '"categoryType":"fix","created":1630394070000,"detailId":"DL_cDaX4L","enableStatus":1,"fillType":"week",' \
          '"hasChd":0,"height":2,"id":12565,"index":195,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0038-0027",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"公共费用分摊测试","parentId":11573,"showType":7,' \
          '"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":16,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out",' \
          '"categoryCode":"CommonFillShare_joinValue_month","categoryName":"公共费用分摊测试-参与值-月","categoryType":"fix",' \
          '"created":1631631646000,"detailId":"DL_p4vhkH","enableStatus":1,"fillType":"month","hasChd":0,"height":2,' \
          '"id":13542,"index":204,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0038-0029","manualFillType":4,' \
          '"modified":1654678483000,"parentCategoryName":"公共费用分摊测试","parentId":11573,"showType":7,"showTypeMap":{' \
          '"all":1,"total":1,"shop":1,"link":1},"sort":17,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"CommonFillShare_joinValue_week",' \
          '"categoryName":"公共费用分摊测试-参与值-周","categoryType":"fix","created":1631631699000,"detailId":"DL_wPl2X7",' \
          '"enableStatus":1,"fillType":"week","hasChd":0,"height":2,"id":13543,"index":205,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"3-0038-0030","manualFillType":4,"modified":1654678483000,' \
          '"parentCategoryName":"公共费用分摊测试","parentId":11573,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,' \
          '"link":1},"sort":18,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"CommonFillShare_joinValue_day","categoryName":"公共费用分摊测试-参与值-日",' \
          '"categoryType":"fix","created":1631631740000,"detailId":"DL_tGFX34","enableStatus":1,"fillType":"day",' \
          '"hasChd":0,"height":2,"id":13544,"index":206,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0038-0032",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"公共费用分摊测试","parentId":11573,"showType":7,' \
          '"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":19,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438}],"created":1627607402000,"detailId":"DL_SyInry",' \
          '"enableStatus":1,"hasChd":1,"height":1,"id":11573,"index":132,"isEdit":"1","isFillType":0,"isShow":1,' \
          '"keyId":"3-0038","manualFillType":4,"modified":1654678483000,"parentCategoryName":"费用: 合计",' \
          '"parentId":7540,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":22,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out",' \
          '"categoryCode":"23423324423","categoryName":"水电费","categoryType":"fix","created":1628144516000,' \
          '"detailId":"DL_mKCI1i","enableStatus":1,"fillType":"month","hasChd":0,"height":1,"id":11709,"index":170,' \
          '"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0042","manualFillType":4,"modified":1654678483000,' \
          '"parentCategoryName":"费用: 合计","parentId":7540,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,' \
          '"link":1},"sort":26,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"shuifei","categoryName":"水电煤气费","categoryType":"fix",' \
          '"created":1628566523000,"detailId":"DL_2nQshe","enableStatus":1,"fillType":"month","hasChd":0,"height":1,' \
          '"id":11865,"index":172,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0043","manualFillType":4,' \
          '"modified":1654678483000,"parentCategoryName":"费用: 合计","parentId":7540,"showType":4,"showTypeMap":{' \
          '"all":1,"total":1,"shop":0,"link":0},"sort":27,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"20210810","categoryName":"水电网络费",' \
          '"categoryType":"fix","context":"11","created":1628566587000,"detailId":"DL_vSol5n","enableStatus":1,' \
          '"fillType":"month","hasChd":0,"height":1,"id":11866,"index":173,"isEdit":"1","isFillType":1,"isShow":1,' \
          '"keyId":"3-0044","manualFillType":4,"modified":1654678483000,"parentCategoryName":"费用: 合计",' \
          '"parentId":7540,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":28,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out",' \
          '"categoryCode":"test_kuaidi","categoryName":"快递费用（手工）","categoryType":"none","childList":[{' \
          '"budgetDirection":"out","categoryCode":"0000999","categoryName":"材料费","categoryType":"fix",' \
          '"created":1628752719000,"detailId":"DL_QmvFNE","enableStatus":1,"fillType":"day","hasChd":0,"height":2,' \
          '"id":12054,"index":194,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0047-0011","manualFillType":1,' \
          '"modified":1654678483000,"parentCategoryName":"快递费用（手工）","parentId":11933,"showType":1,"showTypeMap":{' \
          '"all":1,"total":0,"shop":0,"link":1},"sort":3,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438}],"created":1628589817000,"detailId":"DL_ETxEVp","enableStatus":1,"hasChd":1,"height":1,' \
          '"id":11933,"index":178,"isEdit":"1","isShow":1,"keyId":"3-0047","manualFillType":4,' \
          '"modified":1654678483000,"parentCategoryName":"费用: 合计","parentId":7540,"showType":7,"showTypeMap":{' \
          '"all":1,"total":1,"shop":1,"link":1},"sort":30,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"kmzyy001001","categoryName":"固定费用测试zyy",' \
          '"categoryType":"fix","created":1636599203000,"detailId":"DL_5fujvm","enableStatus":1,"fillType":"day",' \
          '"hasChd":0,"height":1,"id":15272,"index":220,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0052",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"费用: 合计","parentId":7540,"showType":7,' \
          '"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":32,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"0003",' \
          '"categoryName":"00031","categoryType":"fix","created":1654678076000,"detailId":"DL_qAj6jK",' \
          '"enableStatus":1,"fillType":"month","hasChd":0,"height":1,"id":30269,"index":455,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"3-0119","manualFillType":2,"modified":1654678483000,' \
          '"parentCategoryName":"费用: 合计","parentId":7540,"showType":2,"showTypeMap":{"all":1,"total":0,"shop":1,' \
          '"link":0},"sort":33,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"13232","categoryName":"ZS","categoryType":"fix",' \
          '"created":1637741687000,"detailId":"DL_9UnRX1","enableStatus":1,"fillType":"day","hasChd":0,"height":1,' \
          '"id":16188,"index":250,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0053","manualFillType":4,' \
          '"modified":1654678483000,"parentCategoryName":"费用: 合计","parentId":7540,"showType":7,"showTypeMap":{' \
          '"all":1,"total":1,"shop":1,"link":1},"sort":34,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"00088999","categoryName":"员工工资",' \
          '"categoryType":"fix","created":1639467489000,"detailId":"DL_rRtHru","enableStatus":1,"fillType":"month",' \
          '"hasChd":0,"height":1,"id":18011,"index":257,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0056",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"费用: 合计","parentId":7540,"showType":7,' \
          '"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":35,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"fkm001",' \
          '"categoryName":"父科目","categoryType":"none","childList":[{"budgetDirection":"out",' \
          '"categoryCode":"link_detail_fill_1","categoryName":"链接手工填报测试1","categoryType":"fix",' \
          '"created":1639570307000,"detailId":"DL_Y9EVc9","enableStatus":1,"fillType":"day","hasChd":0,"height":2,' \
          '"id":18096,"index":266,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0062-0008","manualFillType":1,' \
          '"modified":1654678483000,"parentCategoryName":"父科目","parentId":18081,"showType":1,"showTypeMap":{"all":1,' \
          '"total":0,"shop":0,"link":1},"sort":2,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"1234567","categoryName":"淘宝天猫","categoryType":"fix",' \
          '"created":1647005176000,"detailId":"DL_WIYbzX","enableStatus":1,"fillType":"day","hasChd":0,"height":2,' \
          '"id":23943,"index":311,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0062-0009","manualFillType":2,' \
          '"modified":1654678483000,"parentCategoryName":"父科目","parentId":18081,"showType":3,"showTypeMap":{"all":1,' \
          '"total":0,"shop":1,"link":1},"sort":3,"symbol":1,"table":"category_manage_info_domain","userId":10438}],' \
          '"context":"2121","created":1639552599000,"detailId":"DL_dNjVQo","enableStatus":1,"hasChd":1,"height":1,' \
          '"id":18081,"index":264,"isEdit":"1","isShow":1,"keyId":"3-0062","manualFillType":2,' \
          '"modified":1654678483000,"parentCategoryName":"费用: 合计","parentId":7540,"showType":3,"showTypeMap":{' \
          '"all":1,"total":0,"shop":1,"link":1},"sort":37,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"link_ceshi","categoryName":"链接手工填报",' \
          '"categoryType":"fix","context":"111","created":1639618501000,"detailId":"DL_1ajEuf","enableStatus":1,' \
          '"fillType":"day","hasChd":0,"height":1,"id":18101,"index":267,"isEdit":"1","isFillType":1,"isShow":1,' \
          '"keyId":"3-0073","manualFillType":2,"modified":1654678483000,"parentCategoryName":"费用: 合计",' \
          '"parentId":7540,"showType":3,"showTypeMap":{"all":1,"total":0,"shop":1,"link":1},"sort":38,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out",' \
          '"categoryCode":"zyykm23232","categoryName":"zyy公共费用分摊测试固定","categoryType":"fix","created":1640071184000,' \
          '"detailId":"DL_BSWrk3","enableStatus":1,"fillType":"day","hasChd":0,"height":1,"id":18551,"index":273,' \
          '"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0065","manualFillType":4,"modified":1654678483000,' \
          '"parentCategoryName":"费用: 合计","parentId":7540,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,' \
          '"link":1},"sort":39,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"zyybm009988","categoryName":"zyy科目测试固定","categoryType":"fix",' \
          '"created":1641807640000,"detailId":"DL_b4p0NY","enableStatus":1,"fillType":"day","hasChd":0,"height":1,' \
          '"id":20461,"index":283,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0075","manualFillType":4,' \
          '"modified":1654678483000,"parentCategoryName":"费用: 合计","parentId":7540,"showType":7,"showTypeMap":{' \
          '"all":1,"total":1,"shop":1,"link":1},"sort":42,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"zyybmcs0099922","categoryName":"zyy测试01",' \
          '"categoryType":"fix","created":1641866847000,"detailId":"DL_xUyEef","enableStatus":1,"fillType":"month",' \
          '"hasChd":0,"height":1,"id":20466,"index":284,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0076",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"费用: 合计","parentId":7540,"showType":7,' \
          '"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":43,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"kdfytb",' \
          '"categoryName":"快递费用填报","categoryType":"fix","created":1645596207000,"detailId":"DL_Ms1DUF",' \
          '"enableStatus":1,"fillType":"day","hasChd":0,"height":1,"id":22447,"index":300,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"3-0080","manualFillType":4,"modified":1654678483000,' \
          '"parentCategoryName":"费用: 合计","parentId":7540,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,' \
          '"link":1},"sort":47,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"fzfy","categoryName":"房租费用","categoryType":"fix",' \
          '"created":1645670035000,"detailId":"DL_ubqvu7","enableStatus":1,"fillType":"month","hasChd":0,"height":1,' \
          '"id":22455,"index":303,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0082","manualFillType":4,' \
          '"modified":1654678483000,"parentCategoryName":"费用: 合计","parentId":7540,"showType":7,"showTypeMap":{' \
          '"all":1,"total":1,"shop":1,"link":1},"sort":49,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"ccc","categoryName":"cccc","categoryType":"fix",' \
          '"created":1647396107000,"detailId":"DL_bnoq9R","enableStatus":1,"fillType":"day","hasChd":0,"height":1,' \
          '"id":24055,"index":314,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0085","manualFillType":4,' \
          '"modified":1654678483000,"parentCategoryName":"费用: 合计","parentId":7540,"showType":5,"showTypeMap":{' \
          '"all":1,"total":1,"shop":0,"link":1},"sort":52,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"000001","categoryName":"yy测试科目1",' \
          '"categoryType":"fix","context":"这是我的测试啊","created":1648796267000,"detailId":"DL_qK2ALT","enableStatus":1,' \
          '"fillType":"day","hasChd":0,"height":1,"id":25766,"index":329,"isEdit":"1","isFillType":1,"isShow":1,' \
          '"keyId":"3-0091","manualFillType":2,"modified":1654678483000,"parentCategoryName":"费用: 合计",' \
          '"parentId":7540,"showType":2,"showTypeMap":{"all":1,"total":0,"shop":1,"link":0},"sort":56,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"000002",' \
          '"categoryName":"yy测试科目2","categoryType":"none","childList":[{"budgetDirection":"out",' \
          '"categoryCode":"000002-1","categoryName":"yy测试科目2-1","categoryType":"fix","context":"测试啊",' \
          '"created":1648796557000,"detailId":"DL_kbs5Gd","enableStatus":1,"hasChd":0,"height":2,"id":25768,' \
          '"index":331,"isEdit":"1","isFillType":0,"isShow":1,"keyId":"3-0092-0001","manualFillType":2,' \
          '"modified":1654678483000,"parentCategoryName":"yy测试科目2","parentId":25767,"showType":2,"showTypeMap":{' \
          '"all":1,"total":0,"shop":1,"link":0},"sort":1,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"000001-2","categoryName":"yy科目测试变动科目",' \
          '"categoryType":"none","childList":[{"budgetDirection":"out","categoryCode":"0304","categoryName":"lzc测试",' \
          '"categoryType":"fix","created":1649232923000,"detailId":"DL_H49Ym5","enableStatus":1,"fillType":"week",' \
          '"hasChd":0,"height":3,"id":26166,"index":334,"isEdit":"1","isFillType":1,"isShow":1,' \
          '"keyId":"3-0092-0002-0002","manualFillType":4,"modified":1654678483000,"parentCategoryName":"yy科目测试变动科目",' \
          '"parentId":25771,"showType":4,"showTypeMap":{"all":1,"total":1,"shop":0,"link":0},"sort":2,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438}],"context":"二级科目","created":1648797472000,' \
          '"detailId":"DL_H0YbQz","enableStatus":1,"hasChd":1,"height":2,"id":25771,"index":332,"isEdit":"1",' \
          '"isShow":1,"keyId":"3-0092-0002","manualFillType":2,"modified":1654678483000,' \
          '"parentCategoryName":"yy测试科目2","parentId":25767,"showType":2,"showTypeMap":{"all":1,"total":0,"shop":1,' \
          '"link":0},"sort":2,"symbol":1,"table":"category_manage_info_domain","userId":10438}],"context":"这是我的测试啊",' \
          '"created":1648796400000,"detailId":"DL_PfzeLr","enableStatus":1,"hasChd":1,"height":1,"id":25767,' \
          '"index":330,"isEdit":"1","isFillType":0,"isShow":1,"keyId":"3-0092","manualFillType":2,' \
          '"modified":1654678483000,"parentCategoryName":"费用: 合计","parentId":7540,"showType":2,"showTypeMap":{' \
          '"all":1,"total":0,"shop":1,"link":0},"sort":57,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"qyp06","categoryName":"qyptest费用固定",' \
          '"categoryType":"fix","created":1649929632000,"detailId":"DL_lcku6g","enableStatus":1,"fillType":"day",' \
          '"hasChd":0,"height":1,"id":26572,"index":352,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0094",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"费用: 合计","parentId":7540,"showType":6,' \
          '"showTypeMap":{"all":1,"total":1,"shop":1,"link":0},"sort":59,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"10-1",' \
          '"categoryName":"服务费","categoryType":"none","childList":[{"budgetDirection":"out","categoryCode":"1110-1",' \
          '"categoryName":"工资A","categoryType":"fix","created":1650287066000,"detailId":"DL_lYngjU","enableStatus":1,' \
          '"fillType":"month","hasChd":0,"height":2,"id":26914,"index":367,"isEdit":"1","isFillType":1,"isShow":1,' \
          '"keyId":"3-0099-0002","manualFillType":4,"modified":1654678483000,"parentCategoryName":"服务费",' \
          '"parentId":26912,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":2,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"2340",' \
          '"categoryName":"租金","categoryType":"fix","created":1650288085000,"detailId":"DL_qMdtVw","enableStatus":1,' \
          '"fillType":"month","hasChd":0,"height":2,"id":26915,"index":368,"isEdit":"1","isFillType":1,"isShow":1,' \
          '"keyId":"3-0099-0003","manualFillType":4,"modified":1654678483000,"parentCategoryName":"服务费",' \
          '"parentId":26912,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":3,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"q001",' \
          '"categoryName":"服务服务反反复复烦烦烦烦烦烦烦烦烦烦烦烦烦烦烦反反复复烦烦烦烦烦烦烦烦烦烦烦烦烦烦烦反反复复烦烦烦烦烦烦烦烦烦烦烦烦烦烦烦","categoryType":"fix",' \
          '"context":"111111111111","created":1654499485000,"detailId":"DL_cZ8nxw","enableStatus":1,"fillType":"day",' \
          '"hasChd":0,"height":2,"id":30057,"index":454,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0099-0004",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"服务费","parentId":26912,"showType":6,' \
          '"showTypeMap":{"all":1,"total":1,"shop":1,"link":0},"sort":4,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438}],"created":1650285967000,"detailId":"DL_lZJsNF",' \
          '"enableStatus":1,"hasChd":1,"height":1,"id":26912,"index":365,"isEdit":"1","isFillType":0,"isShow":1,' \
          '"keyId":"3-0099","manualFillType":4,"modified":1654678483000,"parentCategoryName":"费用: 合计",' \
          '"parentId":7540,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":64,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"zyygd",' \
          '"categoryName":"zyy固定无子线上环境","categoryType":"fix","created":1650508894000,"detailId":"DL_mGnGLd",' \
          '"enableStatus":1,"fillType":"month","hasChd":0,"height":1,"id":27049,"index":375,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"3-0100","manualFillType":4,"modified":1654678483000,' \
          '"parentCategoryName":"费用: 合计","parentId":7540,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,' \
          '"link":1},"sort":65,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"zyygdyz","categoryName":"zyy固定有子线上环境","categoryType":"fix",' \
          '"created":1650508992000,"detailId":"DL_A9QYpJ","enableStatus":1,"hasChd":1,"height":1,"id":27050,' \
          '"index":376,"isEdit":"1","isFillType":0,"isShow":1,"keyId":"3-0101","manualFillType":4,' \
          '"modified":1654678483000,"parentCategoryName":"费用: 合计","parentId":7540,"showType":4,"showTypeMap":{' \
          '"all":1,"total":1,"shop":0,"link":0},"sort":66,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"zyyfybd001","categoryName":"zyy固有001",' \
          '"categoryType":"fix","created":1650547690000,"detailId":"DL_kNUQzJ","enableStatus":1,"hasChd":1,' \
          '"height":1,"id":27156,"index":379,"isEdit":"1","isFillType":0,"isShow":1,"keyId":"3-0104",' \
          '"manualFillType":2,"modified":1654678483000,"parentCategoryName":"费用: 合计","parentId":7540,"showType":2,' \
          '"showTypeMap":{"all":1,"total":0,"shop":1,"link":0},"sort":69,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out",' \
          '"categoryCode":"zyykmcs123","categoryName":"zyy固定777770909","categoryType":"fix","created":1651028723000,' \
          '"detailId":"DL_elddIm","enableStatus":1,"fillType":"day","hasChd":0,"height":1,"id":27536,"index":384,' \
          '"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0107","manualFillType":4,"modified":1654678483000,' \
          '"parentCategoryName":"费用: 合计","parentId":7540,"showType":6,"showTypeMap":{"all":1,"total":1,"shop":1,' \
          '"link":0},"sort":72,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"fyzkmcs","categoryName":"费用子科目测试","categoryType":"fix",' \
          '"created":1651909880000,"detailId":"DL_LaBlc3","enableStatus":1,"fillType":"month","hasChd":0,"height":1,' \
          '"id":28255,"index":399,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0108","manualFillType":2,' \
          '"modified":1654678483000,"parentCategoryName":"费用: 合计","parentId":7540,"showType":3,"showTypeMap":{' \
          '"all":1,"total":0,"shop":1,"link":1},"sort":73,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"rggz","categoryName":"工资","categoryType":"fix",' \
          '"created":1652323801000,"detailId":"DL_zvqMVT","enableStatus":1,"fillType":"month","hasChd":0,"height":1,' \
          '"id":28394,"index":414,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0109","manualFillType":4,' \
          '"modified":1654678483000,"parentCategoryName":"费用: 合计","parentId":7540,"showType":7,"showTypeMap":{' \
          '"all":1,"total":1,"shop":1,"link":1},"sort":74,"symbol":1,"table":"category_manage_info_domain",' \
          '"userId":10438},{"budgetDirection":"out","categoryCode":"6601","categoryName":"66测试公摊",' \
          '"categoryType":"fix","created":1652857917000,"detailId":"DL_ENZUPP","enableStatus":1,"fillType":"day",' \
          '"hasChd":0,"height":1,"id":28961,"index":430,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0110",' \
          '"manualFillType":4,"modified":1654678483000,"parentCategoryName":"费用: 合计","parentId":7540,"showType":7,' \
          '"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":75,"symbol":1,' \
          '"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"test001",' \
          '"categoryName":"test001","categoryType":"fix","created":1653964520000,"detailId":"DL_DJ8yJq",' \
          '"enableStatus":1,"fillType":"month","hasChd":0,"height":1,"id":29625,"index":448,"isEdit":"1",' \
          '"isFillType":1,"isShow":1,"keyId":"3-0115","manualFillType":4,"modified":1654678483000,' \
          '"parentCategoryName":"费用: 合计","parentId":7540,"showType":4,"showTypeMap":{"all":1,"total":1,"shop":0,' \
          '"link":0},"sort":80,"symbol":1,"table":"category_manage_info_domain","userId":10438},' \
          '{"budgetDirection":"out","categoryCode":"S000000000001",' \
          '"categoryName' \
          '":"支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出支出","categoryType":"fix","context":"按月","created":1654051304000,"detailId":"DL_NQHCdL","enableStatus":1,"fillType":"day","hasChd":0,"height":1,"id":29796,"index":452,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0117","manualFillType":4,"modified":1654765582000,"parentCategoryName":"费用: 合计","parentId":7540,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":82,"symbol":1,"table":"category_manage_info_domain","userId":10438},{"budgetDirection":"out","categoryCode":"zyykmcsll","categoryName":"zyy科目名称新","categoryType":"fix","created":1654830098000,"detailId":"DL_Zk0iJ5","enableStatus":1,"fillType":"month","hasChd":0,"height":1,"id":30487,"index":461,"isEdit":"1","isFillType":1,"isShow":1,"keyId":"3-0120","manualFillType":4,"modified":1654830098000,"parentCategoryName":"费用: 合计","parentId":7540,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":999,"symbol":1,"table":"category_manage_info_domain","userId":10438}],"created":1612354924000,"detailId":"charge","enableStatus":1,"hasChd":1,"height":0,"id":7540,"index":15,"isEdit":"0","isShow":1,"keyId":"3","manualFillType":4,"modified":1612354924000,"parentId":0,"showType":7,"showTypeMap":{"all":1,"total":1,"shop":1,"link":1},"sort":999,"symbol":1,"table":"category_manage_info_domain","userId":10438}]},"qTime":42,"result":1,"suc":true} '
    get_kemulist(Res)

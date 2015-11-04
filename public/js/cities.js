var cities=[["110100","市辖区","110000"],["110200","县","110000"],["120100","市辖区","120000"],["120200","县","120000"],["130100","石家庄市","130000"],["130200","唐山市","130000"],["130300","秦皇岛市","130000"],["130400","邯郸市","130000"],["130500","邢台市","130000"],["130600","保定市","130000"],["130700","张家口市","130000"],["130800","承德市","130000"],["130900","沧州市","130000"],["131000","廊坊市","130000"],["131100","衡水市","130000"],["140100","太原市","140000"],["140200","大同市","140000"],["140300","阳泉市","140000"],["140400","长治市","140000"],["140500","晋城市","140000"],["140600","朔州市","140000"],["140700","晋中市","140000"],["140800","运城市","140000"],["140900","忻州市","140000"],["141000","临汾市","140000"],["141100","吕梁市","140000"],["150100","呼和浩特市","150000"],["150200","包头市","150000"],["150300","乌海市","150000"],["150400","赤峰市","150000"],["150500","通辽市","150000"],["150600","鄂尔多斯市","150000"],["150700","呼伦贝尔市","150000"],["150800","巴彦淖尔市","150000"],["150900","乌兰察布市","150000"],["152200","兴安盟","150000"],["152500","锡林郭勒盟","150000"],["152900","阿拉善盟","150000"],["210100","沈阳市","210000"],["210200","大连市","210000"],["210300","鞍山市","210000"],["210400","抚顺市","210000"],["210500","本溪市","210000"],["210600","丹东市","210000"],["210700","锦州市","210000"],["210800","营口市","210000"],["210900","阜新市","210000"],["211000","辽阳市","210000"],["211100","盘锦市","210000"],["211200","铁岭市","210000"],["211300","朝阳市","210000"],["211400","葫芦岛市","210000"],["220100","长春市","220000"],["220200","吉林市","220000"],["220300","四平市","220000"],["220400","辽源市","220000"],["220500","通化市","220000"],["220600","白山市","220000"],["220700","松原市","220000"],["220800","白城市","220000"],["222400","延边朝鲜族自治州","220000"],["230100","哈尔滨市","230000"],["230200","齐齐哈尔市","230000"],["230300","鸡西市","230000"],["230400","鹤岗市","230000"],["230500","双鸭山市","230000"],["230600","大庆市","230000"],["230700","伊春市","230000"],["230800","佳木斯市","230000"],["230900","七台河市","230000"],["231000","牡丹江市","230000"],["231100","黑河市","230000"],["231200","绥化市","230000"],["232700","大兴安岭地区","230000"],["310100","市辖区","310000"],["310200","县","310000"],["320100","南京市","320000"],["320200","无锡市","320000"],["320300","徐州市","320000"],["320400","常州市","320000"],["320500","苏州市","320000"],["320600","南通市","320000"],["320700","连云港市","320000"],["320800","淮安市","320000"],["320900","盐城市","320000"],["321000","扬州市","320000"],["321100","镇江市","320000"],["321200","泰州市","320000"],["321300","宿迁市","320000"],["330100","杭州市","330000"],["330200","宁波市","330000"],["330300","温州市","330000"],["330400","嘉兴市","330000"],["330500","湖州市","330000"],["330600","绍兴市","330000"],["330700","金华市","330000"],["330800","衢州市","330000"],["330900","舟山市","330000"],["331000","台州市","330000"],["331100","丽水市","330000"],["340100","合肥市","340000"],["340200","芜湖市","340000"],["340300","蚌埠市","340000"],["340400","淮南市","340000"],["340500","马鞍山市","340000"],["340600","淮北市","340000"],["340700","铜陵市","340000"],["340800","安庆市","340000"],["341000","黄山市","340000"],["341100","滁州市","340000"],["341200","阜阳市","340000"],["341300","宿州市","340000"],["341400","巢湖市","340000"],["341500","六安市","340000"],["341600","亳州市","340000"],["341700","池州市","340000"],["341800","宣城市","340000"],["350100","福州市","350000"],["350200","厦门市","350000"],["350300","莆田市","350000"],["350400","三明市","350000"],["350500","泉州市","350000"],["350600","漳州市","350000"],["350700","南平市","350000"],["350800","龙岩市","350000"],["350900","宁德市","350000"],["360100","南昌市","360000"],["360200","景德镇市","360000"],["360300","萍乡市","360000"],["360400","九江市","360000"],["360500","新余市","360000"],["360600","鹰潭市","360000"],["360700","赣州市","360000"],["360800","吉安市","360000"],["360900","宜春市","360000"],["361000","抚州市","360000"],["361100","上饶市","360000"],["370100","济南市","370000"],["370200","青岛市","370000"],["370300","淄博市","370000"],["370400","枣庄市","370000"],["370500","东营市","370000"],["370600","烟台市","370000"],["370700","潍坊市","370000"],["370800","济宁市","370000"],["370900","泰安市","370000"],["371000","威海市","370000"],["371100","日照市","370000"],["371200","莱芜市","370000"],["371300","临沂市","370000"],["371400","德州市","370000"],["371500","聊城市","370000"],["371600","滨州市","370000"],["371700","荷泽市","370000"],["410100","郑州市","410000"],["410200","开封市","410000"],["410300","洛阳市","410000"],["410400","平顶山市","410000"],["410500","安阳市","410000"],["410600","鹤壁市","410000"],["410700","新乡市","410000"],["410800","焦作市","410000"],["410900","濮阳市","410000"],["411000","许昌市","410000"],["411100","漯河市","410000"],["411200","三门峡市","410000"],["411300","南阳市","410000"],["411400","商丘市","410000"],["411500","信阳市","410000"],["411600","周口市","410000"],["411700","驻马店市","410000"],["420100","武汉市","420000"],["420200","黄石市","420000"],["420300","十堰市","420000"],["420500","宜昌市","420000"],["420600","襄樊市","420000"],["420700","鄂州市","420000"],["420800","荆门市","420000"],["420900","孝感市","420000"],["421000","荆州市","420000"],["421100","黄冈市","420000"],["421200","咸宁市","420000"],["421300","随州市","420000"],["422800","恩施土家族苗族自治州","420000"],["429000","省直辖行政单位","420000"],["430100","长沙市","430000"],["430200","株洲市","430000"],["430300","湘潭市","430000"],["430400","衡阳市","430000"],["430500","邵阳市","430000"],["430600","岳阳市","430000"],["430700","常德市","430000"],["430800","张家界市","430000"],["430900","益阳市","430000"],["431000","郴州市","430000"],["431100","永州市","430000"],["431200","怀化市","430000"],["431300","娄底市","430000"],["433100","湘西土家族苗族自治州","430000"],["440100","广州市","440000"],["440200","韶关市","440000"],["440300","深圳市","440000"],["440400","珠海市","440000"],["440500","汕头市","440000"],["440600","佛山市","440000"],["440700","江门市","440000"],["440800","湛江市","440000"],["440900","茂名市","440000"],["441200","肇庆市","440000"],["441300","惠州市","440000"],["441400","梅州市","440000"],["441500","汕尾市","440000"],["441600","河源市","440000"],["441700","阳江市","440000"],["441800","清远市","440000"],["441900","东莞市","440000"],["442000","中山市","440000"],["445100","潮州市","440000"],["445200","揭阳市","440000"],["445300","云浮市","440000"],["450100","南宁市","450000"],["450200","柳州市","450000"],["450300","桂林市","450000"],["450400","梧州市","450000"],["450500","北海市","450000"],["450600","防城港市","450000"],["450700","钦州市","450000"],["450800","贵港市","450000"],["450900","玉林市","450000"],["451000","百色市","450000"],["451100","贺州市","450000"],["451200","河池市","450000"],["451300","来宾市","450000"],["451400","崇左市","450000"],["460100","海口市","460000"],["460200","三亚市","460000"],["469000","省直辖县级行政单位","460000"],["500100","市辖区","500000"],["500200","县","500000"],["500300","市","500000"],["510100","成都市","510000"],["510300","自贡市","510000"],["510400","攀枝花市","510000"],["510500","泸州市","510000"],["510600","德阳市","510000"],["510700","绵阳市","510000"],["510800","广元市","510000"],["510900","遂宁市","510000"],["511000","内江市","510000"],["511100","乐山市","510000"],["511300","南充市","510000"],["511400","眉山市","510000"],["511500","宜宾市","510000"],["511600","广安市","510000"],["511700","达州市","510000"],["511800","雅安市","510000"],["511900","巴中市","510000"],["512000","资阳市","510000"],["513200","阿坝藏族羌族自治州","510000"],["513300","甘孜藏族自治州","510000"],["513400","凉山彝族自治州","510000"],["520100","贵阳市","520000"],["520200","六盘水市","520000"],["520300","遵义市","520000"],["520400","安顺市","520000"],["522200","铜仁地区","520000"],["522300","黔西南布依族苗族自治州","520000"],["522400","毕节地区","520000"],["522600","黔东南苗族侗族自治州","520000"],["522700","黔南布依族苗族自治州","520000"],["530100","昆明市","530000"],["530300","曲靖市","530000"],["530400","玉溪市","530000"],["530500","保山市","530000"],["530600","昭通市","530000"],["530700","丽江市","530000"],["530800","思茅市","530000"],["530900","临沧市","530000"],["532300","楚雄彝族自治州","530000"],["532500","红河哈尼族彝族自治州","530000"],["532600","文山壮族苗族自治州","530000"],["532800","西双版纳傣族自治州","530000"],["532900","大理白族自治州","530000"],["533100","德宏傣族景颇族自治州","530000"],["533300","怒江傈僳族自治州","530000"],["533400","迪庆藏族自治州","530000"],["540100","拉萨市","540000"],["542100","昌都地区","540000"],["542200","山南地区","540000"],["542300","日喀则地区","540000"],["542400","那曲地区","540000"],["542500","阿里地区","540000"],["542600","林芝地区","540000"],["610100","西安市","610000"],["610200","铜川市","610000"],["610300","宝鸡市","610000"],["610400","咸阳市","610000"],["610500","渭南市","610000"],["610600","延安市","610000"],["610700","汉中市","610000"],["610800","榆林市","610000"],["610900","安康市","610000"],["611000","商洛市","610000"],["620100","兰州市","620000"],["620200","嘉峪关市","620000"],["620300","金昌市","620000"],["620400","白银市","620000"],["620500","天水市","620000"],["620600","武威市","620000"],["620700","张掖市","620000"],["620800","平凉市","620000"],["620900","酒泉市","620000"],["621000","庆阳市","620000"],["621100","定西市","620000"],["621200","陇南市","620000"],["622900","临夏回族自治州","620000"],["623000","甘南藏族自治州","620000"],["630100","西宁市","630000"],["632100","海东地区","630000"],["632200","海北藏族自治州","630000"],["632300","黄南藏族自治州","630000"],["632500","海南藏族自治州","630000"],["632600","果洛藏族自治州","630000"],["632700","玉树藏族自治州","630000"],["632800","海西蒙古族藏族自治州","630000"],["640100","银川市","640000"],["640200","石嘴山市","640000"],["640300","吴忠市","640000"],["640400","固原市","640000"],["640500","中卫市","640000"],["650100","乌鲁木齐市","650000"],["650200","克拉玛依市","650000"],["652100","吐鲁番地区","650000"],["652200","哈密地区","650000"],["652300","昌吉回族自治州","650000"],["652700","博尔塔拉蒙古自治州","650000"],["652800","巴音郭楞蒙古自治州","650000"],["652900","阿克苏地区","650000"],["653000","克孜勒苏柯尔克孜自治州","650000"],["653100","喀什地区","650000"],["653200","和田地区","650000"],["654000","伊犁哈萨克自治州","650000"],["654200","塔城地区","650000"],["654300","阿勒泰地区","650000"],["659000","省直辖行政单位","650000"]];
.. 36ban documentation master file, created by
   sphinx-quickstart on Fri May  9 11:17:18 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===========================
Data Base Design
===========================

公共表
===========

后台管理人员表
----------------------------------------

======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)	      N                         主键id
work_id                 bigint(20)        N                         工作用的QQ号
customer                bigint(20)        N                         工作人员的inc.eking 的user_id
======================  ================  ============  ========    ================================================================================================



申请主体：applicants
-------------------------------
======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)	      N                         主键id
user_id                 varchar(40)       N                         用户id
name                    varchar(200)      N             ""          名称
app_type                varchar(20)       N             ""          主体类型：person:个人 com:公司
region                  varchar(20)       N             ""          区域：cn（中国大陆）、hk（中国香港）、tw（中国台湾）、mo（中国澳门）、other（其他国籍）
nationality_name        varchar(100)      N             ""          国籍名称（只有在region选择other的时候出现）
company_name            varchar(100)      N             ""          公司名称/个体工商户名称
company_en_name         varchar(200)      N             ""          公司英文名称（只有在region非cn的时候出现）
certificate_num         varchar(100)      N             ""          cn:营业执照号 tw:登记证编号 hk/mo/other:注册证书编号
register_address        varchar(100)      N             ""          注册地址/个体工商户执照地址
register_en_address     varchar(200)      N             ""          注册英文地址（只有在region非cn的时候出现）
certificate_img1        varchar(200)      N             ""          证书/个体工商户执照 图1
certificate_img2        varchar(200)      N             ""          证书 图2 （只有在region非cn的时候出现）
certificate_img3        varchar(200)      N             ""          证书 图3 （只有在region非cn的时候出现）
certificate_img4        varchar(200)      N             ""          证书 图4 （只有在region非cn的时候出现）
person_name             varchar(50)       N             ""          真实姓名
person_en_name          varchar(200)      N             ""          真实英文名
passport_num            varchar(50)       N             ""          护照号 (非cn出现)
id_card_num             varchar(18)       N             ""          身份证号 (cn出现)
person_address          varchar(100)      N             ""          cn:身份证地址 非cn:中文地址
person_en_address       varchar(200)      N             ""          英文地址(非cn出现)
passport_img            varchar(200)      N             ""          护照图片
id_card_front_img       varchar(200)      N             ""          身份证正面照片
id_card_back_img        varchar(200)      N             ""          身份证背面照片
created_at              bigint(20)        N             ""          创建时间
updated_at              bigint(20)        N             ""          更新时间
======================  ================  ============  ========    ================================================================================================

订单：orders
---------------------------------
======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)	      N                         主键id
name                    varchar(200)      N             ""          名称
order_type              varchar(70)       N             ""          订单的类型(商标注册:mark_reg)
price                   double            N             ""          价格
status                  varchar(100)      N             ""          订单状态 non_payment未付款、paid已付款、completed已完成、invalid作废
is_hidden               tinyint(4)        N             0           是否隐藏(对应前端用户的删除逻辑，只有状态不为paid的情况下才具备删除操作)
is_deleted              tinyint(4)        N             0           是否已删除
is_invoiced             tinyint(4)        N             0           是否已开发票
created_at              bigint(20)        N             ""          创建时间
updated_at              bigint(20)        N             ""          更新时间
======================  ================  ============  ========    ================================================================================================

订单支付信息：order_payments
---------------------------------
======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)	      N                         主键id
order_id                bigint(20)        N             0           订单编号
pay_mode                varchar(45)       N             ""          支付方式(支付宝：alipay)
pay_fee                 decimail(20,2)    N             ""          支付价格
pay_config              varchar(200)      N             ""          支付配置(支付宝：保存收款帐号)
buyer_account           varchar(200)      N             ""          付款帐号
trade_no                VARCHAR(200)      N             ""          支付接口返回的订单号
payment_time            bigint(20)        N             0           支付时间
created_at              bigint(20)        N             ""          创建时间
updated_at              bigint(20)        N             ""          更新时间
======================  ================  ============  ========    ================================================================================================


订单支付信息：order_statuses
---------------------------------
======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)	      N                         主键id
order_id                bigint(20)        N             0           订单编号
stuff_id                bigint(20)        N             0           修改状态的员工号
status                  varchar(40)       N             ''          修改之后的当前状态
created_at              bigint(20)        N             ""          创建时间






发票基本信息表：invoice_basics
---------------------------------------
======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)	      N                         主键id
user_id                 varchar(36)       N                         用户id
title                   varchar(200)      N             ""          名称
invoice_type            varchar(30)       N                         发票类型(normal:增值税普通发票, special:增值税专用发票)
taxpayer_certi_image    varchar(200)      N             ""          一般纳税人资格认证复印件
created_at              bigint(20)        N             ""          创建时间
updated_at              bigint(20)        N             ""          更新时间
======================  ================  ============  ========    ================================================================================================

发票表：invoices
---------------------------------------
======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)	      N                         主键id
user_id                 varchar(36)       N                         用户id
title                   varchar(200)      N             ""          发票抬头
invoice_num             varchar(200)      N             ""          发票编号
status                  varchar(30)       N             ""          发票状态(preparing:待邮寄, sent:已邮寄)
invoice_type            varchar(30)       N                         发票类型(normal:增值税普通发票, special:增值税专用发票)
taxpayer_certi_image    varchar(200)      N                         一般纳税人资格认证复印件
recipient               varchar(200)      N                         收件人
delivery_address        varchar(400)      N                         收货地址
contact_mobile          varchar(20)       N                         联系电话
express_num             varchar(40)       N                         快递编号
express_com             varchar(40)       N                         快递公司
created_at              bigint(20)        N             ""          创建时间
updated_at              bigint(20)        N             ""          更新时间
======================  ================  ============  ========    ================================================================================================

发票关联订单：invoice_orders
---------------------------------------
======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)	      N                         主键id
invoice_id              bigint(20)        N                         发票编号
order_id                bigint(20)        N             ""          订单id
created_at              bigint(20)        N                         创建时间
updated_at              bigint(20)        N                         更新时间
======================  ================  ============  ========    ================================================================================================

订单主体关联表：order_applicants
---------------------------------------
======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)        N                         主键id
user_id                 varchar(40)       N                         用户id
applicant_id            bigint(20)        N                         原始主体id
source_type             varchar(40)       N                         来源类型 申请主体:mark_reg_order_app/联合申请人主体:mark_reg_order_coapp
source_id               varchar(70)       N                         来源id(订单id)
name                    varchar(200)      N             ""          名称
profile_type            varchar(20)       N             ""          主体类型：person:个人 com:公司
region	                varchar(20)       N             ""          区域：cn（中国大陆）、hk（中国香港）、tw（中国台湾）、mo（中国澳门）、other（其他国籍）
nationality_name        varchar(100)      N             ""          国籍名称（只有在region选择other的时候出现）
company_name            varchar(100)      N             ""          公司名称/个体工商户名称
company_en_name         varchar(200)      N             ""          公司英文名称（只有在region非cn的时候出现）
certificate_num         varchar(100)      N             ""          cn:营业执照号 tw:登记证编号 hk/mo/other:注册证书编号
register_address        varchar(100)      N             ""          注册地址/个体工商户执照地址
register_en_address     varchar(200)      N             ""          注册英文地址（只有在region非cn的时候出现）
certificate_img1        varchar(200)      N             ""          证书/个体工商户执照 图1
certificate_img2        varchar(200)      N             ""          证书 图2 （只有在region非cn的时候出现）
certificate_img3        varchar(200)      N             ""          证书 图3 （只有在region非cn的时候出现）
certificate_img4        varchar(200)      N             ""          证书 图4 （只有在region非cn的时候出现）
person_name             varchar(50)       N             ""          真实姓名
person_en_name          varchar(200)      N             ""          真实英文名
passport_num            varchar(50)       N             ""          护照号 (非cn出现)
id_card_num             varchar(18)       N             ""          身份证号 (cn出现)
person_address          varchar(100)      N             ""          cn:身份证地址 非cn:中文地址
person_en_address       varchar(200)      N             ""          英文地址(非cn出现)
passport_img            varchar(200)      N             ""          护照图片
id_card_front_img       varchar(200)      N             ""          身份证正面照片
id_card_back_img        varchar(200)      N             ""          身份证背面照片
created_at              bigint(20)        N             ""          创建时间
updated_at              bigint(20)        N             ""          更新时间
======================  ================  ============  ========    ================================================================================================


商标相关
===========
商标注册订单表: mark_reg_orders
-------------------------------------

======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)        N
order_id                bigint(20)        N                         订单编号
user_id                 varchar(32)       N                         用户id
name                    varchar(100)      N             ""          商标名称
description             varchar(200)      N             ""          商标描述
mark_img                varchar(200)      N             ""          商标图片
applicant_id            bigint(20)        N                         申请主体id
category                varchar(10)       N             ""          商标类别
itemtree                varchar(2000)     N             ""          商标小项树结构(使用json数据结构)
items                   varchar(1000)     N             ""          商标小项（以,进行分割，小项最多增加到100）
is_three_d              tinyint(4)        N             0           以3维方式注册
three_d_img             varchar(200)      N             ""          3D 五面图片
is_color                tinyint(4)        N             0           以颜色组合注册
color_img               varchar(200)      N             ""          颜色组合图片
is_voice                tinyint(4)        N             0           以声音标志注册
voice_file              varchar(200)      N             ""          声音标志文件（mp3、wav）
is_portrait             tinyint(4)        N             0           以肖像权注册
portrait_img            varchar(200)      N             ""          肖像图片
is_co_applicants        tinyint(4)        N             0           共同申请人
co_applicants           tinyint(4)        N             0           共同申请人的主体id列表
is_prority              varchar(20)       N             0           优先权(no:否 before:在先优先权 exhibition:展会优先权)
prority_app_region      varchar(200)      N             ""          优先权-申请/展出国家/地区
prority_app_date        varchar(10)       N             ""          优先权-申请/展出日期 (yyyy-MM-dd)
prority_app_serial_num  varchar(50)       N             ""          优先权-申请号
app_serial_num          varchar(50)       N             ""          商标申请号
current_step            tinyint(4)        N             1           当前步骤(1:设置主体;2:商标;3:小项;4:附加;5:预览)
is_paid                 tinyint(4)        N             0           是否付款
is_confirmed            tinyint(4)        N             0           是否确认(确认后将不可修改，可以由后台客服修改当前的状态)
is_reviewed             tinyint(4)        N             0           是否审查(审查通过后就可以下载资料)
is_delegated            tinyint(4)        N             0           是否委托顾问帮助填写(一旦委托current_step就设置为5且不可修改)
is_delegate_confirmed   tinyint(4)        N             0           顾问填写完成确认提交
created_at              bigint(20)        N                         创建时间
updated_at              bigint(20)        N                         更新时间
======================  ================  ============  ========    ================================================================================================

商标类别项：mark_category_items
---------------------------------------

======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)	      N                         主键id
code                    varchar(40)       N             ""          商标编码
name                    varchar(500)      N             ""          商标编码名称
parent_code             varchar(40)       N             ""          商标父编码 ""表示顶级
created_at              bigint(20)        N             ""          创建时间
updated_at              bigint(20)        N             ""          更新时间
======================  ================  ============  ========    ================================================================================================


商标预判表：mark_forecast
---------------------------------------

======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)	      N                         主键id
user_id                 varchar(32)       N                         用户id
name                    varchar(100)      N             ""          商标名称
description             varchar(200)      N             ""          商标描述
mark_img                varchar(200)      N             ""          商标图片
status                  varchar(100)      N             ""          状态(may_apply:可申请; review:审核中; non_apply:不可申请, applying: 已经申请了)
is_deleted              tinyint(4)        N             ""          是否删除
created_at              bigint(20)        N             ""          创建时间
updated_at              bigint(20)        N             ""          更新时间
======================  ================  ============  ========    ================================================================================================





商标注册其他服务表:mark_reg_applies
----------------------------------------

======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)	      N                         主键id
user_id                 bigint(20)        N             ""          用户id
order_id                bigint(20)        N             ""          订单id
applicant_id            bigint(20)        N             ""          申请人主体id
address                 varchar(200)      N             ""          申请人地址
link_man                varchar(40)       N             ""          联系人名称
phone                   varchar(40)       N             ""          联系人电话
agency                  varchar(100)      N             ""          代理机构
mark_reg_num            varchar(40)       N             ""          商标注册号
service                 varchar(40)       N             ""          对应的服务(reissues：补发商标注册, prove: 商标证明申请, correct: 商标更正申请)
reissue_reason          varchar(200)      N             ""          补发理由
category                varchar(10)       N             ""          商标类别
itemtree                varchar(2000)     N             ""          商标小项树结构(使用json数据结构)
items                   varchar(1000)     N             ""          商标小项（以,进行分割，小项最多增加到100）
is_reset                tinyint(4)        N             ""          是否重置证书
modify_items            varchar(1000)     N             ""          更正的事项的json
is_paid                 tinyint(4)        N             0           是否付款
is_confirmed            tinyint(4)        N             0           是否确认(确认后将不可修改，可以由后台客服修改当前的状态)
is_reviewed             tinyint(4)        N             0           是否审查(审查通过后就可以下载资料)
created_at              bigint(20)        N                         创建时间
updated_at              bigint(20)        N                         更新时间
======================  ================  ============  ========    ================================================================================================


====
商标修改 部分
====

修改商标 名义/地址/规则/名单 表:mark_modify_info
----------------------------------------

======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)	      N                         主键id
user_id                 bigint(20)        N             ""          用户id
applicant_id            bigint(20)        N             ""          申请人主体id
address                 varchar(200)      N             ""          申请人地址
link_man                varchar(40)       N             ""          联系人名称
phone                   varchar(40)       N             ""          联系人电话
agency                  varchar(100)      N             ""          代理机构
mark_reg_num            varchar(255)       N             ""          商标注册号

======================  ================  ============  ========    ================================================================================================


=======
商标变更　
=======

商标变更：mark_change_orders
==================

======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)        N                         主键 id
user_id                 bigint(20)        N             ""          用户id
applicant_id            bigint(20)        N                         主体id
order_id                bigint(20)        N                         订单id
service_category        varchar(20)       N             ""          服务类别
price                   float             N             ""          费用
postal_code             varchar(10)       N             ""          邮政编码
applicant_name          varchar(20)       N             ""          联系人(默认个人信息里的，可修改)
applicant_mobile        varchar(20)       N             ""          电话(默认个人信息里的，可修改)
agent_name              varchar(50)       N             ""          代理机构名称
cha_agent_name          varchar(50)       N             ""          变更后代理机构名称
cha_file_rec_name       varchar(20)       N             ""          变更后文件接收人名称/变更前名义（中文）
name_en                 varchar(20)       N             ""          变更前名义（英文）
cha_file_rec_address    varchar(20)       N             ""          变更后文件接收地址/变更前地址（中文）
address_en              varchar(20)       N             ""          变更前地址（英文）
mark_reg_num            varchar(50)       N             ""          商标申请号/注册号
is_common_mark          bigint(5)         N             0           是否共有商标(0:否 1:没有)
is_man_rule             bigint(5)         N             0           是否变更管理规则(0:否 1:没有)
cha_man_rule_bef_path   varchar(50)       N             ""          上传变更前规则
cha_man_rule_aft_path   varchar(50)       N             ""          上传变更后规则
is_collective_names     bigint(5)         N             0           是否有变更集体成员名单(0:否 1:没有)
cha_bef_col_name_path   varchar(50)       N             ""          上传变更前集体成员名单
cha_atf_col_name_path   varchar(50)       N             ""          上传变更后集体成员名单
category                Text              N             ""          商标分类(json数据)
category_write          Text              N             ""          删减商品/服务项目（分类填写）
created_at              bigint(20)        N                         创建时间
updated_at              bigint(20)        N                         更新时间
======================  ================  ============  ========    ================================================================================================




====
商标转让 部分
====

商标转让表，包含申请商标转让/转移 、 补发商标转让/转移
============================================

======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)	      N                         主键id
user_id                 varchar(36)       N             ""          用户id
order_id                bigint(20)        N             ""          订单id
transfer_app_id         bigint(20)        N             ""          转让人的主题id
acceptor_app_id         bigint(20)        N             ""          受让人的主题id
post_num                varchar(20)       N             ""          邮政编码
link_man                varchar(40)       N             ""          联系人名称
phone                   varchar(40)       N             ""          联系人电话
agency                  varchar(100)      N             ""          代理机构
mark_reg_num            varchar(255)      N             ""          商标注册号
domestic_acc            varchar(50)       N             ""          国外受让人的国内接收人
domestic_acc_addr       varchar(50)       N             ""          国外受让人的国内接收人地址
domestic_acc_post_num   varchar(50)       N             ""          国外受让人的国内接收人的邮编
is_co_owner             varchar(50)       N             ""          是否共有人(转让前或转让后是否有共有人)
transfer_co_apps        varchar(1000)     N             ""          转让共有人，is_co_owner为true时有值
acceptor_co_apps        varchar(1000)     N             ""          受让共有人，is_co_owner为true时有值
is_confirmed            tinyint(4)        N             0           是否确认(确认后将不可修改，可以由后台客服修改当前的状态)
is_reviewed             tinyint(4)        N             0           是否审查(审查通过后就可以下载资料)
created_at              bigint(20)        N                         创建时间
updated_at              bigint(20)        N                         更新时间
======================  ================  ============  ========    ================================================================================================



=====
客服管理
=====

客服管理: customer_service_users
========================

======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)	      N                         主键id
staff_user_id           bigint(20)        N                         后台客服用户id(客服转移可以直接变化这个id就可以，对外名称等不变)
name                    varchar(20)       N                         客服名称
nickname                varchar(20)       N                         客服昵称(对外显示用此字段)
qq                      varchar(20)       N                         QQ号码
phone                   varchar(20)       N                         固定电话
email                   varchar(30)       N                         邮箱
introduction            varchar(200)      N                         客服简介
created_at              bigint(20)        N                         创建时间
updated_at              bigint(20)        N                         更新时间
======================  ================  ============  ========    ================================================================================================

客服统计: customer_service_stats
========================

======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)	      N                         主键id
csu_id                  varchar(36)       N                         后台客服用户id
untreated_order_num     bigint(5)         N                         未处理订单
confirm_order_num       bigint(5)         N                         已确认订单
created_at              bigint(20)        N                         创建时间
updated_at              bigint(20)        N                         更新时间
======================  ================  ============  ========    ================================================================================================


客服业务对应表: customer_service_bizs
========================

======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)	      N                         主键id
csu_id                  bigint(20)        N                         后台客服用户id
biz_name                varchar(50)       N                         负责业务名
======================  ================  ============  ========    ================================================================================================


订单客服关联表(customer_service_orders)
============================

======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)	      N                         主键id
csu_id                  bigint(20)        N                         客服id
order_id                bigint(20)        N                         订单id
treat_type              varchar(20)       N                         处理类型(待填订单，确认订单)
finish_status           bigint(5)         N                         完成状态(未处理、已确认)
created_at              bigint(20)        N                         创建时间
updated_at              bigint(20)        N                         更新时间
======================  ================  ============  ========    ================================================================================================



客服打赏表(order_tips)
------------------------
======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)	      N                         主键id
csu_id                  bigint(20)        N                         对应的客服id （如果不是代填的话此项为空）
stuff_id                bigint(20)        N                         代填客服的员工id（方便后台统计）
order_id                bigint(20)        N                         订单id
tip_amount              int(4)            N                         打赏金额
is_paid                 tinyint(3)        N                         是否支付
created_at              bigint(20)        N                         创建时间(一般为付款时间)
======================  ================  ============  ========    ================================================================================================



合同表(contracts)
-------------------
======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)	      N                         主键id
biz_name                varchar(40)       N                         业务名
contract                varchar(20)       N                         合同名
contract_name           varchar(40)       N                         合同中文名
seal_demand             varchar(30)       N                         盖章需求
part_num                varchar(30)       N                         份数要求
remark                  varchar(100)      N                         备注
======================  ================  ============  ========    ================================================================================================


版权业务相关
==============
文字/美术作品:copyright_opus_orders
------------------
======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)	      N                         主键id
user_id                 varchar(36)       N                         用户id
applicant_id            bigint(20)        N                         主体id
order_id                bigint(20)        N                         订单id
biz                     varchar(50)       N                         服务类别
opus_name               varchar(200)      N                         作品名称
opus_sample             varchar(200)      N                         作品样本
author_name             varchar(80)       N                         作者姓名或名称
opus_nature             bigint(5)         N                         作品创作性质
nature_description      varchar(200)      N                         作品创作性质说明(除原创外，都应该填写创作说明)
opus_finish_date        bigint(20)        N                         创作完成日期
opus_finish_country     varchar(20)       N                         完成创作国家
opus_finish_city        varchar(20)       N                         完成创作城市
publish_status          bigint(5)         N                         发表状态（已发表、未发表）
first_publish_data      bigint(20)        N                         首次发表时间
first_publish_country   varchar(20)       N                         首次发表国家
first_publish_city      varchar(20)       N                         首次发表城市
right_get_way           bigint(5)         N                         权利取得方式
right_get_description   varchar(200)      N                         权利取得方式说明(当权利取得方式选择“其他”时,填写此项)
right_ascription_way    bigint(5)         N                         权利归属方式
right_ascription        varchar(200)      N                         权利归属方式说明
right_own_state         bigint(5)         N                         权利拥有状况(全部、部分)
right_own_select        varchar(200)      N                         权利拥有选择(部分的选项)
opus_purpose            Text              N                         创作目的
opus_process            Text              N                         创作过程
opus_alone_create       Text              N                         创作独创性
opus_requisition        varchar(200)      N                         作品著作权申请书
is_delegated            bigint(5)         N             0           是否代填
is_delegate_confirmed   bigint(5)         N             0           代填确认
is_common_app           bigint(5)         N             0           是否有公共申请人
is_paid                 bigint(5)         N             0           是否付款
dielectric              varchar(200)      N                         电子介质
dielectric_piece        bigint(10)        N             0           电子介质(件)
paper_medium            varchar(200)      N                         纸介质
paper_medium_page       bigint(10)        N             0           纸介质(张)
created_at              bigint(20)        N                         创建时间
updated_at              bigint(20)        N                         更新时间
======================  ================  ============  ========    ================================================================================================

软件版权申请:copyright_soft_orders
----------------
======================  ================  ============  ========    ================================================================================================
Name                    Type              Is Null       Default     Markup
======================  ================  ============  ========    ================================================================================================
id                      bigint(20)	      N                         主键id
user_id                 varchar(36)       N                         用户id
applicant_id            bigint(20)        N                         主体id
order_id                bigint(20)        N                         订单id
biz                     varchar(50)       N                         服务类别
soft_name               varchar(100)      N                         软件名称
soft_abb                varchar(50)       N                         软件简称
version_num             varchar(20)       N                         版本号
soft_description        binint(10)        N                         软件作品说明(原创，　修改(含翻译软件、合成软件))
modify_select           varchar(50)       N                         修改选择项
trans_description       varchar(400)      N                         修改合成或翻译说明
soft_finish_date        bigint(20)        N                         软件开发完成日期
is_publish              bigint(5)         N                         是否发表
publish_date            bigint(20)        N                         发表日期
first_publish_country   varchar(20)       N                         首次发表国家
first_publish_city      varchar(20)       N                         首次发表城市
develop_way             bigint(5)         N                         开发方式
right_get_way           bigint(5)         N                         权利取得方式
acquisition_select      binint(5)         N                         继受取得(受让  承受  继承)
is_soft_reg             bigint(5)         N                         软件是否已登记

source_reg_num          varchar(30)       N                         原登记号
is_reg_num_change       bigint(5)         N                         原登记是否做过变更或补充
change_reg_num          varchar(150)      N                         变更或补充证明编号
right_range             bigint(5)         N                         权利范围
range_select            varchar(100)      N                         范围的部分选项
hardware_env            varchar(255)      N                         硬件运行硬件环境
software_env            varchar(255)      N                         软件运行软件环境
pro_lan                 varchar(100)      N                         编程语言
source_pro_size         varchar(40)       N                         源程序量
function_feature        varchar(700)      N                         软件功能和技术特点
source_program          varchar(200)      N                         源程序
program_description     varchar(200)      N                         程序使用说明书
is_delegated            bigint(5)         N             0           是否代填
is_delegate_confirmed   bigint(5)         N             0           代填确认
is_common_app           bigint(5)         N             0           是否有公共申请人
is_paid                 bigint(5)         N             0           是否付款
created_at              bigint(20)        N                         创建时间
updated_at              bigint(20)        N                         更新时间
======================  ================  ============  ========    ================================================================================================
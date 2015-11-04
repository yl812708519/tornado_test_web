/**
 * Created by oubunfei on 15/3/27.
 */
/**
 * Created by oubunfei on 15/3/27.
 */
function gatData(){
    var arr_list = [{'books1': [{'title': '1.单位的经营范围：','select':{'A':'电子与信息', 'B':'新能源与节能', 'C':'生物医药技术', 'D':'环境保护', 'E':'新材料', 'F':'航空航天', 'G':'光机电一体化','H':'其他'}, 'has_too_select':0},
                       {'title': '2.现有职工总数：', 'select':{'A':'20人以下', 'B':'20-50人', 'C':'50-100人', 'D':'100-500人', 'E':'500人以上'}, 'has_too_select':0},
                       {'title': '3.单位性质（可多选）：', 'select':{'A':'转制为单位的科研院所', 'B':'国有单位；', 'C':'集体所有制单位；', 'D':'股份合作单位；', 'E':'联营单位；', 'F':'有限责任公司；', 'G': '股份有限公司；', 'H': '私营单位；', 'I': '港澳台商投资单位；', 'J':'中外合资经营单位；','K':'中外合作经营单位；','L': '外商独资单位；','M':'其他。'}, 'has_too_select':4},
                       {'title':'4.单位是否为高新单位：','select':{'A':'国家级高新技术单位','B':'省级高新技术单位','C':'地市级高新技术单位','D':'以上都不是'},'has_too_select':0}
                      ],
                 'books2': [{'title': '1.单位申报知识产权的目的（多选）:', 'select':{'A':'出于政府项目申报的要求', 'B':'为了完成相关部门的要求', 'C':'出于保护自身技术或品牌的需求', 'D':'提高单位形象，提高产品形象', 'E':'为了满足商务需求','F':'我们没有申报过任何知识产权'}, 'has_too_select':2,'coerce_select':{'F':['A','B','C','D','E']},'score':{'A':1,'B':1,'C':6,'D':2,'E':1,'F':0}},
                       {'title': '2.到目前为止，单位是否申请过专利：', 'select':{'A':'是', 'B':'否'}, 'has_too_select':0,'coerce_question':{'B':[3,4]},'score':{'A':1,'B':0}},
                       {'title':'3.到目前为止，单位在中国申请的专利数量（包括三种专利）：','select':{'A':'1-10件','B':'10-50件','C':'50-100件','D':'100件以上'},'has_too_select':0,'score':{'A':2,'B':3,'C':4,'D':'5'}},
                       {'title':'4.到目前为止，单位在外国申请的专利数量：','select':{'A':' 0件','B':'1-10件','C':'10-50件','D':'50件以上'},'has_too_select':0,'score':{'A':0,'B':3,'C':4,'D':5}},
                       {'title':'5.到目前为止，单位是否注册过商标：','select':{'A':'是','B':'否'},'has_too_select':0,'coerce_question':{'B':[6,7]},'score':{'A':1,'B':0}},
                       {'title':'6.到目前为止，单位在中国注册的商标的数量（一标N类的按N件计算）：','select':{'A':'1-10件','B':'10-50件','C':'50-100件','D':'100件以上'},'has_too_select':0,'score':{'A':2,'B':3,'C':4,'D':5}},
                       {'title':'7.到目前为止，单位在外国注册的商标数量（一标N类的按N件计算）：','select':{'A':'0件','B':'1-10件','C':'10-50件','D':'50件以上'},'has_too_select':0,'score':{'A':0,'B':3,'C':4,'D':5}},
                       {'title':'8.到目前为止，单位是否登记过版权：','select':{'A':'是','B':'否'},'has_too_select':0,'coerce_question':{'B':[9]},'score':{'A':1,'B':0}},
                       {'title':'9.到目前为止，单位在中国获得登记的版权的数量：','select':{'A':'1-10件','B':'1-50件','C':'50-100件','D':'100件以上'},'has_too_select':0,'score':{'A':2,'B':3,'C':4,'D':5}}
                      ],
                 'books3':[{'title':'1.到目前为止，单位对专利缴纳年费的策略是:','select':{'A':'所有专利获得授权后就不再缴纳年费','B':'所有专利获得授权后缴纳年费3年','C':' 所有专利获得授权后至少缴纳年费5年以上','D':'所有专利获得授权后至少缴纳年费3年，针对有需要继续维持的继续缴纳年费'},'has_too_select':0,'score':{'A':0,'B':2,'C':4,'D':5}},
                      {'title':'2.到目前为止，单位对专利缴纳年费的策略是：','select':{'A':' 所有专利不做区分，一视同仁','B':'由行政管理人员确定哪项专利需要维持多长时间','C':'由技术人员确定哪项专利需要维持多长时间','D':'由知识产权管理人员确定哪项专利需要维持多长时间'},'has_too_select':0,'score':{'A':0,'B':1,'C':3,'D':5}},
                      {'title':'3.到目前为止，单位对商标的续展情况：','select':{'A':'商标权尚未到期，还未涉及续展问题','B':'对商标权全部进行续展','C':'针对有用的商标进行了续展，作用不大的商标作了放弃处理','D':'商标还能续展？不清楚这个事'},'has_too_select':0,'score':{'A':2,'B':2,'C':4,'D':0}},
                      {'title':'4.是否定期组织市场部门、技术部门会同知识产权管理部门对已有知识产权进行联合评估，以确定其延续时间：','select':{'A':'是','B':'否'},'has_too_select':0,'score':{'A':5,'B':0}}
                     ],
                 'books4':[{'title':'1.到目前为止，单位授权专利的实施情况：','select':{'A':'绝大多数专利技术未在日常生产经营中进行实施','B':'部分专利技术进行了实施，实施过程中可能对专利技术内容有改动','C':'部分专利在日常生产经营中得到了实施'},'has_too_select':0,'score':{'A':0,'B':2,'C':4}},
                      {'title':'2.到目前为止，单位将自有专利权许可或转让他人使用的情况：','select':{'A':'没有将自有专利权许可或转让他人的情况','B':'存在自有专利权许可或转让给了关联单位或集团内兄弟单位的情况','C':'存在自有专利权许可或转让给其他无关联关系的单位使用的情况'},'has_too_select':0,'score':{'A':0,'B':2,'C':4}},
                      {'title':'3.到目前为止，单位获得他人专利权许可使用的情况：','select':{'A':'没有获得他人专利权许可或转让他人的情况','B':'存在获得了关联单位或集团内兄弟单位的专利权许可的情况','C':'存在获得无关联关系单位的专利权许可的情况'},'has_too_select':0,'score':{'A':0,'B':2,'C':4}},
                      {'title':'4.到目前为止，单位注册商标的实施情况：','select':{'A':'注册的商标没有使用','B':'注册的商标在使用'},'has_too_select':0,'score':{'A':0,'B':2}},
                      {'title':'5.到目前为止，是否发现他人侵犯自己知识产权的情况：','select':{'A':'是','B':'否'},'coerce_question':{'B':[6,7]},'has_too_select':0,'score':{'A':3,'B':0}},
                      {'title':'6.是通过何种渠道发现他人侵犯自己知识产权的？','select':{'A':'无意间得知','B':'单位内部员工反馈','C':'有专门的人员或部门对市场上相关产品进行定期分析，通过分析得知'},'has_too_select':0,'score':{'A':0,'B':2,'C':4}},
                      {'title':'7.了解他人侵犯自己知识产权之后有什么行动？','select':{'A':'侵权人量小势微，不需要也不值得做什么','B':'直接与侵权人联系，要求其停止侵权行为，并提出赔偿','C':'由专人或专门的部门进行侵权情况分析，后通过专业服务机构（如律师事务所、知识产权代理机构）对侵权方提出诉求'},'has_too_select':0,'score':{'A':0,'B':2,'C':4}},
                      {'title':'8.是否了解自有产品涉及侵犯他人知识产权的情况，如何了解？','select':{'A':'不做了解','B':'会不定期进行市场调查，通过比对市场上的产品来了解','C':'会定期对市场上的主要竞争者的专利技术进行分析，以此确定自有产品是否涉及侵权','D':'会定期进行自有产品所属技术领域的专利技术分析，以此确定自有产品是否涉及侵权'},'has_too_select':0,'score':{'A':0,'B':2,'C':4,'D':5}}
                     ],
                 'books5': [{'title': '1.单位目前已有以下体系文件（可多选）:', 'select':{'A':'知识产权管理制度', 'B':'年度知识产权申请计划', 'C':' 技术研发中的知识产权评议制度', 'D':'原材料采购中的知识产权审核制度', 'E':'知识产权项目档案保管制度','F':'与涉及技术研发的员工签订的技术保密协议','G':'以上都没有'}, 'has_too_select':2,'coerce_no_select':{'G':['A','B','C','D','E','F']},'score':{'A':4,'B':4,'C':4,'D':4,'E':4,'F':4,'G':0}},
                       {'title': '2.单位目前关于设立的创新与保护的相关部门（可多选）:', 'select':{'A':'知识产权管理部门', 'B':'产品研发部门', 'C':'有知识产权管理人员，但没有专门部门', 'D':'有产品研发人员，但没有专门部门', 'E':'以上都没有'}, 'has_too_select':3,'coerce_no_select':{'E':['A','B','C','D']},'score':{'A':4,'B':4,'C':2,'D':2,'E':0},'select_limit':{'1':['A','C'],'2':['B','D']}},
                       {'title':'3.是否有聘请知识产权代理机构或知识产权法律顾问机构为单位服务：','select':{'A':'有，而且是常年稳定的某一家或几家服务机构','B':'有，碰到有需要的事情现找','C':'没有，自己处理相关事务'},'has_too_select':0,'score':{'A':8,'B':4,'C':0}}
                      ]
        }]

    arr_list.forEach(function (item){
        var first_content = item.books1;
        var html = '';
        first_content.forEach(function (item,content){
            var title = item.title;
            var select = item.select;
            var data_code = item.has_too_select;

            var subHtml = '';
                for (var content in select) {
                    subHtml += '<span class="col-sm-3" data-id="'+content+'">'+content+'.' + select[content]+'</span>'
                }

            html += '<dl class="item" data-code="'+data_code+'"><dt>'+title+'</dt><dd class="row">'+subHtml+'</dd></dl>'
        })
        $('.first-container').html(html)
        /*books2*/
        var second_content = item.books2;
        var third_content = item.books3;
        var fourth_content = item.books4;
        var fifth_content = item.books5;
        getData(second_content,'second-container')
        getData(third_content,'third-container')
        getData(fourth_content,'fourth-container')
        getData(fifth_content,'fifth-container')

    });
    function getData(third_content,content){
        var third_html = '';
        third_content.forEach(function (item,content){
            var title = item.title;
            var select = item.select;
            var score_ = item.score;
            var data_code = item.has_too_select;
            var suphtml = '';
            var subHtml = '';
                for (var content in select) {

                    subHtml += '<span class="col-sm-3" data-id="'+content+'" data-fen="'+score_[content]+'">'+content+'.' + select[content]+'</span>'
                }
             third_html += '<dl class="item" data-code="'+data_code+'"><dt>'+title+'</dt><dd class="row">'+subHtml+''+suphtml+'</dd></dl>'

        })
        $('.'+content).html(third_html)
    };

    /*单选*/
    var $has_select = $('dl[data-code=0]');

    $has_select.on('click','span',function (){
        $(this).addClass('active').siblings('span').removeClass('active');
    });

    /*提示框*/
    function tipHook(content,index){
        var $content = $('.'+content)
        $content.on('click','dd span',function (){

            var visublelen = $content.find('.item:visible').length;
            var chiledlen = $content.find('.active').parents('.item').length;
            visublelen == chiledlen ? $('.hook li:eq('+index+') a').addClass('current') : $('.hook li:eq('+index+') a').removeClass('current')
        });
    }
    tipHook('first-container',0);
    tipHook('second-container',1);
    tipHook('third-container',2);
    tipHook('fourth-container',3);
    tipHook('fifth-container',4);

    /*special task*/
    function specialTask(container,index){

        var $no_select = $('.'+container).find('.item:eq('+index+') span').eq(1);
        var $yes_select = $('.'+container).find('.item:eq('+index+') span').eq(0);
        var $no_question1 = $('.'+container).find('.item').eq(index+1)
        var $no_question2 = $('.'+container).find('.item').eq(index+2)

        $no_select.on('click',function (){
             $no_question1.find('span').removeClass('active')
            $no_question2.find('span').removeClass('active')

            $no_question1.hide();
            $no_question2.hide();

        })
       $yes_select.on('click',function (){
           $no_question1.show();
            $no_question2.show();
       })
    }
    specialTask('second-container',1)
    specialTask('second-container',4)
    specialTask('second-container',7)
    specialTask('fourth-container',4)
    /*多选 删除*/
    var $special_select = $('dl[data-code=4]');

    $special_select.on('click','span',function (){
       $(this).hasClass('active') ? $(this).removeClass('active') : $(this).addClass('active')
    });
    /*special 第二部分1，第五部分1*/

    var $last_select = $('.second-container [data-code=2] dd span').last();
    var $nolast_select = $('.second-container [data-code=2] dd span:not(:last)');

    $nolast_select.click(function (){
         $(this).hasClass('active') ? $(this).removeClass('active') : $(this).addClass('active')
        $last_select.removeClass('active');
    });
    $last_select.click(function (){

        $(this).addClass('active').siblings('span').removeClass('active');
    });
    var $last_selects = $('.fifth-container [data-code=2] dd span').last();
    var $nolast_selects = $('.fifth-container [data-code=2] dd span:not(:last)');

    $nolast_selects.click(function (){
        $(this).hasClass('active') ? $(this).removeClass('active') : $(this).addClass('active')
        $last_selects.removeClass('active');

    });
    $last_selects.click(function (){

        $(this).addClass('active').siblings('span').removeClass('active');
    });
    /*第五部分第二题*/
    var special_other = $('.fifth-container [data-code=3] dd span');
    var special_other_l = $('.fifth-container [data-code=3] dd span').last();

    special_other_l.click(function (){
        $(this).addClass('active').siblings('span').removeClass('active');
    });
    function delect_select(index){
        special_other.eq(index).click(function (){
             $(this).hasClass('active') ? $(this).removeClass('active') : $(this).addClass('active')
            special_other.eq(index+2).removeClass('active')
            special_other_l.removeClass('active');
        });
        special_other.eq(index+2).click(function (){
            $(this).hasClass('active') ? $(this).removeClass('active') : $(this).addClass('active')
            special_other.eq(index).removeClass('active')
            special_other_l.removeClass('active');
        });

    }
    delect_select(0);
    delect_select(1);

    /*end*/
//    前端校验
    $('.cus_radio li').click(function (){
        $('.tip').slideUp();
    });

    $("#submitBtn").on('click',function (){

        var con_type = $('input[name=com_type]').val();

        if(con_type == ''){
            $('.tip').slideDown();
        };

        var el = $('.item dd .active');
        var el_parent = el.parents('dl');
        var len = el_parent.length;
        var dl_len = $('dl:visible').length;
        if(dl_len !== len && !con_type == ''){

            $('.tip').html('亲，题目还木有选完哦！')
            $('.tip').slideDown();
        }
        if(dl_len == len && !con_type == ''){
            $('#info_Modal').modal();
            $('.tip').slideUp();
        };
    });
    /*获取第一部分的选项*/
     $(document).on('click', '.first-container  dd span', function () {
        var $this = $(this);
        var uid = $this.data('id');
        var arr = [].slice.call($this.closest('.item').find('span.active'));
        var scoreArr = [];

        arr.forEach(function (item){
            var $item = $(item);

            scoreArr.push($item.data('id'));

        })

        $this.closest('.item').attr('scoreArr',scoreArr)

    })
    /*计算分数 和选项*/
    /*获取第二，三，四，五部分单选时，选项，和分数*/
    $(document).on('click', '.second-container [data-code="0"] dd span,.third-container [data-code="0"] dd span,.fourth-container [data-code="0"] dd span,.fifth-container [data-code="0"] dd span', function () {
        var $this = $(this);
        var uid = $this.data('id');
        var arr = [].slice.call($this.closest('.item').find('span.active'));
        var scoreArr = [];
        var totalFen = 0;

        arr.forEach(function (item){
            var $item = $(item);
            var subFen = $item.data('fen');

            totalFen = subFen;
            scoreArr.push($item.data('id'));

        })

        $this.closest('.item').attr('scoreArr',scoreArr)
        $this.closest('.item').attr('totalFen',totalFen)

    });
    /*第二部分 多选 和第五部分多选*/

    $(document).on('click', '.second-container [data-code="2"] dd span,.fifth-container [data-code="2"] dd span,.fifth-container [data-code="3"] dd span', function () {
        var $this = $(this);
        var fen = $this.data('fen')
        var uid = $this.data('id');
        var totalFen = 0;
        var arr = [].slice.call($this.closest('.item').find('span.active'));
        var scoreArr = [];

        arr.forEach(function (item) {
            var subFen = $(item).data('fen');

            totalFen += subFen;
        });
        /*if (arr.filter(function (item) {return $(item).data('id') == 'F'}).length != 0) {
            totalFen = 0
        } else {
            arr.forEach(function (item) {
                var subFen = $(item).data('fen');

                totalFen += subFen;
            });
        }*/
        arr.forEach(function (item) {
            var $item = $(item);

            scoreArr.push($item.data('id'));
        });

        $this.closest('.item').attr('scoreArr', scoreArr);
        $this.closest('.item').attr('totalFen', totalFen);
    });


}gatData();
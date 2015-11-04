$(function () {

//    //日期组件
//    /*
//    * 由于页面自适应设计，需要指定container，不能使用默认的body
//    * 否则日期组件定位不对
//    * 使用日期主键时，需要在日期组件父组件添加一个picker-container class类
//    * */
//    if($('.form_date').datetimepicker){
//        $('.form_date').datetimepicker({
//            language:  'zh-CN',
//            container:'.picker-container',
//            format:'yyyy-mm-dd',
//            weekStart: 1,
//            todayBtn:  1,
//            autoclose: 1,
//            todayHighlight: 1,
//            startView: 2,
//            minView: 2,
//            forceParse: 0
//        });
//    }
});

//写Cookie
function addCookie(objName, objValue, objHours) {
    var str = objName + "=" + escape(objValue);
    if (objHours > 0) {//为0时不设定过期时间，浏览器关闭时cookie自动消失
        var date = new Date();
        var ms = objHours * 3600 * 1000;
        date.setTime(date.getTime() + ms);
        str += "; expires=" + date.toGMTString();
    }
    document.cookie = str;
}

//读Cookie
function getCookie(objName) {//获取指定名称的cookie的值
    var arrStr = document.cookie.split("; ");
    for (var i = 0; i < arrStr.length; i++) {
        var temp = arrStr[i].split("=");
        if (temp[0] == objName) return unescape(temp[1]);
    }
    return "";
}
//固定底部导航的函数
function fixed_footer(){
    var liuH = document.documentElement.clientHeight;
    var bodyH = $('body').height() + 50;
    if (bodyH < liuH) {
        $('.footer').addClass('navbar-fixed-bottom');
    }
}
//基于bootstrap编写的模态提示框
function wModalDialog(options){
    var type = options.type||"confirm";//类型 alert  confirm success failed
    var title = options.title||"友情提示";//标题
    var content = options.content||"您确定吗？";//提示内容
    var cancelCallBack = options.cancelCallBack||function(){};//关闭按钮，X点击回调
    var sureCallBack = options.sureCallBack||function(){};//确认按钮回调
    var showAnimate = options.showAnimate? true:false;//是否显示动画效果

    if(type=="success"){
        content='<div style="text-align: center"><span class="glyphicon glyphicon-ok" style="color:green;font-size:40px;"></span></div><div style="text-align: center">'+content+'</div>'
        type="alert";
    }
    if(type=="failed"){
        content ='<div style="text-align: center"><span class="glyphicon glyphicon-remove" style="color:red;font-size:40px;"></span></div><div style="text-align: center">'+content+'</div>',
        type="alert";
    }

    var fade = showAnimate?"fade":"";
    var modalHtml = ''
        +'<div class="modal clean_empty '+fade+' " id="wModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">'
            +'<div class="modal-dialog">'
                +'<div class="modal-content">'
                    +'<div class="modal-header">'
                        +'<button type="button" class="close wCancle" ><span aria-hidden="true">&times;</span><span class="sr-only">关闭</span></button>'
                        +'<h4 class="modal-title" id="wModalLabel">'+title+'</h4>'
                    +'</div>'
                    +'<div class="modal-body">'
                        +content
                    +'</div>'
                    +'<div class="modal-footer">'
                        +'<button type="button" class="btn btn-success wSure" >确定</button>'
                        +'<button type="button" class="btn btn-danger wCancle" >关闭</button>'
                    +'</div>'
                +'</div>'
            +'</div>'
        +'</div>';
    $("body").append(modalHtml);
    if(type=="alert"){
        $("#wModal .wSure").hide();
    }
    if(type=="confirm"){
        $("#wModal .wSure").show();
    }
    //初始化modal
    $('#wModal').modal({
        keyboard: false,
        backdrop:false
    });
    $('#wModal').on('hidden.bs.modal', function (e) {
            $('#wModal').remove();
        })
    //绑定事件
    $("#wModal .wSure").click(function(){
        $('#wModal').modal('hide');

        if(sureCallBack){
            sureCallBack();
        }
    });
    $("#wModal .wCancle").click(function(){
        $('#wModal').modal('hide');
        if(cancelCallBack){
            cancelCallBack();
        }
    });



}


//原生select组件级联操作
function wCascadeSelect(options){
    var parentSelectId = options.parentSelectId;
    var childSelectId = options.childSelectId;
    var hasNull = options.hasNull==undefined?true:options.hasNull;
    var nullValue = options.nullValue==undefined?"":options.nullValue;
    var nullText = options.nullText==undefined?"==请选择==":options.nullText;
    var valueField= options.valueField;
    var nameField = options.nameField;
    var subTypeField = options.subTypeField;
    var dataUrl = options.dataUrl;
    var idField = options.idField;
    var complete = options.complete;

    if (!parentSelectId){
        alert("父级下拉id未指定!");
        return;
    }
    if(!childSelectId){
        alert("子级下拉未指定!");
        return;
    }

    var $parentSelect = $("#"+parentSelectId);
    var $childSelect = $("#"+childSelectId);
    $parentSelect.change(function(){
        var parentValue = $(this).val();
        var sub_type = $(this).find("option[value='"+parentValue+"']").attr("sub_type")
        var params = {}
        params[idField] = parentValue;
        params["sub_type"] = sub_type;
        $.ajax({
            type: "get",
            async:false,
            url:dataUrl ,
            data:params,
            beforeSend: function(XMLHttpRequest){
                $childSelect.addClass("disabled")
            },
            success: function(data, textStatus){
                $childSelect.html("");
                if(hasNull){
                    $childSelect.append('<option value="'+nullValue+'">'+nullText+'</option>');
                }
                for(i=0;i<data.list.length;i++){
                    var dep = data.list[i];
                    $childSelect.append('<option value="'+dep[valueField]+'" sub_type="'+dep[subTypeField]+'">'+dep[nameField]+'</option>');
                }
            },
            complete: function(XMLHttpRequest, textStatus){
                $childSelect.removeClass("disabled");
                if(complete){
                    complete();
                }
            },
            error: function(XMLHttpRequest, textStatus, errorThrown){
                alert("error:"+XMLHttpRequest+textStatus+errorThrown);
            }
        });
    });


}
/*var JPlaceHolder = {
    *//*placeholder 兼容IE*//*
    //检测
    _check : function(){
        return 'placeholder' in document.createElement('input');
    },
    //初始化
    init : function(){
        if(!this._check()){
            this.fix();
        }
    },
    //修复
    fix : function(){
        jQuery(':input[placeholder]').each(function(index, element) {
            var self = $(this), txt = self.attr('placeholder');
            self.wrap($('<div></div>').css({position:'relative', zoom:'1', border:'none', background:'none', padding:'none', margin:'none'}));
            var pos = self.position(), h = self.outerHeight(true), paddingleft = self.css('padding-left');
            var holder = $('<span></span>').text(txt).css({position:'absolute', left:pos.left, top:pos.top, height:h, lienHeight:h, paddingLeft:paddingleft, color:'#aaa'}).appendTo(self.parent());
            self.focusin(function(e) {
                holder.hide();
            }).focusout(function(e) {
                if(!self.val()){
                    holder.show();
                }
            });
            holder.click(function(e) {
                holder.hide();
                self.focus();
            });
        });
    }
};
//执行
jQuery(function(){
    JPlaceHolder.init();
});*/

function showErr(field, error) {
    /*
    * 处理后端校验，样式与前端统一
    * */
    var $inputVal = $('[name="' + field + '"]');
    var html = $('<small class="help-block back-vil" data-bv-for="' + field + '" data-bv-result="INVALID" style="">' + error + '</small>');
    if ($inputVal) {
        $inputVal.parents(".form-group").addClass('has-error');
    }//data-bv-validator="notEmpty"
    if($inputVal.length>1){
        $inputVal.eq(0).closest('div').find('.back-vil').length == 0 ?
        html.appendTo($inputVal.eq(0).closest('div')):
            $inputVal.eq(0).closest('div');
    }else {
        $inputVal.siblings('.back-vil').length == 0 ? $inputVal.after(html) : $inputVal
        $inputVal.parents(".form-group").find('.form-control-feedback').removeClass('glyphicon-ok').addClass('glyphicon-remove');
    }
    $inputVal.keyup(function () {
        $inputVal.parent().find('.back-vil').remove();
    });
    $inputVal.focus(function (){
         $inputVal.parents('.form-group').find('.back-vil').remove();
         $inputVal.parents('.form-group').removeClass('has-error').addClass('has-success');
         $inputVal.parents('.ajaxForm_div').find('input[type=submit]').removeAttr('disabled','')
    });
}
//在线咨询
function getStyle(obj, name) {
    if (obj.currentStyle) {
        return obj.currentStyle[name];
    }
    else {
        return getComputedStyle(obj, false)[name];
    }
}
function Running(obj, json, fnEnd) {
    clearInterval(obj.timer);
    obj.timer = setInterval(function () {
        var now = 0;
        var bStop = true;
        for (var attr in json) {
            if (attr == 'opacity') {
                now = Math.round(parseFloat(getStyle(obj, attr)) * 100);
            }
            else {
                now = parseInt(getStyle(obj, attr));
            }
            var speed = (json[attr] - now) / 5;
            speed = speed > 0 ? Math.ceil(speed) : Math.floor(speed);
            if (now != json[attr])bStop = false;
            if (attr == 'opacity') {
                obj.style.filter = 'alpha(opacity:' + now + speed + ')';
                obj.style.opacity = (now + speed) / 100;
            }
            else {
                obj.style[attr] = speed + now + 'px';
            }
        }
        if (bStop) {
            clearInterval(obj.timer);
            if (fnEnd)fnEnd();
        }
    }, 30);
};
$(document).ready(function () {
    var oBox = document.getElementById('oncs');
    var oTitle = $('#oncs .title');
    var closed = '关闭窗口';
    var opened = '在线客服';
    var i = 0;
    $('#oncs .title').click(function(){
         i++;
        (i % 2) ? Running(oBox, {right: 0}, function () {
            oTitle[0].innerHTML = closed;
        })
            : Running(oBox, {right: -180}, function () {
            oTitle[0].innerHTML = opened;
        });
    })
});
//oss_url .
;function oss_url(src){
    return 'http://dev.b.i.cdn.eking99.cn/'+src
};
function oss_url1(src){
    return 'http://dev.b.i.cdn.eking99.cn/'+src
};
function detatil(src){
    return 'http://eking-yestar-test.oss-cn-beijing.aliyuncs.com/'+src
};
//IE forEach
if (!Array.prototype.forEach) {
    Array.prototype.forEach = function(fun /*, thisp*/) {
        var len = this.length;
        if (typeof fun != "function")
            throw new TypeError();

        var thisp = arguments[1];
        for (var i = 0; i < len; i++) {
            if (i in this)
                fun.call(thisp, this[i], i, this);
        }
    };
};
function getCategory(itemtree,items){
//        一类别
    function getJsonData(url, callback) {
        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'json',
            success: function (result) {
                callback && callback(result)
            },
            error: function (err) {
                console.log(err)
            }
        })
    };

    var renderFirst = function () {
        var firstContainer = $('.first-container');

        getJsonData('/s/data/data1.json', function (result) {
            var firstContainerHtml = '';

            result.forEach(function (item, key) {
                firstContainerHtml += '<dd class="list-group-item"><span class="left" data-id="'+item.id+'" data-i="' + item.code + '">' + item.code + '</span><span class="right">' + item.name + '</span></dd>'
            })
            firstContainer.html(firstContainerHtml)
        })
    }
    renderFirst();
    var renderSecond = function (code, callback) {
        var firstContainer = $('.second-container');
        var code = Number(code);


        getJsonData('/s/data/data2.json', function (result) {
            var firstContainerHtml = '';
            result.forEach(function (item, key) {
                if (item.parent_code == code) {
                    firstContainerHtml += '<dd class="list-group-item"><span class="left '+item.code+'" data-sencode="'+item.id+'">' + item.code + '</span><span class="right">' + item.name + '</span></dd>';

                }
            });

            firstContainer.html(firstContainerHtml);
            $('.child-type').fadeIn();
        });

        callback && callback();

    };
    $('.first-container').on('click', 'dd', function () {
        var $this = $(this);
        var len = $('#allul').find('ul').length;

        if (len == 0) {
            $this.find('span:eq(0)').addClass('active').parent().siblings('.list-group-item').find('span:eq(0)').removeClass('active');
        }

        var code = $this.children('span:eq(0)').text();

        renderSecond(code, function () {
            // console.log('Render Second success');
        });
    });
    var renderThird = function (code, callback) {
        var firstContainer = $('.third-container');
        $.ajax({
            url: '/mark/category.json',
            type: 'post',
            dataType: 'json',
            data: {parent_code: code, _xsrf: $('input[name=_xsrf]').val()},
            success: function (result) {
                var firstContainerHtml = '';
                var list = result.list;

                for (var i in list) {
                    if (list[i].parent_code == code) {
                        firstContainerHtml += '<div class="checkbox"><label>'+ list[i].name +'<input type="checkbox" data-value="'+list[i].id+'" data-parencode="'+$('.'+list[i].parent_code).data('sencode')+'" value="' + list[i].code + '"></label></div>';
                    }
                }

                firstContainer.html(firstContainerHtml);
                $('.content').fadeIn();
            },
            error: function (err) {
                console.log(err)
            }
        });

    };
    $('.second-container').on('click', 'dd', function () {
        var $this = $(this);
        var code = $this.children('span:eq(0)').text();
        var secondTxt = $this.children('span:eq(1)').text();
        $('.subtext span').html(secondTxt);
        $('.subtext input[name=second_code]').val(code);
        renderThird(code, function () {
            // console.log('Render Second success');
        });
    });
    $(document).on('click','.third-container input[type=checkbox]',function (){
        var $this = $(this);
        var code = $(this).val();
        var thirs_subcode = $(this).data('value');
        var parencode = $(this).data('parencode');
        var name = $this.parent('label').text();

        var second_code = $this.parents('.content').find('input[name=second_code]').val();
        var second_code_atr = second_code.substr(0,2);
        var seclist = $('#' + second_code);
        var inputs = $('#inputs');
        if ($(this).is(':checked')) {
            if ($('#allul ul').length == 0) {
                $('#allul').append("<ul id=" + second_code + "><li id=" + code + " class="+thirs_subcode+">" + name + ".<span class='glyphicon glyphicon-remove delete'></span></li></ul>");
                inputs.append('<input type="hidden" class="'+second_code+'" name="'+itemtree+'" value="' + parencode + '">')
                inputs.append('<input type="hidden" class="'+code+'"  name="'+items+'" value="' + thirs_subcode + '">')

            } else {
                if (seclist.text() !== '') {
                    if (seclist.children('.' + thirs_subcode).length == 0) {
                        console.log(name,seclist)
                        seclist.append("<li id=" + code + " class="+thirs_subcode+">" + name + ".<span class='glyphicon glyphicon-remove delete'></span></li>")
                        inputs.append('<input type="hidden" class="'+code+'" name="'+items+'" value="' + thirs_subcode + '">')
                    }
                } else {
                    if (second_code_atr == $('#allul ul').attr('id').substr(0, 2)) {
                        $('#allul').append("<ul id=" + second_code + "><li id=" + code + " class="+thirs_subcode+">" + name + ".<span class='glyphicon glyphicon-remove delete'></span></li></ul>");

                        inputs.append('<input type="hidden" class="'+second_code+'" name="'+itemtree+'" value="' + parencode + '">')
                        inputs.append('<input type="hidden" class="'+code+'" name="'+items+'" value="' + thirs_subcode + '">')

                    } else {
                        $(this).removeAttr('checked')
                        alert('如果要更换第一级类别，请先删除已选择的小项！')
                    }
                }
            }
        }else{
            var input = $('#inputs').children('input[value='+thirs_subcode+']');
            if ($('.' + thirs_subcode).parent().children('li').length == 1) {
                $('.' + thirs_subcode).parent().remove()
                $('.' + thirs_subcode).remove();
                input.prev().remove();
            }
            $('.' + thirs_subcode).remove();
            input.remove();
        }

    });
    $('#allul').on('click', 'ul li', function () {
        var ele = $(this).attr('class')
        var li = $('.' + ele);
        var input = $('#inputs').children('input[value='+ele+']');
        var lis = li.parent()

        if (lis.children('li').length == 1) {
            lis.remove();
            input.prev().remove();
            $('.checkbox input[data-value=' + ele + ']').removeAttr('checked', '')
        }
        input.remove();
        li.remove();
        $('.checkbox input[data-value=' + ele + ']').removeAttr('checked', '')
    });
    $('#new_type_btn').click(function () {
        $('#allul').html('')
        $('#inputs').html('');
        $('#myModal').modal('hide');
    });
}
;function getfirstType(input_name){
var input_name = input_name || 'mark_category_first';
  $('.first_type_btn').click(function (){

      var $this = $(this);
      var name = $this.text();

      $this.toggleClass('active');
      if($this.hasClass('active')){
          $('<input type="hidden" value="'+name+'" name="'+input_name+'"/>').appendTo($('.mark_cate_inputs'));
          $('.mark_small').remove();
          $(this).closest('form').find('.baocun').removeAttr('disabled','');
      }else{
          $('.mark_cate_inputs').find('input[value='+name+']').remove();
      }
  })
};
//点击空白处消失
/*$content : 非空白区域class
$alert : 隐藏的区域
callback: 隐藏后的回调函数
*/
function hideContent(content,$alert_contnt,callback){
    $(document).click(function (e){
        var $content = $('.'+content);
        if(!$content.is(e.target) && $content.has(e.target).length == 0){
            $('.' + $alert_contnt).hide();
            callback()
        }
    });
};
//全球城市
function wordCountry() {
        var countrys = [["AO", "安哥拉"], ["AF", "阿富汗"], ["AL", "阿尔巴尼亚"], ["DZ", "阿尔及利亚"], ["AD", "安道尔共和国"], ["AI", "安圭拉岛"], ["AG", "安提瓜和巴布达"],
            ["AR", "阿根廷"], ["AM", "亚美尼亚"], ["AU", "澳大利亚"], ["AT", "奥地利"], ["AZ", "阿塞拜疆"], ["BS", "巴哈马"], ["BH", "巴林"], ["BD", "孟加拉国"], ["BB", "巴巴多斯"],
            ["BY", "白俄罗斯"], ["BE", "比利时"], ["BZ", "伯利兹"], ["BJ", "贝宁"], ["BM", "百慕大群岛"], ["BO", "玻利维亚"], ["BW", "博茨瓦纳"], ["BR", "巴西"], ["BN", "文莱"],
            ["BG", "保加利亚"], ["BF", "布基纳法索"], ["MM", "缅甸"], ["BI", "布隆迪"], ["CM", "喀麦隆"], ["CA", "加拿大"], ["CF", "中非共和国"], ["TD", "乍得"], ["CL", "智利"], ["CN", "中国"],
            ["CO", "哥伦比亚"], ["CG", "刚果"], ["CK", "库克群岛"], ["CR", "哥斯达黎加"], ["CU", "古巴"], ["CY", "塞浦路斯"], ["CZ", "捷克"],
            ["DK", "丹麦"], ["DJ", "吉布提"], ["DO", "多米尼加共和国"], ["EC", "厄瓜多尔"], ["EG", "埃及"], ["SV", "萨尔瓦多"], ["EE", "爱沙尼亚"], ["ET", "埃塞俄比亚"], ["FJ", "斐济"], ["FI", "芬兰"], ["FR", "法国"],
            ["GF", "法属圭亚那"], ["GA", "加蓬"], ["GM", "冈比亚"], ["GE", "格鲁吉亚"], ["DE", "德国"], ["GH", "加纳"], ["GI", "直布罗陀"], ["GR", "希腊"], ["GD", "格林纳达"], ["GU", "关岛"],
            ["GT", "危地马拉"], ["GN", "几内亚"], ["GY", "圭亚那"], ["HT", "海地"], ["HN", "洪都拉斯"], ["HK", "香港"], ["HU", "匈牙利"], ["IS", "冰岛"], ["IN", "印度"],
            ["ID", "印度尼西亚"], ["IR", "伊朗"], ["IQ", "伊拉克"], ["IE", "爱尔兰"], ["IL", "以色列"], ["IT", "意大利"], ["JM", "牙买加"], ["JP", "日本"], ["JO", "约旦"],
            ["KH", "柬埔寨"], ["KZ", "哈萨克斯坦"], ["KE", "肯尼亚"], ["KR", "韩国"], ["KW", "科威特"], ["KG", "吉尔吉斯坦"], ["LA", "老挝"], ["LV", "拉脱维亚"], ["LB", "黎巴嫩"],
            ["LS", "莱索托"], ["LR", "利比里亚"], ["LY", "利比亚"], ["LI", "列支敦士登"], ["LT", "立陶宛"], ["LU", "卢森堡"], ["MO", "澳门"], ["MG", "马达加斯加"],
            ["MW", "马拉维"], ["MY", "马来西亚"], ["MV", "马尔代夫"], ["ML", "马里"], ["MT", "马耳他"], ["MU", "毛里求斯"], ["MX", "墨西哥"], ["MD", "摩尔多瓦"], ["MC", "摩纳哥"],
            ["MN", "蒙古"], ["MS", "蒙特塞拉特岛"], ["MA", "摩洛哥"], ["MZ", "莫桑比克"], ["NA", "纳米比亚"], ["NR", "瑙鲁"], ["NP", "尼泊尔"], ["NL", "荷兰"], ["NZ", "新西兰"],
            ["NI", "尼加拉瓜"], ["NE", "尼日尔"], ["NG", "尼日利亚"], ["KP", "朝鲜"], ["NO", "挪威"], ["OM", "阿曼"], ["PK", "巴基斯坦"], ["PA", "巴拿马"], ["PG", "巴布亚新几内亚"],
            ["PY", "巴拉圭"], ["PE", "秘鲁"], ["PH", "菲律宾"], ["PL", "波兰"], ["PF", "法属玻利尼西亚"], ["PT", "葡萄牙"], ["PR", "波多黎各"], ["QA", "卡塔尔"], ["RO", "罗马尼亚"],
            ["RU", "俄罗斯"], ["LC", "圣卢西亚"], ["VC", "圣文森特岛"], ["SM", "圣马力诺"], ["ST", "圣多美和普林西比"], ["SA", "沙特阿拉伯"], ["SN", "塞内加尔"], ["SC", "塞舌尔"],
            ["SL", "塞拉利昂"], ["SG", "新加坡"], ["SK", "斯洛伐克"], ["SI", "斯洛文尼亚"], ["SB", "所罗门群岛"], ["SO", "索马里"], ["ZA", "南非"], ["ES", "西班牙"], ["LK", "斯里兰卡"], ["SD", "苏丹"],
            ["SR", "苏里南"], ["SZ", "斯威士兰"], ["SE", "瑞典"], ["CH", "瑞士"], ["SY", "叙利亚"], ["TW", "台湾省"], ["TJ", "塔吉克斯坦"], ["TZ", "坦桑尼亚"], ["TH", "泰国"], ["TG", "多哥"],
            ["TO", "汤加"], ["TT", "特立尼达和多巴哥"], ["TN", "突尼斯"], ["TR", "土耳其"], ["TM", "土库曼斯坦"], ["UG", "乌干达"], ["UA", "乌克兰"], ["AE", "阿拉伯联合酋长国"],
            ["GB", "英国"], ["US", "美国"], ["UY", "乌拉圭"], ["UZ", "乌兹别克斯坦"], ["VE", "委内瑞拉"], ["VN", "越南"], ["YE", "也门"], ["YU", "南斯拉夫"], ["ZW", "津巴布韦"], ["ZR", "扎伊尔"],
            ["ZM", "赞比亚"]];
        var html = '';
        countrys.forEach(function (item) {
            var $item = $(item);
            var $value = $item[0];
            var $data = $item[1];
            html += '<option data-content="'+$data+'" data-value="' + $value + '">' + $data + '</option>';
            $('.wordCountry').html(html);
            $('.wordCountry option[data-value=CN]').attr('selected', '');
        })
    };

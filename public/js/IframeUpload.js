/**
 * Created by wangshubin on 14-12-26.
 * 按钮需要使用div span a等可以包含内容的标签
 */

;(function ($, window, document, undefined) {
    //定义Beautifier的构造函数
    var UploadObj = function (ele, opt) {
        this.$element = ele,
        this.defaults = {
            'url': '',
            'ossName': 'default',
            'openPositionInterval':false,
            'multiple':true,
            'xsrfName':"_xsrf",
            'xsrfValue':"",
            'beforeSubmit':function(){return true},// 返回true继续提交，返回false阻止提交，这个方法还有待完善，可以传入一些参数，比如文件大小，文件名等，作一些提交之前的前端校验，目前用户可以自己获取数据，做校验。
            'success':function(){},
            'accept':""// image/jpeg,image/pjpeg,image/bmp,image/png,image/x-png
        },
        this.options = $.extend({}, this.defaults, opt);
        // 处理默认值
        if(!this.options.xsrfValue){
            this.options.xsrfValue = $("input[name="+this.options.xsrfName+"]").val();
        }
        // 获取btn名称
        if(this.$element[0].tagName=="INPUT"){
            this.options.elementLabel = this.$element.val();
        }else{
            this.options.elementLabel = this.$element.text();
        }

    }
    //定义Beautifier的方法
    UploadObj.prototype = {
        init: function () {
            //声明变量,防止this乱用
            var options = this.options;
            var $element = this.$element;
            $element.data("options",options);
            //body 中插入所需HTML
            var upload_form = $element.data("upload_form");
            //获取$element的id如果不存在使用时间戳作为id
            var eleId = $element.attr("id");
            if(!eleId) $element.attr("id",new Date().getTime());
            if(!upload_form){
                var multiple = options.multiple?'multiple="multiple"':'';
                var form_html = '<form id="form_'+eleId+'" action="'+options.url+'"  style="" encType="multipart/form-data" method="post" target="hidden_frame">'
                        +'<div>'
                            +'<input type="hidden" value="'+options.xsrfValue+'" name="'+options.xsrfName+'" />'
                            +'<input type="hidden" value="'+options.ossName+'" name="ossName" />'
                            +'<input type="hidden" value="'+options.multiple+'" name="multiple" />'
                            +'<input type="hidden" value="'+eleId+'" name="eleId" />'
                            +'<input type="file" name="fileData" accept="'+options.accept+'" '+multiple+' />'
                        +'</div>'
                    +'</form>';
                //需要加入body 否则火狐无效
//                $element.html(form_html);
                $("body").append(form_html);
                upload_form = $("#form_"+eleId);
                this.setFilePosition();
                //定时器的作用：按钮的位置可能因为插入图片等原因位置发生改变，file就会错位，使用定时器，定时刷新file位置。
                if(options.openPositionInterval){
                    setInterval(function (){
                        var eleOffset = $element.offset();
                        var btn_top = eleOffset.top;
                        var btn_left = eleOffset.left;
                        upload_form.css({
                            "left":btn_left+"px",
                            "top":btn_top+"px"
                        });
                    } ,300);
                }

                //修改样式
                upload_form.find("div").css({
                    "position":"relative",
                    "width":"100%",
                    "height":"100%",
                    "overflow":"hidden"
                });
                upload_form.find("input[type=file]").css({
                    "position":"absolute",
                    "cursor":"pointer",
                    "left":"0",
                    "top":"0",
                    "width":"100%",
                    "height":"100%",
                    "opacity":"0",
                    "-ms-filter":"alpha(opacity=0)",
                    "filter":"alpha(opacity=0)"
                });
                $element.data("upload_form",upload_form);
            }
            if($("#hidden_frame").length<=0){
                $("body").append('<iframe name="hidden_frame" id="hidden_frame" style="display:none"></iframe>');
            }

            $("#form_"+eleId).on("change","input[type=file]",function(){
                var can_submit = options.beforeSubmit($(this));
                if(can_submit){
                    upload_form.submit();
                }
            });
            return $element;
        },
        setFilePosition:function(){
            var options = this.options;
            var $element = this.$element;
            var btn_width = $element.outerWidth(true);
            var btn_height = $element.outerHeight(true);
            var btn_top = $element.offset().top;
            var btn_left = $element.offset().left;
            var eleId = $element.attr("id");
            var upload_form = $("#form_"+eleId);
            upload_form.css({
//                "border":"1px solid #000",
                "width":btn_width+"px",
                "height":btn_height+"px",
                "position":"absolute",
                "left":btn_left+"px",
                "top":btn_top+"px"
            })
        }
    }
    //在插件中使用Beautifier对象
    $.fn.wIFrameUpload = function (options,data) {
        //创建Beautifier的实体
        var uploadObj = new UploadObj(this, options);
        //调用其方法
        if(typeof(options)=="string"){
            // 需要init方法被调用之后。
            switch(options){
                case "success":
                    //清空file，否则不能连续上传同一个文件
                    var eleId = this.attr("id");
                    var $form = $("#form_"+eleId);
                    var multiple = options.multiple?'multiple="multiple"':'';
                    //删除原先的input 再新加一个input
                    $form.find("input[type=file]").remove();
                    $form.find("div").append('<input type="file" name="fileData" accept="'+options.accept+'" '+multiple+' />')
                    $form.find("input[type=file]").css({
                        "position":"absolute",
                        "cursor":"pointer",
                        "left":"0",
                        "top":"0",
                        "width":"100%",
                        "height":"100%",
                        "opacity":"0",
                        "-ms-filter":"alpha(opacity=0)",
                        "filter":"alpha(opacity=0)"
                    });
                    //执行回调函数
                    this.data("options").success(data);
                    break;
                default:
                    alert("No such method!");
                    return this
            }
            return this
        }else{
            return uploadObj.init();
        }

    }
})(jQuery, window, document);

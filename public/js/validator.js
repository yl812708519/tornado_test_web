/*校验规则
默认规则
(1)required:true           必输字段
(2)remote:"check.php"      使用ajax方法调用check.php验证输入值
(3)email:true              必须输入正确格式的电子邮件
(4)url:true                必须输入正确格式的网址
(5)date:true               必须输入正确格式的日期 日期校验ie6出错，慎用
(6)dateISO:true            必须输入正确格式的日期(ISO)，例如：2009-06-23，1998/01/22 只验证格式，不验证有效性
(7)number:true             必须输入合法的数字(负数，小数)
(8)digits:true             必须输入整数
(9)creditcard:true         必须输入合法的信用卡号
(10)equalTo:"#field"       输入值必须和#field相同
(11)accept:                输入拥有合法后缀名的字符串（上传文件的后缀）
(12)maxlength:5            输入长度最多是5的字符串(汉字算一个字符)
(13)minlength:10           输入长度最小是10的字符串(汉字算一个字符)
(14)rangelength:[5,10]     输入长度必须介于 5 和 10 之间的字符串")(汉字算一个字符)
(15)range:[5,10]           输入值必须介于 5 和 10 之间
(16)max:5                  输入值不能大于5
(17)min:10                 输入值不能小于10

扩展规则：
(1)zipCode:true            请正确填写您的邮政编码
(2)date:true               您输入的日期有误
(3)mobile:true             手机号码不正确
(4)userName:true           已存在
(5)
(6)
(7)
(8)
(9)
(10)

使用方法：
(1)class="required"
(2)class="{required:true,minlength:5}"

* */
$(function(){
    // 邮政编码验证
    jQuery.validator.addMethod("zipCode", function(value, element) {
        var tel = /^[0-9]{6}$/;
        return this.optional(element) || (tel.test(value));
    }, "请正确填写您的邮政编码");



    // 日期验证 日期格式：YYYY-MM-DD
    jQuery.validator.addMethod("date", function(value, element) {
        // 简单判断格式
        var tel = /^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]$/;
        if(!tel.test(value)){
            return this.optional(element) || (tel.test(value));
        }
        // 判断日期，平闰年支持
        tel = /(([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29)/;
        return this.optional(element) || (tel.test(value));
    }, "您输入的日期有误");

    //手机号验证
    jQuery.validator.addMethod("mobile", function(value, element) {
        var tel = /^1[3|4|5|7|8][0-9]\d{8,8}$/;
        return this.optional(element) || (tel.test(value));
    }, "手机号码不正确");

    //远程用户名验证
    jQuery.validator.addMethod("userName", function(value, element) {
//                console.log(value);
        var user_id = $("#user_id").val();
        var result = 0;
        $.ajax({
            type: "get",
            async:false,
            url:"/human/staff/check_account.json",
            data:{user_account:value,user_id:user_id},
            success: function(data, textStatus){
                result = data.result;
            }
        });
        return this.optional(element) ||!result;
    }, "已存在");

    $(".common_validate").validate({
        onkeyup:false,//敲击键盘时不进行验证，否则远程验证会频繁请求数据
        errorPlacement: function(error, element) {
            if(error.html()){
                //console.log("有错："+error.html());
                element.parents(".input-group").addClass("has-error");
                element.parents(".input-group").find('div.input-error').remove();
                element.parents(".input-group").append('<div class="input-error">'+error.html()+'</div>');
            }else{
//                        console.log("正确"+error.html());
                element.parents(".input-group").removeClass("has-error");
                element.parents(".input-group").find('div.input-error').remove();
            }
        },
        success:function(error){
            //这个success函数必须写，否则上面的正确分支不执行，原因未知。
            /*console.log("success");
            console.log(error);*/
        }
    });//end of $(".common_validate").validate(
})
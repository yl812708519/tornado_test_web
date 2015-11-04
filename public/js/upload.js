        function upload(json){
            /*
             *多文件上传文档说明
             * .loadingImgUrl指定上传中的图片
             *.elementId是给哪个按钮加多文件上传
             *.attachmentList 后台返回前端的数据（是这个人已经在服务存在的数据）
             * .tipId是插件给你返回的你已经上传文件的数量
             *返回格式为
             *download_url: "http://eking-test.oss-cn-beijing.aliyuncs.com/11/my/i14q8tsd7ou.jpg"
             *file_size: "10"
             *id: "12"
             *name: "files-15-qn-i14lq7ut7ou (2).jpg"
             *operator_name: "邵振兴"
             *oss_url: "11/my/i14q8tsd7ou.jpg"
             *upload_time: "2014-10-11 16:54:42"
             *.uploadUrl 是上传文件的提交的url地址
             *点击上传之后前端给后台的数据格式为
             *上传成功后后台返回格式必须为{"status": 1, "oss_url": "files/n/4w/i178614n7ou.jpg", "upload_time": "2014-10-13 10:51:57", "operator_id": 9, "operator_name": "\u90b5\u632f\u5174", "download_url": "http://eking-test.oss-cn-beijing.aliyuncs.com/files/n/4w/i178614n7ou.jpg"}
             *前台会把后台所需要的数据保存在当前表单提交页面上，返回数据name是files格式是files/1d/4z/i17861dp7ou.jpg</>2014-10-13 10:51:58</>9</>files-1r-hd-i14q8ear7ou (1).jpg</>9966
             *.deleteUrl 是删除文件时提交的url地址 默认是当前url里的delete方法
             *删除文件的时候前端会把当前的id给后台返回回去
             * .del 值为1的时候下载和删除按钮是隐藏的，值为0的时候是显示的默认是0
             * .showType 值为1的时候不能上传文件，不能删除文件，只有下载文件的功能 ，默认为0 是关闭该功能的
             **/
         json.showType=json.showType||0;
         if(json.showType==0){
            $('body').append('<div class="modal fade" id="emailModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" ><div class="modal-dialog" style="width:80%" ><div class="container span7 offset3 well" style="width:80%"><form id="uploadForm" class="form-horizontal" enctype="multipart/form-data" method="post" action="javascript:void(0);"><fieldset><legend>文件上传<button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button></legend><div class="control-group"><label class="control-label" for="fileToUpload" >选择文件(支持多选,10M以上禁止上传):</label><div class="controls" ><div  class="btn btn-primary" style="width:100px;height:35px;margin-bottom:5px;"><span>添加文件</span><input type="file" name="fileToUpload" id="fileToUpload" multiple="multiple" style="opacity:0;width:80px;position:relative;top:-20px;" ></div></div></div><div class="file-list" id="fileList" style="height:400px;overflow-y:scroll;border-bottom:1px solid #e3e3e3;border-top:1px solid #e3e3e3"></div><div class="form-actions text-left"><button type="button" class="btn btn-primary disabled" id="subBtn" style="margin-top:10px;">立即上传</button><button type="button" class="btn btn-primary pull-right" style="margin-top:10px;" data-dismiss="modal">完成</button></div></fieldset></form></div></div></div>');
         }else{
            $('body').append('<div class="modal fade" id="emailModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" ><div class="modal-dialog" style="width:80%" ><div class="container span7 offset3 well" style="width:80%"><form id="uploadForm" class="form-horizontal" enctype="multipart/form-data" method="post" action="javascript:void(0);"><fieldset><legend>文件上传<button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button></legend><div class="file-list" id="fileList" style="height:400px;overflow-y:scroll"></div></fieldset></form></div></div></div>');
         }
        //将bootcss弹出框html代码插入页面中
        var attachments=json.attachmentList;
        var $class='#'+json.elementId;
        var $fileList = $('#fileList');
        var html1='';
        var nums=0;
        var inum=0;
        var inames=[];
         if(attachments){
             nums=attachments.length;
             inum=attachments.length;
             for(var i=0;i<attachments.length;i++){
                 var filesize1=0;
                 if (attachments[i].file_size > 1024 * 1024) {
                        filesize1 = (Math.round(attachments[i].file_size * 100 / (1024 * 1024)) / 100).toString() + 'MB';
                    } else {
                        filesize1 = (Math.round(attachments[i].file_size * 100 / 1024) / 100).toString() + 'KB';
                    }
                 html1 += '<div class="file-item well">'
                            +'<div class="shanchuan">'
                                +'<span class="span2" style="overflow:hidden;text-overflow:ellipsis;white-space:nowrap;width:200px;">文件名：'+ attachments[i].name +'</span>'
                                +'<span class="glyphicon glyphicon-ok-sign" style="color:#008000;margin-left:5px"></span>'
                                +'<span class="pull-right" >'
                                    +'<span class="glyphicon glyphicon-trash"  title="删除" oid="'+attachments[i].id+'"/>'
                                    +'<a style="margin-left:10px" class = "down_file glyphicon glyphicon-download-alt" href="'+attachments[i].download_url+'" title="下载" ></a>'
                                +'</span><br/>'
                                +'<span class="span2" style="font-size:12px;color:#6e6e6e;margin-right:20px;">文件大小：'+filesize1+'</span>'
                                +'<span class="utime" style="font-size:12px;color:#6e6e6e;margin-right:20px;">上传时间：'+attachments[i].upload_time+'</span>'
                                +'<span class="uren"  style="font-size:12px;color:#6e6e6e;margin-right:20px;">上传人：'+attachments[i].operator_name+'</span>'
                            +'</div>'
                          +'</div>';
                inames.push(attachments[i].name);
             };
             $fileList.append(html1);
             $('#'+json.tipId).html('已上传'+inum+'个');
         }
          $($class).click(function(){
            //上传文件按钮点击事件
            $("#emailModal .cus_email").remove();
            $('#emailModal').modal('show');
        });
            var str=null;
            var chongfu=[];
            var files = [];
            var $uploadForm = $('#uploadForm');
            var $fileToUpload = $('#fileToUpload');
            var index = 0;
            var isize=[];
            var cishu=0;
            var $shan=$('.glyphicon-trash');
            function fileSelected(){
                var fs = $fileToUpload.get(0).files;
                var html = '';
                for(var i = 0; i < fs.length; i++) {
                    var file = fs[i];
                    var fileSize = 0;
                    if (file.size > 1024 * 1024){
                        fileSize = (Math.round(file.size * 100 / (1024 * 1024)) / 100).toString() + 'MB';
                    } else {
                        fileSize = (Math.round(file.size * 100 / 1024) / 100).toString() + 'KB';
                    }
                    if(inames.join("").indexOf(file.name)!=-1){
                        chongfu.push(file.name);
                    }else{
                        html += '<div class="file-item well">'
                                    +'<div class="shanchuan">'
                                        +'<span class="span2" style="overflow:hidden;text-overflow:ellipsis;white-space:nowrap;width:200px;">文件名：'+ file.name +'</span>'
                                        +'<img style="display:none;width:14px;height:16px;" class="oupload" src="'+json.loadingImgUrl+'" />'
                                        +'<span class="glyphicon glyphicon-ok-sign" style="display:none;color:#008000;margin-left:5px"></span>'
                                        +'<span class="glyphicon glyphicon-remove-sign" style="color:red;display:none;margin-left:5px"></span>'
                                        +'<span class="pull-right" style="display:none">'
                                            +'<span class="glyphicon glyphicon-trash" title="删除"/>'
                                            +'<a class = "down_file glyphicon glyphicon-download-alt" href="###" title="下载" style="margin-left:10px"></a>'
                                        +'</span>'
                                        +'<span class="pull-right deleteding" oid='+files.length+'>'
                                            +'<span class="glyphicon glyphicon-remove">'
                                            +'</span>'
                                        +'</span><br/>'
                                        +'<span class="span2" style="font-size:12px;color:#6e6e6e;margin-right:20px;">文件大小：'+ fileSize +'</span>'
                                        +'<span class="utime" style="font-size:12px;color:#6e6e6e;margin-right:20px;"></span>'
                                        +'<span class="uren"  style="font-size:12px;color:#6e6e6e;margin-right:20px;"></span>'
                                    +'</div>'
                                +'</div>';
                        inames.push(file.name);
                        isize.push(file.size);
                        files.push(file);
                    }
                }
                $fileList.append(html);
                $('.deleteding').click(function(){
                        files.splice($(this).parent().parent().index()-nums,1);
                        isize.splice($(this).parent().parent().index()-nums,1);
                        inames.splice($(this).parent().parent().index(),1);
                        chongfu.splice($(this).parent().parent().index(),1);
                        $(this).parent().parent().remove();
                        console.log(inames);
                        console.log(chongfu);
                        if(files.length<1){
                       $('#subBtn').get(0).className="btn btn-primary disabled";
                    }
                       cishu++;
                  }
                );
                if(chongfu.length>=1){
                    wModalDialog({
                      content:'<div>以下文件已添加，请不要重复添加</div>'+chongfu.join('</br>'),
                      showAnimate:true,
                      type:"alert"
                    });
                    chongfu.length=0;
                }
                if(files.length>=1){
                   $('#subBtn').get(0).className="btn btn-primary";
                }
                $cuowu=$('.glyphicon-remove-sign');
                $utime = $('.utime');
                $uren = $('.uren');
                $pullright=$('.pull-right');
                $oupload=$('.oupload');
                $chengong=$('.glyphicon-ok-sign');
            }
            function uploadFile() {
                var xhr = new XMLHttpRequest();
                xhr.addEventListener("load", uploadComplete,false);
                xhr.addEventListener("error", uploadFailed,false);
                xhr.addEventListener("abort", uploadCanceled,false);
                xhr.open("POST",json.uploadUrl);
                var fd = new FormData();
                var _xsrf = getCookie("_xsrf");
                fd.append("_xsrf",_xsrf);
                fd.append("file", files[index]);
                fd.append("file_name",inames[index]);
                fd.append("file_size",isize[index]);
                fd.append("module_name",json.modelName);
                fd.append("entity_id",json.entityId);
                xhr.send(fd);
            }
             //删除
             $shan.click(function(){
                 var $this=$(this);
                 var params = {};
                    params.id =  $(this).attr('oid');;
                    params._xsrf = getCookie("_xsrf");
                    $.ajax({
                        type: "post",
                        async: false,
                        url:json.deleteUrl,
                        data: params,
                        beforeSend: function (XMLHttpRequest) {
                            $(".loading").show();
                        },
                        success:function (data, textStatus){
                            if(data.result==1){
                                wModalDialog({
                                //title:"测试标题",
                                content:"删除成功！",
                                showAnimate:true,
                                type:"alert"
                             });
                        inames.splice($this.parent().parent().parent().index(),1);
                        chongfu.splice($this.parent().parent().parent().index(),1);
                            }
                            $this.parent().parent().parent().remove();
                        },
                        complete: function (XMLHttpRequest, textStatus) {
                            $(".loading").hide();
                        },
                        error: function () {
                             wModalDialog({
                                //title:"测试标题",
                                content:"删除失败！",
                                showAnimate:true,
                                type:"alert"
                             });
                         }
                });
            })
            function uploadComplete(evt){
                if(evt.target.status>=200 && evt.target.status<300 || evt.target.status==304){
                    var result = eval('(' + evt.target.responseText + ')');
                    console.log(index+','+nums);
                    if (result['status'] == 1) {
                        //成功了
                        $($pullright.get(index + nums)).find(".down_file").attr("href", result["download_url"]);
                        $chengong.get(index+nums+cishu).style.display = "inline-block";
                        $(".oupload:eq(0)").remove();
                        if (!attachments){
                            $pullright.get(index + nums).style.display = "inline-block";
                        }
                        $utime.get(index + nums+cishu).innerHTML = "上传时间：" + result['upload_time'];
                        $uren.get(index + nums+cishu).innerHTML = "上传人：" + result['operator_name'];
                        inum++;
                    } else {
                        //失败了
                        $(".oupload:eq(0)").remove();
                        $cuowu.get(index + nums+cishu).style.display = "inline-block";
                        $cuowu.get(index + nums+cishu).innerHTML = "请上传10M以下的文件";
                    }
                }else {
                   $(".oupload:first").next().next().css('display','inline-block');
                   $(".oupload:first").next().next().html('网络错误，请重新上传');
                   $(".oupload:first").remove();
                }
                $('#'+json.tipId).html('已上传' +(inum)+ '个');
                if (index === files.length - 1) {
                        console.log('全部上传完毕');
                        index=files.length;
                        $('#subBtn').get(0).className="btn btn-primary disabled";
                        return;
                }
                index++;
                uploadFile();
            };
            if(json.showType!=0){
                $shan.css('display', 'none');
            }
            $fileToUpload.change(function() {
                fileSelected();
            });
            $('#subBtn').click(function() {
                uploadFile();
                $('.deleteding').css('display','none');
                $('.oupload').css('display','inline-block');
            });
            function uploadFailed(evt) {
                alert("网络错误，请刷新页面重新上传");
            }
            function uploadCanceled(evt) {
                alert("网络错误，请刷新页面重新上传");
            }
           //多文件上传结束
        };

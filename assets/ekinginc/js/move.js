/****运动框架开始***************************************************************************************/
//取样式
function getStyle(obj, name) {
    return window.getComputedStyle ? getComputedStyle(obj, false)[name] : obj.currentStyle[name];
}
//运动
function move(obj, json, options) {
    //缺省设置
    options = options || {};
    options.time = options.time || 300;
    options.type = options.type || 'ease-out';
    //计算步数
    var start = {};
    var dis = {};
    var count = Math.round(options.time / 30);
    var n = 0;
    //取起点，算距离
    for (var i in json) {
        start[i] = parseFloat(getStyle(obj, i));
        dis[i] = parseInt(json[i]) - start[i];
    }
    //每隔三十毫秒重新计算坐标
    clearInterval(obj.timer);
    obj.timer = setInterval(function () {
        n++;
        for (var i in json) {
            switch (options.type) {
                case 'linear':
                    var cur = start[i] + dis[i] * n / count;
                    break;
                case 'ease-in':
                    var a = n / count;
                    var cur = start[i] + dis[i] * a * a * a;
                    break;
                case 'ease-out':
                    var a = 1 - n / count;
                    var cur = start[i] + dis[i] * (1 - a * a * a);
                    break;
            }

            if (i == 'opacity') {
                obj.style.opacity = cur;
                obj.style.filter = 'alpha(opacity:' + cur * 100 + ')';
            } else {
                obj.style[i] = cur + 'px';
            }
        }

        if (n == count) {
            clearInterval(obj.timer);
        }
    }, 30)
}//end
/****运动框架结束***************************************************************************************/
/****弹性运动开始***************************************************************************************/
function elastic(obj, name, value) {
    //存储坐标
    obj.speed = obj.speed || 0;
    obj.cur = obj.cur || 0;
    obj.timer = null;
    //elastic
    clearInterval(obj.timer);
    obj.timer = setInterval(function () {
        obj.speed += (value - obj.cur) / 5;
        obj.speed *= 0.7;
        obj.cur += obj.speed;
        obj.style[name] = Math.round(obj.cur) + 'px';

        if (Math.round(obj.cur) == value && Math.round(obj.speed) == 0) {
            clearInterval(obj.timer);
        }
    }, 30);
}
/****弹性运动结束**********************************************************************************/
/****拖拽开始*********************************************************************************/
function drag(obj) {
    obj.onmousedown = function (ev) {
        ev = ev || event;
        var disX = ev.clientX - obj.offsetLeft;
        var disY = ev.clientY - obj.offsetTop;
        document.onmousemove = function (ev) {
            ev = ev || event;
            obj.style.left = ev.clientX - disX + 'px';
            obj.style.top = ev.clientY - disY + 'px';
        };
        document.onmouseup = function () {
            document.onmousemove = null;
            document.onmouseup = null;
            obj.releaseCapture && obj.releaseCapture();
        };
        obj.setCaputure && obj.setCaputure();
        return false;
    };
}
/****拖拽结束**********************************************************************************/
/****投掷运动开始**********************************************************************************/
function toss(obj) {
    obj.onmousedown = function (ev) {
        this.style.opacity = '1';
        this.style.filter = 'alpha(opacity:100)';
        ev = ev || event;
        redOnlyIndex = window.redOnlyIndex || 0;
        redOnlyIndex++;
        obj.style.zIndex = redOnlyIndex;
        var preX = obj.offsetLeft;
        var preY = obj.offsetTop;
        var disX = ev.clientX - preX;
        var disY = ev.clientY - preY;
        var speedX = 0;
        var speedY = 0;
        clearInterval(obj.timer);

        document.onmousemove = function (ev) {


            ev = ev || event;
            var l = ev.clientX - disX;
            var t = ev.clientY - disY;
            speedX = l - preX;
            speedY = t - preY;
            preX = l;
            preY = t;
            if (l < 0) {
                l = 0;
            } else if (l > document.documentElement.clientWidth - obj.offsetWidth) {
                l = document.documentElement.clientWidth - obj.offsetWidth;
            } else if (t < 0) {
                t = 0;
            } else if (t > document.documentElement.clientHeight - obj.offsetHeight) {
                t = document.documentElement.clientHeight - obj.offsetHeight;
            }
            obj.style.left = l + 'px';
            obj.style.top = t + 'px';
        };

        document.onmouseup = function () {
            document.onmousemove = null;
            document.onmouseup = null;
            clearInterval(obj.timer);
            obj.timer = setInterval(function () {
                speedY += 3;
                var l = obj.offsetLeft;
                var t = obj.offsetTop;
                l += speedX;
                t += speedY;
                if (t > document.documentElement.clientHeight - obj.offsetHeight) {
                    t = document.documentElement.clientHeight - obj.offsetHeight;
                    speedY *= -0.8;
                    speedX *= 0.8;
                } else if (t < 0) {
                    t = 0;
                    speedY *= -0.8;
                    speedX *= 0.8;
                } else if (l > document.documentElement.clientWidth - obj.offsetWidth) {
                    l = document.documentElement.clientWidth - obj.offsetWidth;
                    speedX *= -0.8;
                    speedY *= 0.8;
                } else if (l < 0) {
                    l = 0;
                    speedX *= -0.8;
                    speedY * +0.8;
                }
                if (Math.abs(speedX) < 1) {
                    speedX = 0;
                }
                if (Math.abs(speedY) < 1) {
                    speedY = 0;
                }
                if ((t == document.documentElement.clientHeight - obj.offsetHeight) && speedX == 0 && speedY == 0) {
                    clearInterval(obj.timer);
                    obj.style.opacity = '0.3';
                    this.style.filter = 'alpha(opacity:30)';
                }
                obj.style.left = l + 'px';
                obj.style.top = t + 'px';
            }, 30);
            obj.releaseCapture && obj.releaseCapture();
        };
        obj.setCapture && obj.setCapture();
        return false;
    };
}
/****投掷运动结束**********************************************************************************/
/****碰撞检测开始**********************************************************************************/
function collTest(obj1, obj2) {
    var l1 = obj1.offsetLeft;
    var t1 = obj1.offsetTop;
    var r1 = l1 + obj1.offsetWidth;
    var b1 = t1 + obj1.offsetHeight;

    var l2 = obj2.offsetLeft;
    var t2 = obj2.offsetTop;
    var r2 = l2 + obj2.offsetWidth;
    var b2 = t2 + obj2.offsetHeight;


    if (r1 < l2 || b1 < t2 || l1 > r2 || t1 > b2) {
        //没有碰上
        return false;
    } else {
        //碰上了
        return true;
    }
}
/****碰撞检测结束**********************************************************************************/
/****滚轮事件绑定开始**********************************************************************************/
function addMouseWheel(obj, fn) {
    if (navigator.userAgent.toLowerCase().indexOf('firefox') > -1) {
        obj.addEventListener('DOMMousescroll', fnWheel, false);//ff
    } else {
        obj.onmousewheel = fnWheel;
    }

    function fnWheel(ev) {
        ev = ev || event;
        var bDown = ev.wheelDelta ? ev.wheelDelta < 0 : ev.detail > 0;

        fn && fn(bDown);
    }
}
/****滚轮事件绑定结束**********************************************************************************/

function move_img(id, sort_id, del) {
    var oWrap = document.getElementById(id);
    var aLi = oWrap.children;
    var aPos = [];
    var str = '';
    for (var i = 0, len = aLi.length; i < len; i++) {
        aLi[i].index = i;
        aPos.push({left: aLi[i].offsetLeft, top: aLi[i].offsetTop});
        aLi[i].style.left = aPos[i].left + 'px';
        aLi[i].style.top = aPos[i].top + 'px';
    }
    for (var i = 0, len = aLi.length; i < len; i++) {
        aLi[i].style.position = 'absolute';
        aLi[i].style.margin = '0';
    }
    for (var i = 0, len = aLi.length; i < len; i++) {
        drag(aLi[i]);
    }

    for (var i = 0; i < aLi.length; i++) {
        $('#' + id).children().eq(i).attr('index', aLi[i].index);
    }

    function drag(obj) {
        obj.onmousedown = function (ev) {
            str = '';
            ev = ev || event;
            var disX = ev.clientX - obj.offsetLeft;
            var disY = ev.clientY - obj.offsetTop;
            document.onmousemove = function (ev) {
                ev = ev || event;
                obj.style.left = ev.clientX - disX + 'px';
                obj.style.top = ev.clientY - disY + 'px';

                var oNear = findNearest(obj);

                if (oNear && oNear != obj) {
                    var n = obj.index;
                    var m = oNear.index;
                    if (n < m) {
                        for (var i = 0; i < aLi.length; i++) {
                            if (aLi[i].index >= n + 1 && aLi[i].index <= m) {
                                aLi[i].index--;
                                move(aLi[i], aPos[aLi[i].index]);
                            }
                        }
                    } else {
                        for (var i = 0; i < aLi.length; i++) {
                            if (aLi[i].index >= m && aLi[i].index <= n - 1) {
                                aLi[i].index++;
                                move(aLi[i], aPos[aLi[i].index]);
                            }
                        }
                    }
                    obj.index = m;
                }
            };
            document.onmouseup = function () {
                document.onmousemove = null;
                document.onmouseup = null;
                move(obj, aPos[obj.index]);
                obj.releaseCapture && obj.releaseCapture();
                for (var i = 0; i < aLi.length; i++) {
                    $('#' + id).children().eq(i).attr('index', aLi[i].index);
                    if (str) {
                        str += (',' + aLi[i].index);
                    } else {
                        str += ('' + aLi[i].index);
                    }
                }
                $('#' + sort_id).attr('value', str);
            };
            obj.setCapture && obj.setCapture();
            return false;
        };
    }


    function collTest(obj1, obj2) {
        var l1 = obj1.offsetLeft;
        var t1 = obj1.offsetTop;
        var r1 = obj1.offsetLeft + obj1.offsetWidth;
        var b1 = obj1.offsetTop + obj1.offsetHeight;

        var l2 = aPos[obj2.index].left;
        var t2 = aPos[obj2.index].top;
        var r2 = aPos[obj2.index].left + obj2.offsetWidth;
        var b2 = aPos[obj2.index].top + obj2.offsetHeight;

        if (r1 < l2 || l1 > r2 || b1 < t2 || t1 > b2) {
            return false;
        }
        else {
            return true;
        }
    }

    //算距离
    function getDis(obj1, obj2) {
        var a = obj1.offsetLeft - aPos[obj2.index].left;
        var b = obj1.offsetTop - aPos[obj2.index].top;

        return Math.sqrt(a * a + b * b);
    }

    //找到最近——1.碰上 && 2.最近
    function findNearest(obj) {
        var iMin = 9999999;
        var iMinIndex = -1;

        for (var i = 0; i < aLi.length; i++) {
            if (collTest(obj, aLi[i])) {
                var dis = getDis(obj, aLi[i]);

                if (dis < iMin) {
                    iMin = dis;
                    iMinIndex = i;
                }
            }
        }

        if (iMinIndex == -1)	//没碰上
        {
            return null;
        }
        else {
            return aLi[iMinIndex];
        }
    }

    $('.delete_img').unbind();
    $('.delete_img').click(function () {
        var sort_num = $(this).parents('.file').attr('index');
        var old_num = $(this).parents('.file').index();
        $("#files_img input").eq(old_num).remove();
        var arr = $('#sequence').val().split(',');
        var new_str = '';
        aLi = '';
        aLi = oWrap.children;
        for (var i = 0; i < arr.length; i++) {
            if (arr[i] == sort_num) {
                continue;
            }
            if (arr[i] > sort_num) {
                new_str += ',' + (arr[i] - 1);
                aLi[i].index = (arr[i] - 1);
            } else {
                new_str += ',' + arr[i];
                aLi[i].index = arr[i];
            }
            if (arr[i] > sort_num) {
                $('#files_img .file').eq(i).attr('index', ($('#files_img .file').eq(i).attr('index') - 1));
            }
        }
        new_str = new_str.substring(1);
        var arr1 = new_str.split(',');
        $(this).parents('.file').remove();
        $('#sequence').attr('value', new_str);
        for (var i = 0; i < aLi.length; i++) {
            move(aLi[i], aPos[arr1[i]]);
        }
        ;
        if ($('#files_img .file').length < 5) {
            $('#iFrameUpload_img').removeAttr('disabled');
        }
        if ($('#files_img .file').length < 1) {
            $('#files_img').css('display', 'none');
        }
    });
};
function moves(patent_sale_img, options) {
    $("#iFrameUpload_img").wIFrameUpload({
        url: "/iframe_upload",
        ossName: "yestar",
        openPositionInterval: true,
        beforeSubmit: function ($file_input) {
            var file_name = $file_input.val();
            var arr = ["gif", "jpeg", "jpg", "bmp", "png"];
            if (!RegExp("\.(" + arr.join("|") + ")$", "i").test(file_name.toLowerCase())) {
                alert('选择文件错误,图片类型必须是(gif,jpeg,jpg,bmp,png)中的一种');
                return false;
            }
            if ($('#iFrameUpload_img').attr('disabled') == 'disabled'){
                return false;
            }
            $('#files_img .file').removeAttr("style");
            $('#iFrameUpload_img').html('正在上传中...');
            $('#iFrameUpload_img').attr('disabled', 'disabled');
            $('#files_img').append('<div class="file" state="load">'
                + '<div style="position:relative">'
                + '<span class="glyphicon glyphicon-remove delete_img" style="position:absolute;top:-12px;left:87px;color:red"></span>'
                + '<img class="imgs" style="width:100px;height:100px;" src="/s/img/load.gif">'
                + '</div>'
                + '</div>');
            $('#files_img').css('display', 'block');
            return true;//返回false 阻止提交
        },
        success: function (data) {
            if (data.status == 1) {
                var str = '';
                $('#files_img').find('div[state=load]').remove();
                $('#files_img').append('<div class="file" state="success">'
                    + '<div style="position:relative">'
                    + '<span class="glyphicon glyphicon-remove delete_img" style="position:absolute;top:-12px;left:87px;color:red"></span>'
                    + '<img class="imgs" style="width:100px;height:100px;" src="' + data.downloadUrl + '">'
                    + '<input type="hidden" name="' + patent_sale_img + '" value="' + data.ossUrl + '">'
                    + '</div>'
                    + '</div>');
                if ($("#files_img input").length > 4) {
                    $('#iFrameUpload_img').attr('disabled', 'disabled');
                } else {
                    $('#iFrameUpload_img').removeAttr('disabled');
                }
                $('#iFrameUpload_img').html('请选择图片上传');
                if ($("#files_img input").length == 1) {
                    $('#files_img').css('display', 'block');
                }
                if (options) {
                    $('#' + options.btn_id).attr('value', '111');
                    var form_validator = $('#' + options.form_id).data('bootstrapValidator');
                    form_validator.revalidateField(options.check_name);
                }
                move_img('files_img', 'sequence');
                $('#files_img .file').css("cursor", "pointer");
                for (var i = 0; i < $('#files_img .file').length; i++) {
                    if (str) {
                        str += (',' + $('#files_img .file').eq(i).attr('index'));
                    } else {
                        str += ('' + $('#files_img .file').eq(i).attr('index'));
                    }
                }
                $('#sequence').attr('value', str);
            } else {
                alert(data.message);
            }
        }
    });
}

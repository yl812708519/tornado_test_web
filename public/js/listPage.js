/*
 说明：
 操作列按钮添加方法：edit btn-info:编辑,delete btn-danger:删除,detail btn-warning:详情,
                  1 “edit”没有样式，纯为了绑定事件添加的钩子；“btn-info”为按钮样式；“编辑”为按钮显示的字。
                  2 系统默认对edit  delete   detail 绑定了方法，如果要更改，先unbind，再bind。
                  3 可以随意添加按钮，规则如1所诉。
*/


function buildWtableHeight(){
    if(wTableOptions.TABLEHEIGHT){
        $(".wtable-data").css("height", wTableOptions.TABLEHEIGHT+"px");
        return;
    }
    $(".content-main").css("overflow","hidden");
    var mainHeight = $(".wtable-con").parent().height();
    var topBarH = $(".wtable-tools").height();
    var topBtnsH = $(".wtable-top-more").height();
    var headH =$(".wtable-head").height();
    var bottomBarH = $(".wtable-footer").height();
    if(!wTableOptions.SHOWTOPBAR){
        topBarH = -10;
    }
    if(!wTableOptions.SHOWBOTTOMBAR){
        bottomBarH=-8;
    }
    var wtableDataH = mainHeight - 22 - topBarH - topBtnsH - headH - bottomBarH;
    $(".wtable-data").css("height", wtableDataH+"px");
}
function wTable(options){
    wTableOptions = {};
    wTableOptions.FIELDS = [];//列的顺序,从表头中获取，查询返回之后需要根据这个顺序来载入数据，防止数据与表头对应不上。
    wTableOptions.UNIQUE_FIELD = options.unique_field||'id';//数据唯一id，由于各模块提供的唯一id不同，为了js统一处理，需要全局存储此字段，比如人员查询：UNIQUE_FIELD=“user_id”
    wTableOptions.RESULT;//查询返回结果，为了页面其它函数方便获取当前页面的数据。
    wTableOptions.SHOWTOPBAR = options.showTopBar==undefined?true:options.showTopBar;//是否显示查询条件区域，默认显示
    wTableOptions.SHOWBOTTOMBAR = options.showBottomBar==undefined?true:options.showBottomBar;//是否显示底部工具条，默认显示
    wTableOptions.SHOWPAGINATION = options.showPagination==undefined?true:options.showPagination;//是否显示分页，默认显示，需要showBottomBar为true
    wTableOptions.ENTERSEARCH = options.enterSearch==undefined?true:options.enterSearch;;//查询条件区域，文本框点击回车是否执行查询，默认true
    wTableOptions.DATA = options.data;//本地数据，支持本地数据加载，无需从ajax方法获取数据，注意数据格式。
    wTableOptions.TABLEHEIGHT = options.tableHeight;//指定表格高度，就不自适应页面，页面主滚动条可用。
    wTableOptions.SHOWBORDER = options.showBorder==undefined?true:options.showBorder;//是否显示表格边框

    wTableOptions.DATAURL =options.dataUrl;//ajax获取数据路径 search（）函数有用到
    //如下这些url是提供给默认的按钮使用的路径。
    wTableOptions.ADDURL =options.addUrl;//添加请求的url
    wTableOptions.DELETEURL =options.deleteUrl;//删除请求的url
    wTableOptions.EXPORTURL =options.exportUrl;//导出请求的url
    wTableOptions.EXPORTALLURL =options.exportAllUrl;//全部导出请求的url
    wTableOptions.DETAILURL =options.detailUrl;//详情请求的url
    wTableOptions.EDITURL = options.editUrl;//编辑请求的url
    wTableOptions.LOADCOMPLETE = options.onDataLoaded;//数据装载完成函数  data后台传来的完整数据
    wTableOptions.DATAFILTER = options.dataFilter;//数据载入页面之前的过滤函数
    wTableOptions.ONCLICKCELL = options.onClickCell;//点击数据单元格触发事件（点击正行事件也可以用这个函数处理） 参数cell:点击单元格（td）的jQuery对象row:经过过滤函数dataFilter处理之后的正行数据。


    if(!wTableOptions.SHOWTOPBAR){
        $(".wtable-tools").hide();
    }
    if(!wTableOptions.SHOWBOTTOMBAR){
        $(".wtable-footer").hide();
    }

    if(!wTableOptions.SHOWPAGINATION){
        $(".page-size-group,.pagination,.page_msg").hide();
    }
    if(!wTableOptions.SHOWBORDER){
        $("div.wtable ").css("border","0px");
    }


    //获取表头字段顺序
    $(".wtable-head th.wtable-col").each(function(k,v){
        var dataOptions = $(v).attr("data-options");
        if(dataOptions!=undefined) {
            //解析dataOptions为json格式
            var options = analyzeOptions(dataOptions);
            wTableOptions.FIELDS.push(options.field);
        }
    });


    search({
        currentPage:1
    });
    //页面按钮绑定事件
    bindBtn();
    //执行查询
    buildWtableHeight();//处理表格高度
    if(!wTableOptions.TABLEHEIGHT){
        var bwht;
        $(window).resize(function () {
            if(bwht) clearTimeout(bwht);
            bwht = setTimeout("buildWtableHeight();",50);
        });
    }

    function bindBtn(){
        //表格滚动条事件
        $(".wtable-data").scroll(function(){
            $(this).parent().find(".wtable-head").scrollLeft($(this).scrollLeft());
        });

    //    $(selector).scrollTop();

        //查询条件输入框，按回车时，是否执行查询
        if(wTableOptions.ENTERSEARCH){
           $(".wtable-tools input").keydown(function(event){
            //输入框按回车执行查询。
                if(event.keyCode==13){
                    search({
                        currentPage:1
                    });
                }

            })
        }
        //list页面按钮绑定事件

        $(".wtable-head th.sortable").click(function(){
            //可排序表头点击事件
            var sortArrow = $(this).find("span.glyphicon ");
            var field = analyzeOptions($(this).attr("data-options")).field;
            var type = "asc";
            if(sortArrow.hasClass("glyphicon-chevron-down")){
                //当前为降序排列
                sortArrow.removeClass("glyphicon-chevron-down");
                sortArrow.addClass("glyphicon-chevron-up");
                type = "asc";

            }else{
                //当前为升序排列
                sortArrow.removeClass("glyphicon-chevron-up");
                sortArrow.addClass("glyphicon-chevron-down");
                type = "desc";
            }
            alert(field+":"+type);
            /*
            search({
                sortField:field,
                sortType:type
            });
            */
        });
        $("#search").click(function(){
            //顶部搜索按钮
            search({
                currentPage:1
            });
        });
        //显示其他查询条件按钮点击事件
        $("#senior-search").click(function(){
            var seniorSearchs = $(".wtable-search.wtable-senior-search");
            if(seniorSearchs.hasClass("hide")){
                seniorSearchs.removeClass("hide");
                $(this).html("简易搜索");
                $(".wtable-search").not(".wtable-senior-search").addClass("hide");
            }else{
                $(this).html("高级搜索");
                seniorSearchs.addClass("hide");
                $(".wtable-search").not(".wtable-senior-search").removeClass("hide");
            }
            buildWtableHeight();
        });
        $(".page-size-group ul li a").click(function(){
            $(this).parent().addClass("disabled").siblings().removeClass("disabled");
            //显示数据数量下拉
            var pageSize = $(this).html();
            $(".page-size-group #page_size").html(pageSize);
            //执行查询
            search({
                currentPage:1,
                pageSize:pageSize
            });
        });
        $(".pagination #page_first").click(function(){
            //翻页 首页
            if($(this).parent().hasClass("disabled")) return false;
            search({
                currentPage:1
            });
        });
        $(".pagination #page_pre").click(function(){
            //翻页 上一页
            if($(this).parent().hasClass("disabled")) return false;
            var currentPage = parseInt($(".page_msg #current_page").val());
            search({
                currentPage:currentPage-1
            });
        });
        $(".pagination #page_last").click(function(){
            //翻页 尾页
            if($(this).parent().hasClass("disabled")) return false;
            search({
                currentPage:$("#total_page").html()
            });
        });
        $(".pagination #page_next").click(function(){
            //翻页 下一页
            if($(this).parent().hasClass("disabled")) return false;
            var currentPage = parseInt($(".page_msg #current_page").val());
            search({
                currentPage:currentPage+1
            });
        });

        $(".page_msg #current_page").keydown(function(event){
            //输入框按回车执行查询。
            if(event.keyCode==13){
                var totalPage = parseInt($(".page_msg #total_page").html());
                var currentPage = $(this).val();
                if(!currentPage) currentPage = 1;
                currentPage = currentPage>totalPage?totalPage:currentPage;
                search({
                    currentPage:currentPage
                });
            }
        })
        $(".wtable-footer #exportAll").click(function(){
            //全部导出
            if(!wTableOptions.EXPORTALLURL){
                wModalDialog({
                    //title:"测试标题",
                    content:"导出路径未配置！",
                    showAnimate:true,
                    type:"alert"
                });
                return
            }
            //获取查询条件
            var params =getSearchConditions();
            params['exportType'] = "all";
            //导出所有
            $.ajax({
                type: "get",
                async:false,
                url:wTableOptions.EXPORTALLURL ,
                data:params,
                beforeSend: function(XMLHttpRequest){
                    $(".loading").show();
                },
                success: function(data, textStatus){
                    window.location.href=data.result;
                },
                complete: function(XMLHttpRequest, textStatus){
                    $(".loading").hide();
                },
                error: function(){
                    //请求出错处理
                }
            });
        });
        $(".wtable-footer #exportSelected").click(function(){
            if(!wTableOptions.EXPORTURL){
                wModalDialog({
                    //title:"测试标题",
                    content:"导出路径未配置！",
                    showAnimate:true,
                    type:"alert"
                });
                return
            }
            //导出选中
            var ids = getRowIds();//默认返回选中
            if(ids) {
                $.ajax({
                    type: "get",
                    async:false,
                    url:wTableOptions.EXPORTURL ,
                    data:{"ids":ids,"exportType":"selected"},
                    beforeSend: function(XMLHttpRequest){
                        $(".loading").show();
                    },
                    success: function(data, textStatus){
                        window.location.href=data.result;
                    },
                    complete: function(XMLHttpRequest, textStatus){
                        $(".loading").hide();
                    },
                    error: function(){
                        //请求出错处理
                    }
                });
            }else{
                wModalDialog({
                    //title:"测试标题",
                    content:"请选择您要导出的记录！",
                    showAnimate:true,
                    type:"alert"
                });
            }
        });
        $(".wtable-footer #footer_delete").click(function(){
            if(!wTableOptions.DELETEURL){
                wModalDialog({
                    //title:"测试标题",
                    content:"删除URL未配置！",
                    showAnimate:true,
                    type:"alert"
                });
                return;
            }
            //删除选中
            var ids = getRowIds();//默认返回选中
            if(ids) {
                var count = ids.split(",").length-1;
                //有选中记录
                wModalDialog({
                    //title:"测试标题",
                    content:"您确定要删除选中的"+count+"条记录吗？",
                    showAnimate:true,
                    type:"confirm",
                    sureCallBack:function(){
                        var params = {};
                        params._method="delete";
                        params.ids = ids;
                        params._xsrf = getCookie("_xsrf");
                        $.ajax({
                            type: "post",
                            async:false,
                            url:wTableOptions.DELETEURL ,
                            data:params,
                            beforeSend: function(XMLHttpRequest){
                                $(".loading").show();
                            },
                            success: function(data, textStatus){
                                search();
                            },
                            complete: function(XMLHttpRequest, textStatus){
                                $(".loading").hide();
                            },
                            error: function(){
                                //请求出错处理
                            }
                        });
                    }
                });
            }else{
                //没有选中记录
                wModalDialog({
                    //title:"测试标题",
                    content:"请选择您要删除的记录！",
                    showAnimate:true,
                    type:"alert"
                });
            }
        });
        $(".wtable-footer #footer_add").click(function(){
            if(wTableOptions.ADDURL){
                location.href=wTableOptions.ADDURL;
            }else{
                alert("配置错误：系统默认添加按钮路径addUrl未配置");
            }
            //添加

        });

    }//end of function bindBtn(){
    function getSearchConditions(options){
        //获取查询条件
        var params = {};
        //当前页
        params.current_page = parseInt($(".page_msg #current_page").val())||1;
        params.page_size = $("#page_size").html()||15;

        if(options&&options.currentPage){
            params.current_page=options.currentPage;
        };

        if(options&&options.pageSize){
            params.page_size = options.pageSize;
        }

        if(options&&options.sortField){
            params.sort_field = options.sortField;
            if(options&&options.sortType){
               params.sort_type = options.sortType;
            }else{
               params.sort_type ="desc";
            }
        }
        //头部的查询条件  是否考虑缓存点击搜素时的查询条件？不缓存，翻页时会实时获取查询条件。
        $(".wtable-tools input").each(function(k,v){
            if(!$(v).parent().hasClass("hide")){
                //只拼接显示出来的查询条件
                var s_name =$(v).attr("name");
                var s_value = $(v).val();
                params[s_name] = s_value;
            }
        });
        return params;
    }
    function search(options){
        //默认刷新当前页数据
        if(!wTableOptions.DATAURL){
            var data = wTableOptions.DATA;
            //页面缓存查询结果
            wTableOptions.RESULT = data;
            //计算分页
            computePagination({
                currentPage:data.current_page,
                totalCount:data.total_count,
                pageSize:data.page_size
            });
            //载入数据
            loadWtableDatas(data);
            return;
        }
        //查询并装载数据，计算分页
        var params = getSearchConditions(options);
        $.ajax({
            type: "get",
            async:false,
            url:wTableOptions.DATAURL ,
            data:params,
            beforeSend: function(XMLHttpRequest){
                $(".loading").show();
            },
            success: function(data, textStatus){
                //页面缓存查询结果
                wTableOptions.RESULT = data;
                //计算分页
                computePagination({
                    currentPage:data.current_page,
                    totalCount:data.total_count,
                    pageSize:data.page_size
                });
                //载入数据  这个函数需要注意性能
                loadWtableDatas(data);
            },
            complete: function(XMLHttpRequest, textStatus){
                $(".loading").hide();
            },
            error: function(){
                //请求出错处理
            }
        });
    }
    function computePagination(options){
        var currentPage = options.currentPage||0;
        var totalCount = options.totalCount||0;
        var pageSize = options.pageSize||10;


        var totalPage = 0;
        var hasPre = true;
        var hasNext = true;
        totalPage = Math.ceil(totalCount/pageSize);
        if(currentPage<=1){
            hasPre = false;
        }
        if(currentPage>=totalPage){
            hasNext = false;
        }
        $(".wtable-footer .pagination .pageNum").parent().remove();
        var n = 1;
        var beginIndex = 1;
        var endIndex = totalPage;
        if(totalPage>5){
            if(currentPage<=3){
                endIndex = 5;

            }else if(currentPage>3){
                if(totalPage-currentPage<2){
                    beginIndex = totalPage-4;
                    endIndex = totalPage;

                }else{
                    beginIndex = currentPage-2;
                    endIndex = currentPage+2;
                }
            }
        }
        for(n=beginIndex;n<=endIndex;n++){
            $(".wtable-footer .pagination #page_next").parent().before('<li><a href="javascript:;" id = "'+n+'" class="pageNum">'+n+'</a></li>');
        }
        $(".wtable-footer .pagination .pageNum#"+(currentPage)).parent().addClass("disabled");
        if(hasPre){
            $(".wtable-footer .pagination #page_first").parent().removeClass("disabled");
            $(".wtable-footer .pagination #page_pre").parent().removeClass("disabled");
           // $(".wtable-footer .pagination #1").parent().removeClass("disabled");
        }else{
            $(".wtable-footer .pagination #page_first").parent().addClass("disabled");
            $(".wtable-footer .pagination #page_pre").parent().addClass("disabled");
            //$(".wtable-footer .pagination #1").parent().addClass("disabled");
        }
        if(hasNext){
            $(".wtable-footer .pagination #page_last").parent().removeClass("disabled");
            $(".wtable-footer .pagination #page_next").parent().removeClass("disabled");
           // $(".wtable-footer .pagination .pageNum:last-child").parent().removeClass("disabled");
        }else{
            $(".wtable-footer .pagination #page_last").parent().addClass("disabled");
            $(".wtable-footer .pagination #page_next").parent().addClass("disabled");
            //$(".wtable-footer .pagination .pageNum:last-child").parent().addClass("disabled");
        }

        $(".wtable-footer #page_size ").html(pageSize);
        $(".wtable-footer .page_msg #current_page ").val(currentPage);
        $(".wtable-footer .page_msg #total_page ").html(totalPage);
        $(".wtable-footer .page_msg #total_count ").html(totalCount);
    }// end of computePagination

    function loadWtableDatas(sData){
        //清空数据
        $(".wtable-data .table tbody ").html("");
        if(!sData||!sData.list||sData.list.length==0){
            bulidWtable();
            //无数据
            $(".empty-data").remove();
            $(".wtable-data").append('<div class="empty-data" style="text-align: center;line-height: 100px; position: absolute;top:0px;left:0px;width:100%;height:100%;background-color:rgba(0,0,0,0.01)">暂无数据</div>');
            return
        }
        var data = sData;
        if(wTableOptions.DATAFILTER){
            for(var i = 0;i<data.list.length;i++){
                var fd =data.list[i];
                data.list[i] = wTableOptions.DATAFILTER(fd);
            }
        }

        var datas = data.list;
        wTableOptions.UNIQUE_FIELD = data.unique_field;
        if(datas&&datas.length>0){
            //有数据
            $(".wtable-data .empty-data").remove();
            for(var i = 0 ;i<datas.length;i++){
                var trHtml = "<tr>";
                var row = datas[i];
                for(var k = 0 ;k<wTableOptions.FIELDS.length;k++){
                    var field = wTableOptions.FIELDS[k];
                    var value = row[field];
                    value = value?value:"";
                    var unId ="";
                    if(k==0){
                        var unique_id = row[wTableOptions.UNIQUE_FIELD];
                        trHtml="<tr unique_id='"+unique_id+"'>"
                        unId+='<input type="hidden" name="id" value="'+unique_id+'"/>';
                    }
                    //为了防止鼠悬停时显示出额外的html标签
                    var cellHtml = "<td class='data-cell'><div class='text_off' title='"+value+"'>"+value+"</div>"+unId+"</td>";
                    var tipTitle = $(cellHtml).text();

                    trHtml+="<td class='data-cell'><div class='text_off' title='"+tipTitle+"'>"+value+"</div>"+unId+"</td>";
                };
                trHtml+="</tr>";
                $(".wtable-data .table tbody ").append(trHtml);

            }
        }else{
            //无数据
            $(".empty-data").remove();
            $(".wtable-data").append('<div class="empty-data" style="text-align: center;line-height: 100px; position: absolute;top:0px;left:0px;width:100%;height:100%;background-color:rgba(0,0,0,0.01)">暂无数据</div>');
        }
        //构造表格结构 需要数据加载完成之后
        bulidWtable();
        //单元格点击事件
        if(wTableOptions.ONCLICKCELL){
            $(".wtable-data tr td.data-cell").click(function(event){
                wTableOptions.ONCLICKCELL($(this),wTableOptions.RESULT.list[$(this).parent().index()],event);
            });
        }
        //表格数据特殊处理等操作  数据加载完成后调用的函数
        if(wTableOptions.LOADCOMPLETE) wTableOptions.LOADCOMPLETE(data);
        //页面数据相关的按钮绑定事件 这些事件需要数据载入之后再绑定
        $(".pagination .pageNum").click(function(){
            //翻页点击页码
            if($(this).parent().hasClass("disabled")) return false;
            var pageNum =$(this).attr("id");
            search({
                currentPage:pageNum
            });
        });
        $(".wtable-data .edit").click(function(){
            if(wTableOptions.EDITURL){
                //行内操作 编辑
                var id = $(this).parents("tr").find("input[name=id]").val();
                location.href=wTableOptions.EDITURL+"?"+wTableOptions.UNIQUE_FIELD+"="+id;
            }else{
                alert("配置错误：系统默认编辑按钮路径editUrl未配置");
            }

        });
        $(".wtable-data .delete").click(function(){
            //行内操作 删除
            var id = $(this).parents("tr").find("input[name=id]").val();
            wModalDialog({
                //title:"测试标题",
                content:"您确定要删除此条记录吗？",
                showAnimate:true,
                type:"confirm",
                sureCallBack:function(){
                   // location.href=wTableOptions.DELETEURL+"?_method=delete&id="+id;
                    var params = {};
                        params._method="delete";
                        params.ids = id;
                        params._xsrf = getCookie("_xsrf");
                        $.ajax({
                            type: "post",
                            async:false,
                            url:wTableOptions.DELETEURL ,
                            data:params,
                            beforeSend: function(XMLHttpRequest){
                                $(".loading").show();
                            },
                            success: function(data, textStatus){
                                search();
                            },
                            complete: function(XMLHttpRequest, textStatus){
                                $(".loading").hide();
                            },
                            error: function(){
                                //请求出错处理
                            }
                        });
                }
            });
        });
        $(".wtable-data .detail").click(function(){
            //行内操作 详情
            var id = $(this).parents("tr").find("input[name=id]").val();
            alert("详情"+id);
        });


    }//end of loadWtableDatas;


    function bulidWtable(){
        //处理表格结构，事件绑定，表格载入数据之后调用
        $('.wtable input').iCheck('uncheck'); //— 移除 checked 状态
        //处理表格是否含有checkbox
        if($(".wtable-head th.wtable-check").length){
            if(!$(".wtable-head th.wtable-check").find("div.text_off").length){
                $(".wtable-head th.wtable-check").html('<div class="text_off">'+$(".wtable-head th.wtable-check").html()+'</div>');
            }
            //含有checkbox
            //将表格的每一行都添加一个checkbox
            $(".wtable-data tr").each(function(kk,vv){
                $(this).prepend('<td class="wtable-check"><div class="text_off"><input type="checkbox" name="check_id"/></div></td>');
            });
        }
        //处理表格是否有最后的“操作”列
        if($(".wtable-head th.wtable-oper").length){
            //含有操作列
            //获取操作类型
            var dataOptions = $(".wtable-head th.wtable-oper").attr("data-options");
            if(dataOptions!=undefined) {
                //解析dataOptions为json格式
                var options = analyzeOptions(dataOptions);
                //edit:true,delete:true,detail:true\
                var btns = "";
                var btnsw="";
                for(var pp in options){
                    if(pp =="width") {
                        btnsw = options[pp];
                        continue;
                    }
                    btns+='<button type="button" class="btn btn-success btn-xs '+pp+'">'+options[pp]+'</button>';

                }
                /*if(options.edit) btns+='<button type="button" class="btn btn-success btn-xs edit">编辑</button>';
                if(options.delete) btns+='<button type="button" class="btn btn-danger btn-xs delete">删除</button>';
                if(options.detail) btns+='<button type="button" class="btn btn-warning btn-xs detail">详情</button>';*/
                $(".wtable-data tr").each(function(kk,vv){
                    $(vv).append('<td class="wtable-oper"><div class="text_off" style="width:'+btnsw+'px">'+btns+'</div></td>');
                });
            }else{
                //默认添加一个编辑按钮
                $(".wtable-data tr").each(function(kk,vv){
                    $(vv).append('<td class="wtable-oper"><div class="text_off"  ><button type="button" class="btn btn-success btn-xs edit">编辑</button></div></td>');
                });
            }

        }
        //处理表格列宽,排列方式
        $(".wtable-head th").each(function(k,v){
            var dataOptions = $(v).attr("data-options");
            if(dataOptions!=undefined){
                //解析dataOptions为json格式
                var options = analyzeOptions(dataOptions);
                if(options.width){
                    //处理列宽
                    $(this).html("<div class='text_off' style='width:"+(options.width)+"px' orw = "+options.width+" title='"+$(this).text()+"'>"+$(this).text()+"</div>")
                    $(this).css("width",options.width);
                    $(".wtable-data tr").each(function(kk,vv){
                        $(this).find("td:eq("+k+")").css("width",options.width);
                        $(this).find("td:eq("+k+")").find("div.text_off").attr("style","width:"+options.width+"px").attr("orw",options.width);
                    });
                }
                //处理剧中方式
                if(options.align){
                    $(".wtable-data tr").each(function(kk,vv){
                        $(this).find("td:eq("+k+")").css("text-align","center");
                        $(this).find("td:eq("+k+")").find("div.text_off").css("text-align",options.align);
                    });
                }
                //是否可排序
                if(options.sort&&options.sort=="true"){
                    //glyphicon-chevron-up
                    //glyphicon-chevron-down
                    if(!$(this).find("span.glyphicon").length) {
                        $(this).addClass("sortable");
                        $(this).append('<span class="glyphicon "></span>');
                    }
                }

            }
        });

        //处理表格checkbox
        if($(".wtable-check").length){
            $('input[type=checkbox]').iCheck({
                checkboxClass: 'icheckbox_square-blue',
                radioClass: 'iradio_square-blue',
                increaseArea: '20%' // optional</span>
            });
            $('input[name=main_check]').on('ifChecked', function(event){
                $('input[name=check_id]').iCheck('check');

            });
            $('input[name=main_check]').on('ifUnchecked', function(event){
                $('input[name=check_id]').iCheck('uncheck');
            });
        }




    }//end of function bulidWtable(){


    function getRowIds(type){
        var ids = "";
        if(type =="all"){
            //获取所有行id
            $(".wtable-data input[name=id]").each(function(k,v){
                ids+=$(this).val()+",";
            });
            return ids;
        }
        //默认获取选中行的id
        $(".wtable-data tr td.wtable-check").each(function(k,v){
            if($(v).find("div").hasClass("checked")){
                ids+=$(v).next().find("input[name=id]").val()+",";
            }
        });
        return ids;
    }//end of getRowIds

    function analyzeOptions(options){
        var opt = {};
        var ops = options.split(",");
        for(var i = 0 ;i<ops.length;i++){
            var kv = ops[i].split(":");
            var key = kv[0];
            var value = kv[1];
            opt[key] = value;
        }
        return opt;
    }

    var wTableObj = {};
    wTableObj.getAllRowIds = function(){
        var allIds = []
        $(".wtable-data input[name=id]").each(function(k,v){
            allIds.push($(this).val());
        });
        return allIds;
    }
    wTableObj.getSelectedRowIds = function(){
        var ids = [];
        $(".wtable-data tr td.wtable-check").each(function(k,v){
            if($(v).find("div").hasClass("checked")){
                ids.push($(v).next().find("input[name=id]").val());
            }
        });
        return ids;
    }
    wTableObj.getSelectedRows = function(){
        var rows = [];
        $(".wtable-data tr").each(function(k,v){

            if($(v).find("td.wtable-check div.checked").length){
                rows.push(wTableOptions.RESULT.list[$(v).index()]);
            }
        });
        return rows;
    }
    wTableObj.getSearchConditions = getSearchConditions;
    return wTableObj;
}


/*var nameArr = [
"王艺豪",
"沈通",
"赵伯林",
"宋岳桢",
"解晏玥",
"卢文龙",
"郭天成",
"李润宽",
"王建宸",
"郭生岳",
"李东洋",
"王小荣",
"杨彬",
"蔡彦麓",
"祖迁淏",
"郭泽华",
"叶诏辉",
"李明达",
"黄梓安",
"马金辰",
"陈铠",
"林子涵",
"郑卓睿",
"李锐",
"刘嵩泉",
"付泽宇",
"刘孙瑞",
"吴昊",
"孟斗南",
"王飒",
"杨俊逸",
"赵伯罕",
"隋安",
"吴超越",
"高涌博",
"王越祎",
"丁璨夏",
"何义文",
"徐德昊",
"刘瀚天",
"孙玉齐",
"曹野",
"戴宁",
"范芃",
"刘壮",
"吕海铭",
"罗圣松",
"王孝聪",
"高铭鸿",
"胡志峰",
"温昕岳",
"靳帅祥",
"杨光宇",
"李京泽",
"邵年",
"潘翰聪",
"周浩博",
"叶子杨",
"裴恒志",
"肖起凡",
"张天翔",
"张宇恒",
"刘晓黎",
"陈思捷",
"杨芗琳",
"朱鸿宁",
"宫碧盈",
"关佳佳",
"顾林天",
"盛钡娜",
"化嘉仪",
"王曦赟",
"张鑫",
"王欣雨",
"严佳雯",
"张湲湲",
"陈廷曜",
"曲筱瑄",
"李宛达",
"汪扬",
"魏宇辰",
"茹钰涵",
"张愉婷",
"邹天韵",
"肖梦婕",
"马静怡",
"扎瑞蒙",
"马纳普",
];*/

var timer;
var flag = new Array(100);   
var existingnum = new Array(100);   
var clickTimes = 0;   
var randnum;   
var cellnum =1;   
var mobile;   
var num ;   
function check_input(){     
    var input = document.getElementById("real_num").
value;   
    var re = /^[1-9]+[0-9]*]*$/;   
    if (!re.test(input)){     
        alert("请输入正整数");     
        window.location.href=window.location.href;
      
        return false;     
     }   
}     
//get the random numbers from the mobile array every 0.05s   
function setTimer(){   
    timer = setInterval("getRandNum();",50);   
    document.getElementById("start").disabled = true;
    document.getElementById("end").disabled = false;
}   
function getRandNum(){   
    document.getElementById("result").value = mobile[
GetRnd(0,num)];   
}   
function GetRnd(min,max){    
    randnum = parseInt(Math.random()*(max-min+1));   
    return randnum;   
}   
//------------------------------------------------   
//turn the input's running down   
function clearTimer(){   
    noDupNum();   
    clearInterval(timer);   
    document.getElementById("start").disabled = false;
   
    document.getElementById("end").disabled = true;   
}   
// Re defined array:change the length of the array and delete the checked one   
function noDupNum(){   
    mobile.removeEleAt(randnum);   
    var o = 0;   
    for(p=0; p<mobile.length;p++){   
        if(typeof mobile[p]!="undefined"){   
            mobile[o] = mobile[p];   
            o++;   
        }   
    }   
    num = mobile.length-1;   
 }   
 function setValues(){   
    document.getElementById(cellnum).value = document.
getElementById("result").value ;   
    cellnum++;   
}   
function set_array(){   
    var real_num = document.getElementById("real_num").value ;   
    mobile= new Array(real_num);   
    var o = 0;
    for(i=1; i<=real_num;i++){
        mobile[o] = i;
        o++;
    }
    num = mobile.length-1;   
    document.getElementById("set_number").disabled = true;
}   
Array.prototype.removeEleAt = function(dx){   
    if(isNaN(dx)||dx>this.length){return false;}   
        this.splice(dx,1);   
    }
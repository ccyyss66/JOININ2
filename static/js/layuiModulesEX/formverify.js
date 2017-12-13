/**
 * Created by 71903 on 2017/5/7.
 * Decription: 关于layer-form的自定义表单验证
 */
layui.define(['form'],function (exports) {
    "use strict";

    var mod_name='formverify',
        form=layui.form,
        $ = layui.$;

    var obj={
    };


    form.verify({
        university:[
            /[\S]+/
            ,'请填写名称'
        ],
        chooseUniversity:[
            /[\S]+/
            ,'请选择大学'
        ],
        // university:function(value, item){
        //   if (new RegExp("/[\\S]+/").test(value)){
        //       return '请填写名称';
        //   }
        // },
        mphone:function (value,item) {
            if(value){
                if( !new RegExp("^1(3|4|5|7|8)[0-9]\\d{8}$").test(value)) {
                    return '手机号码输入格式有误';
                }
            }
        },
        Email:function (value,item) {
            if(value){
                if( !new RegExp("^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$").test(value)) {
                return '邮箱输入格式有误';
            }
            }
        },
        socialsecid:function (value,item) {//在验证的时候17位的身份证也会通过
            if(value){
                if( !new RegExp("^((1[1-5])|(2[1-3])|(3[1-7])|(4[1-6])|(5[0-4])|(6[1-5])|71|(8[12])|91)\\d{4}((19\\d{2}(0[13-9]|1[012])(0[1-9]|[12]\\d|30))|(19\\d{2}(0[13578]|1[02])31)|(19\\d{2}02(0[1-9]|1\\d|2[0-8]))|(19([13579][26]|[2468][048]|0[48])0229))\\d{3}(\\d|X|x)?$").test(value)) {
                return '身份证输入格式有误';
            }
            }
        },
        password: function(value, item){ //value：表单的值、item：表单的DOM对象
            if(value){
                if(!new RegExp("^(\\w){6,16}$").test(value)){
                return '只能输入6-20个字母、数字、下划线';
            }
            }
        },
        zipcode: function(value, item){ //value：表单的值、item：表单的DOM对象
            if(value){
                if(!new RegExp("^[0-9]{6}$").test(value)){
                    return '邮编输入格式有误';
                }
            }
        },
        ip:function (value,item) {
            if(value){
                if(!new RegExp("^(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|[1-9])\\."
                        + "(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)\\."
                        + "(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)\\."
                        + "(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)$").test(value)){
                    return 'ip输入格式有误';
                }
            }
        }
    });

    exports(mod_name,obj);
});
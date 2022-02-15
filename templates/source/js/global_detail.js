
$(document).ready(function(){
	LoadSliders();
});
var lang = "tr-TR";
function dateToTS (ds) {
    var date = new Date(ds)
    return date.valueOf();
}
function tsToDate (ts) {
    var d = new Date(ts);
    return d.toLocaleDateString(lang, {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}
function LoadSliders(){
    var slider_list= document.getElementsByClassName("ion-rangeslider");
    for(var i=0;i<slider_list.length;i++){
        var sl_elem = slider_list[i];
        DateSlider(sl_elem);
    }
}
function DateSlider(sl_elem){
    var sl_slider=$("#"+sl_elem.id).ionRangeSlider({
        min: dateToTS(sl_elem.getAttribute("min_value")),
        max: dateToTS(sl_elem.getAttribute("max_value")),
        from: dateToTS(sl_elem.getAttribute("from_value")),
        to: dateToTS(sl_elem.getAttribute("to_value")),
        type    : 'double',
        step    : 1,
        prefix  : '',
        prettify: tsToDate,
        hasGrid : true,
        from_fixed: true,
        to_fixed: true, 
        skinColor: '#F6F6F6'
    })
}

function RepetitiveDoubleClick(e){
    var to_address = "/global_detail/RepetitiveTransactionModel/"+e.getAttribute("data-id");
    window.location=to_address;
}
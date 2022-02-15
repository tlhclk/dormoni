// model select ten seçim sonrası diğer alanların doldurulması
function AfterSelection(field_startwith,model_select_field_name){
    console.log(field_startwith)
    console.log(model_select_field_name)
    var model_id=document.getElementById("id_"+model_select_field_name).value
    if (model_id != -1){
        GetFieldData(field_startwith,model_id)
    }
    else{
        ClearFormData(field_startwith)
    }
}
// belirtilen formu siler
function ClearFormData(field_startwith) {
    var form_data = $('[id^="'+field_startwith+'"]');
    for (var i=0; i<form_data.length; i++){
        for (let key in field_data){
            var field_id=field_startwith+"-"+key
            if (field_id == form_data[i].id){
                var input_item=document.getElementById(field_id)
                if (input_item.className.includes("form-dropdown-select2")){
                    $("#"+field_id).val(parseInt(-1)).prop("disabled",false).trigger("change");
                }
                else if (input_item.className.includes("form-date-time")){
                    input_item.value=""
                    input_item.readOnly=false
                }
                else
                {
                    input_item.value=""
                    input_item.readOnly=false
                }
            }
        }
    }
}
// belirtilen formda verilen id objesinin değerleri çekilir ve form alanlarına yazılarak kiliklenir
function GetFieldData(field_startwith,model_id){
    $.ajax({
        url: "/financial/get_form_data/",
        contentType: "application/json",
        dataType: 'json',
        data: {"field_startwith":field_startwith,"primary_key":model_id},
        success: function(result){
            field_data=result["data"]
            field_startwith=result["field_startwith"]
            var form_data = $('[id^="'+field_startwith+'"]');
            for (var i=0; i<form_data.length; i++){
                for (let key in field_data){
                    var field_id=field_startwith+"-"+key
                    if (field_id == form_data[i].id){
                        var input_item=document.getElementById(field_id)
                        if (input_item.className.includes("form-dropdown-select2")){
                            $("#"+field_id).val(parseInt(field_data[key])).prop("disabled","true").trigger("change");
                        }
                        else{
                            input_item.value=field_data[key]
                            input_item.readOnly=true
                        }
                    }
                }
            }
        }
    })
}
// tab açıldığında ait olan form  listeleri yükleniyor ve gerekli ilişkiler sağlanıyor
model_field_id_list=["id_transaction_repetitive-repetitive_id","id_transaction_change-change_id","id_transaction_penalty-penalty_id"]
function GetSelectData(item){
    tab_name=item.id.substring(8,item.id.length-4)
    field_startwith = "id_"+tab_name
    var form_data = $('[id^="'+field_startwith+'"]');
    for (var i=0; i<form_data.length; i++){
        var field_item=form_data[i]
        field_name=field_item.name
        field_value =field_item.value
        if (field_name != "csrfmiddlewaretoken"){
            field_id=field_item.id
            field_class = field_item.className
            if (field_class.includes("form-dropdown-select2")){
                field_select2 = field_item.getAttribute("data-select2-id")
            }
            // check is select is empty
            if (field_class.includes("form-dropdown-select2")){
                if (field_item.options.length == 0){
                    // if its model selection for fill rest of fields
                    if (model_field_id_list.includes(field_id)){
                        $('#'+field_id).on('select2:select', function (e) {
                            AfterSelection(field_startwith,e.currentTarget.name)
                        });
                    }
                    // fill data
                    // dummy data
                    var title =$('[for="id_'+field_name+'"]')[0].innerText
                    var newOption = new Option(title.substring(0,title.length-1), -1, false, true);
                    $("#id_"+field_name).append(newOption);
                    // real data
                    $.ajax({
                        url: "/financial/get_select_data/",
                        contentType: "application/json",
                        dataType: 'json',
                        data: {"field_name":field_name},
                        success: function(result){
                            var data_list=result["data_list"]
                            var to_field_id="id_"+result["field_name"]
                            var select_item=document.getElementById(to_field_id)
                            for (i=0; i<data_list.length; i++){
                                var data=data_list[i];
                                var newOption = new Option(data[1], data[0], false, false);
                                select_item.append(newOption);
                            }
                        }
                    })
                }
            }
        }
    }
}

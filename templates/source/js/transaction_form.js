// kaydet butonu fonksiyonu
function FormSave() {
    form_list=["form_transaction_master","form_transaction_change","form_transaction_repetitive","form_transaction_penalty"]
    var master_form_dict={}
    for (var i=0; i<form_list.length; i++){
        var form_data=document.getElementById(form_list[i]);
        var form_dict= GetFormData(form_data)
        var note_form_dict= GetNoteFormData(form_list[i])
        master_form_dict[form_data.getAttribute("model")]=form_dict;
        master_form_dict[form_data.getAttribute("model")+"_note"]=note_form_dict;
    }
    console.log(master_form_dict)
    PostData(master_form_dict)
}
// form bilgilerini topluyor
function GetFormData(form_data){
    form_dict={}
    var element_list=form_data;
    for (var i=0; i<element_list.length; i++){
        var element = element_list[i];
        var name = element.name;
        var value = element.value;
        if (name != "csrfmiddlewaretoken" && value != "" && value!= -1){
            name = name.split("-")[1]
            form_dict[name]=value
        }
    }
    return form_dict;
}
//note formunda belirtilen satır notlarını topluyor
function GetNoteFormRowData(tr_elem){
    var input_list=tr_elem.getElementsByClassName("form-control")
    var tr_dict={}
    for (var i=0; i<input_list.length; i++){
        var elem = input_list[i]
        tr_dict[elem.name]=elem.value
    }
    return tr_dict
}
// note form bilgilerini topluyor 
function GetNoteFormData(form_name){
    var table_body=document.getElementById(form_name+"_note_table_body")
    var tr_list=table_body.getElementsByClassName(form_name)
    var note_form_dict={}
    for (var i=0; i<tr_list.length; i++){
        var tr_dict= GetNoteFormRowData(tr_list[i])
        note_form_dict[i]=tr_dict
    }
    return note_form_dict
}
// Error Bilgilerini Yazdırma
function AlertError(error_data){
    var result="";
    if ("TransactionModel" in error_data){
        result = "Muhasebe Kaydı Tablosu Hatalı Alanlar: "
        for (var i=0; i<error_data["TransactionModel"].length; i++){
            var title =$('[for="id_transaction_master-'+error_data["TransactionModel"][i]+'"]')[0].innerText
            result += title.substring(0,title.length-1) + ", "
        }
        result+="\n"
    }else if ("ChangeModel" in error_data){
        result = "Aldım - Verdim Tablosu Hatalı Alanlar: "
        for (var i=0; i<error_data["ChangeModel"].length; i++){
            var title =$('[for="id_transaction_change-'+error_data["ChangeModel"][i]+'"]')[0].innerText
            result += title.substring(0,title.length-1) + ", "
        }
        result+="\n"
    }else if ("RepetitiveModel" in error_data){
        result = "Tekrarlı Olay Tablosu Hatalı Alanlar: "
        for (var i=0; i<error_data["RepetitiveModel"].length; i++){
            var title =$('[for="id_transaction_repetitive-'+error_data["RepetitiveModel"][i]+'"]')[0].innerText
            result += title.substring(0,title.length-1) + ", "
        }
        result+="\n"
    }else if ("PenaltyModel" in error_data){
        result = "Ceza Tablosu Hatalı Alanlar: "
        for (var i=0; i<error_data["PenaltyModel"].length; i++){
            var title =$('[for="id_transaction_penalty-'+error_data["PenaltyModel"][i]+'"]')[0].innerText
            result += title.substring(0,title.length-1) + ", "
        }
        result+="\n"
    }
    alert(result)
}
//form bilgilerini sevise yolluyor
function PostData(form_dict){
      $.ajax({
        url: "/financial/create/",
        contentType: "application/json",
        dataType: 'json',
        cache : false,  
        method: "post",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
          },
        data: JSON.stringify(form_dict),
        success: function(result){
            if ("error" in result) {
                AlertError(result["error"]);
            }
            else {
                // yeni kayıtlardaki başarılı seçimler comboya eklenip seçiliyor.
                if ("ChangeModel" in result){
                    var newOption = new Option("Mevcut Seçim: " + result["ChangeModel"], result["ChangeModel"], false, true);
                    $("#id_transaction_change-change_id").append(newOption).trigger('change');
                }
                if ("RepetitiveModel" in result){
                    var newOption = new Option("Mevcut Seçim: " + result["RepetitiveModel"].toString(), result["RepetitiveModel"], false, true);
                    $("#id_transaction_repetitive-repetitive_id").append(newOption).trigger('change');
                }
                if ("PenaltyModel" in result){
                    var newOption = new Option("Mevcut Seçim: " + result["PenaltyModel"].toString(), result["PenaltyModel"], false, true);
                    $("#id_transaction_penalty-penalty_id").append(newOption).trigger('change');
                }
                console.log(result)
            }
        }
    });
}
// Tablodaki not satırını silme
function NoteFormDelete(e){
    document.getElementById(e.parentElement.parentElement.id).remove();
}
// Tabloya Not Ekleme
function NoteFormAdd(e){
    var table_id=e.parentElement.parentElement.parentElement.parentElement.id
    var form_name=table_id.substring(0,table_id.length-11)
    var prefix= form_name.substring(5,form_name.length)
    var note_amount =document.getElementsByClassName(form_name).length+1;
    // form oluşturma başı
    //form element
    var note_form_elem = document.createElement("form")
    note_form_elem.method="post"
    note_form_elem.className="note-form"
    note_form_elem.id=form_name+"-"+note_amount
    note_form_elem.model="NoteModel"
    // satır element 
    var tr_elem =document.createElement("tr")
    tr_elem.className=form_name
    tr_elem.id=form_name+"-"+note_amount
    tr_elem.model="NoteModel"
    // sıra no td
    var td_order=document.createElement("td")
    td_order.innerHTML=note_amount
    tr_elem.appendChild(td_order)
    // kayıtlı not td
    var td_list=document.createElement("td")
    td_list.innerHTML=note_amount
    tr_elem.appendChild(td_list)
    // Adı td
    var td_name=document.createElement("td")
    // Adı input
    var input_name=document.createElement("input")
    input_name.type="text"
    input_name.className="form-control"
    input_name.name= "name"
    input_name.id="id_"+prefix+"-name"+"-"+note_amount
    input_name.maxLength="50"
    td_name.appendChild(input_name)
    tr_elem.appendChild(td_name)
    // Not td
    var td_note=document.createElement("td")
    // Not input
    var input_note=document.createElement("input")
    input_note.type="text"
    input_note.className="form-control"
    input_note.name="note"
    input_note.id="id_"+prefix+"-note"+"-"+note_amount
    input_note.maxLength="100"
    td_note.appendChild(input_note)
    tr_elem.appendChild(td_note)
    // Kodu td
    var td_code=document.createElement("td")
    // Kodu input
    var input_code=document.createElement("input")
    input_code.type="text"
    input_code.className="form-control"
    input_code.name="code"
    input_code.id="id_"+prefix+"-code"+"-"+note_amount
    input_code.maxLength="20"
    td_code.appendChild(input_code)
    tr_elem.appendChild(td_code)
    // Açıklama td
    var td_desc=document.createElement("td")
    // Açıklama input
    var input_desc=document.createElement("input")
    input_desc.type="text"
    input_desc.className="form-control"
    input_desc.name="desc"
    input_desc.id="id_"+prefix+"-desc"+"-"+note_amount
    input_desc.maxLength="500"
    td_desc.appendChild(input_desc)
    tr_elem.appendChild(td_desc)
    // buton td
    var td_buton = document.createElement("td")
    // buton buton
    var buton_sil= document.createElement("buton")
    buton_sil.className="btn btn-secondary btn-icon-split"
    buton_sil.type="button"
    buton_sil.setAttribute("onclick","NoteFormDelete(this)")
    buton_sil.setAttribute("formname",form_name)
    // buton span
    var span_sil = document.createElement("span")
    span_sil.className = "text"
    span_sil.innerHTML="Sil"
    buton_sil.appendChild(span_sil)
    td_buton.appendChild(buton_sil)
    tr_elem.appendChild(td_buton)
    note_form_elem.appendChild(tr_elem)
    // form oluşturma sonu
    //<button formName="form_transaction_master_note" class="btn btn-secondary btn-icon-split" type="button" onclick="NoteFormAdd(this)"><span class="text">Ekle</span></button>
    var table_elem=document.getElementById(table_id+"_body")
    table_elem.appendChild(tr_elem)
}
// model select ten seçim sonrası diğer alanların doldurulması
function AfterSelection(form_data,model_select_field_name){
    var model_id=document.getElementById("id_"+model_select_field_name).value
    if (model_id != -1){
        GetFieldData(form_data.id,model_id)
    }
    else{
        ClearFormData(form_data)
    }
}
// belirtilen formu siler
function ClearFormData(form_data) {
    var field_pre_name = form_data.id.substring(5,form_data.id.length)
    for (var i=0; i<form_data.length; i++){
        for (let key in field_data){
            var field_id="id_"+field_pre_name+"-"+key
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
function GetFieldData(form_id,model_id){
    $.ajax({
        url: "/financial/get_form_data/",
        contentType: "application/json",
        dataType: 'json',
        data: {"form_id":form_id,"primary_key":model_id},
        success: function(result){
            field_data=result["data"]
            form_id=result["form_id"]
            var form_data = document.getElementById(form_id);
            var field_pre_name = form_id.substring(5,form_id.length)
            for (var i=0; i<form_data.length; i++){
                for (let key in field_data){
                    var field_id="id_"+field_pre_name+"-"+key
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
    form_name = "form_"+tab_name
    form_data=document.getElementById(form_name);
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
                            AfterSelection(e.currentTarget.form,e.currentTarget.name)
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
// çerez verisi alma
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + "=")) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
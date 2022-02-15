function PageLoad(){
	NotificationLoad();
}
function NotificationLoad(){
	var apiUrl = "http://127.0.0.1:8000/functions/GetNotifications";
	fetch(apiUrl).then(response => {
		return response.json();
	}).then(data => {
		var result_text='<span class="dropdown-header">'+data.length+' Bildirim</span>';
		result_text+='<div class="dropdown-divider"></div>'
		data.forEach(item =>{
			result_text+='<div class="dropdown-divider"></div><a href="#" class="dropdown-item"><i class="fa fa-bell-exclamation mr-2"></i>'+item.title+'<span class="float-right text-muted text-sm">'+item.datetime+'</span></a>'
		})
		result_text+='<div class="dropdown-divider"></div>'
		result_text+='<a href="#" class="dropdown-item dropdown-footer">Tüm Bildirimler</a>'
		document.getElementById("id_notification_list").innerHTML=result_text;
		document.getElementById("id_notification_count").innerHTML=data.length || 0;
	}).catch(err => {
		// Do something for an error here
		console.log("Api Hatası: " +err)
	});
}

function DetailLoad(){
	var apiUrl = window.location;
	fetch(apiUrl).then(response => {
		return response.json();
	}).then(data => {
		var result_text='<span class="dropdown-header">'+data.length+' Bildirim</span>';
		result_text+='<div class="dropdown-divider"></div>'
		data.forEach(item =>{
			result_text+='<div class="dropdown-divider"></div><a href="#" class="dropdown-item"><i class="fa fa-bell-exclamation mr-2"></i>'+item.title+'<span class="float-right text-muted text-sm">'+item.datetime+'</span></a>'
		})
		result_text+='<div class="dropdown-divider"></div>'
		result_text+='<a href="#" class="dropdown-item dropdown-footer">Tüm Bildirimler</a>'
		document.getElementById("id_notification_list").innerHTML=result_text;
		document.getElementById("id_notification_count").innerHTML=data.length || 0;
	}).catch(err => {
		// Do something for an error here
		console.log("Api Hatası: " +err)
	});
}



$(document).ready(function () {
    AllReportLoad();
});
function AllReportLoad(){
    var report_list = document.getElementsByClassName("global_report");
    for (var i = 0;i<report_list.length;i++)
    {
        ReportLoad(report_list[i]);
    }
}
function ReportLoad(report_canvas){
    data_dict={
        "report_code":report_canvas.getAttribute("id"),
    }
    //console.log(data_dict);
    console.log(123)
    $.ajax({
        url: "/functions/GetReportData/",
        contentType: "application/json",
        dataType: 'json',
        async: false,
        data: data_dict,
        success: function(result){
            if (result.hasOwnProperty("error")) {
                AlertError(result["error"]);
            }
            else {
                console.log(result)
                if ("-0-" in result)
                {
                    var report_type = result["report_type"];
                }
                else
                {
                    var report_type = result["report_type"]
                }
                if (report_type=="1")
                {
                    GetPieChart(result["report_code"],result)
                }
                else if (report_type=="2")
                {
                    GetLineChart(result["report_code"],result)
                }
                else if (report_type=="3")
                {
                    GetBarChart(result["report_code"],result)
                }
            }
        }
    });
}
function GetPieChart(chart_id,report_data) {
    var label_list=[];
    var value_data=[];
    for (var key in report_data["dataset"])
    {
        data = report_data["dataset"][key];
        label_list=report_data["dataset"][key]["text_title"];
        var value_dict={};
        value_dict["label"]=data["title"];
        value_dict["data"] = data["value_data"];
        value_dict["backgroundColor"]=['#C60000','#f56954','#C68D00','#f39c12','#00A763','#00B2B4','#00c0ef', '#3c8dbc', '#d2d6de','#000000'];
        value_dict["fill"]=false;
        value_data.push(value_dict)
    }
    var chartData        = 
    {
        labels: label_list,
        datasets: value_data
    };
    var chartOptions     = 
    {
        maintainAspectRatio : false,
        responsive : true,
        legend:{
            position:'right',
            onClick:
                function (e,legendItem) 
                {
                    //console.log(legendItem)
                    //console.log(e)
                },
            title:
            {
                text:"Toplam: "+ 1
            },
            labels:
            {
                generateLabels: 
                function(chart) 
                {
                    var data = chart.data;
                    console.log(chart);
                    if (data.labels.length && data.datasets.length) 
                    {
                        return data.labels.map(function(label, i) 
                        {
                            var meta = chart.getDatasetMeta(0);
                            var style = meta.controller.getStyle(i);
                            return {
                                text: label+": "+data.datasets[0].data[i],
                                fillStyle: style.backgroundColor,
                                strokeStyle: style.borderColor,
                                lineWidth: style.borderWidth,
                                hidden: isNaN(data.datasets[0].data[i]) || meta.data[i].hidden,
                                index: i
                            };
                        });
                    }
                    return [];
                }
            }
        },
        plugins:
        {
            title:
            {
                display:true,
                text: "Toplam: "+ 1
            },
            subtitle:
            {
                display:true,
                text: "Toplam: "+ 2
            }
        }
    };
    //-------------
    //- PIE CHART -
    //-------------
    // Get context with jQuery - using jQuery's .get() method.
    //var donutChartCanvas = $('#'+chart_id).get(0).getContext('2d');
    var pieChartCanvas = document.getElementById(chart_id).getContext('2d')
    new Chart(pieChartCanvas, {
        type: 'pie',
        data: chartData,
        options: chartOptions
      })
  
}

function GetLineChart(chart_id,report_data) {
    var label_list=[];
    var value_data=[];
    var color_list=['#C60000','#f56954','#C68D00','#f39c12','#00A763','#00B2B4','#00c0ef', '#3c8dbc', '#d2d6de','#000000'];
    var ci=0;
    for (var key in report_data["dataset"])
    {
        data = report_data["dataset"][key];
        label_list=report_data["dataset"][key]["text_title"];
        var value_dict={};
        value_dict["label"]=data["title"];
        value_dict["data"] = data["value_data"];
        value_dict["backgroundColor"]=color_list[ci%10];
        value_dict["fill"]=false;
        value_data.push(value_dict)
        ci+=1
    }
    var chartData        = 
    {
        labels: label_list,
        datasets: value_data
    };
    var chartOptions = 
    {
        maintainAspectRatio : false,
        responsive : true,
        legend: 
        {
            position:'bottom',
            onClick:
                function (e,legendItem) 
                {
                    //console.log(legendItem)
                    //console.log(e)
                },
        },
        scales: 
        {
            xAxes: 
            [{
                gridLines : 
                {
                    display : false,
                }
            }],
            yAxes: 
            [{
                gridLines : {
                    display : false,
                }
            }]
        },
        
    };
    
    //-------------
    //- LINE CHART -
    //--------------
    var lineChartCanvas = document.getElementById(chart_id).getContext('2d')

    var lineChart = new Chart(lineChartCanvas, {
      type: 'line',
      data: chartData,
      options: chartOptions
    })

}

function GetBarChart(chart_id,report_data) {
    var label_list=[];
    var value_data=[];
    var color_list=['#C60000','#f56954','#C68D00','#f39c12','#00A763','#00B2B4','#00c0ef', '#3c8dbc', '#d2d6de','#000000'];
    var ci=0;
    for (var key in report_data["dataset"])
    {
        data = report_data["dataset"][key];
        label_list=report_data["dataset"][key]["text_title"];
        var value_dict={};
        value_dict["label"]=data["title"];
        value_dict["data"] = data["value_data"];
        value_dict["backgroundColor"]=color_list[ci%10];
        value_dict["fill"]=false;
        value_data.push(value_dict)
        ci+=1
    }
    var chartData        = 
    {
        labels: label_list,
        datasets: value_data
    };
    var chartOptions = 
    {
        maintainAspectRatio : false,
        responsive : true,
        legend: 
        {
            position:'bottom',
            onClick:
                function (e,legendItem) 
                {
                    //console.log(legendItem)
                    //console.log(e)
                },
        },
        scales: 
        {
            xAxes: 
            [{
                gridLines : 
                {
                    display : false,
                }
            }],
            yAxes: 
            [{
                gridLines : {
                    display : false,
                }
            }]
        },
        
    };
    
    //-------------
    //- BAR CHART -
    //--------------
    var barChartCanvas = document.getElementById(chart_id).getContext('2d')

    var barChart = new Chart(barChartCanvas, {
      type: 'bar',
      data: chartData,
      options: chartOptions
    })

}
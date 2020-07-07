function get_time() {
    $.ajax({
        url: '/time',
        type: 'get',
        timeout: '10000',
        success: function (data) {
            $('#time').text(data)
        },
        error: function (xhr, type, errorThrown) {
        }
    })
}
function get_leftbottom() {
    $.ajax({
        url: '/left-bottom',
        type: 'get',
        timeout: '10000',
        success:function (data) {
            lb_option.xAxis.data = data.time
            lb_option.series[0].data = data.frontend
            lb_option.series[1].data = data.backend1
            lb_option.series[2].data = data.backend2
            lb_option.series[3].data = data.reject
            lb_map.setOption(lb_option)
        },
        error: function (xhr, type, errorThrown) {
        }
    })
}
// function get_info() {
//     $.ajax({
//         url: '/info',
//         success:function (data) {
//                 var tr;
//                 tr='<td>'+data.time+'</td>'+'<td>'+data.demand+'</td>'+'<td>'+data.order+'</td>'
//                 $("#commandTable").append('<tr>'+tr+'</tr>')
//         },
//         error: function (xhr, type, errorThrown) {
//         }
//     })
// }
// 暂时不用
get_time()
get_leftbottom()
setInterval(get_time, 1000)
setInterval(get_leftbottom, 1000*2)

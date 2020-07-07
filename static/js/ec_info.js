$(function () {
    $('#sendmsg').click(function(){
            var content = $('#content').val();
            $.ajax({
                type:"POST",
                url:"/info",
                dataType:"json",
                data: {content:content},
                success:function(data){
                    let tr;
                    tr='<td>'+data.time+'</td>'+'<td>'+data.demand+'</td>'+'<td>'+data.order+'</td>'
                    $("#commandTable").append('<tr align="center">'+tr+'</tr>')
                }
            });
    })
})
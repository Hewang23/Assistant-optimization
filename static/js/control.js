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

function get_info() {
    $.ajax({
        url: '/info',
        type: 'post',  // !!!!!
        timeout: '10000',
        success:function (data) {
           // 更新内容
        },
        error: function (xhr, type, errorThrown) {
        }
    })
}

// 暂时不用
function get_leftbottom() {
    $.ajax({
        url: '/left-bottom',
        type: 'get',
        timeout: '10000',
        success:function (data) {
           // 更新内容
        },
        error: function (xhr, type, errorThrown) {
        }
    })
}


// 前后端不分离
function backend_loop() {
    $.ajax({
        url: '/backend_loop'
    })
}

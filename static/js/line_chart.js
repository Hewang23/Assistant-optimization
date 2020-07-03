var lb_map = echarts.init(document.getElementById("chart"), 'dark');

lb_option = {
    title: {
        text: '服务器负载图'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['前端服务器负载', '后端服务器1负载', '后端服务器2负载', '被拒绝服务数量']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    },
    yAxis: {
        type: 'value',
        splitLine: {
            show: true,
            lineStyle: {
                color: '#17273B',
                width: 1,
                type: 'solid'
            }
        }
    },
    series: [
        {
            name: '前端服务器负载',
            type: 'line',
            data: [120, 132, 101, 134, 90, 230, 210]
        },
        {
            name: '后端服务器1负载',
            type: 'line',
            data: [220, 182, 191, 234, 290, 330, 310]
        },
        {
            name: '后端服务器2负载',
            type: 'line',
            data: [150, 232, 201, 154, 190, 330, 410]
        },
        {
            name: '被拒绝服务数量',
            type: 'line',
            data: [320, 332, 301, 334, 390, 330, 320]
        }
    ]
};
lb_map.setOption(lb_option);
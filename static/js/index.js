(function(){
    var mychart = echarts.init(document.querySelector(".bar .chart"));
    var option = {
        color:["#2f89cf"],
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        grid: {
          left: '0%',
          right: '0%',
          bottom: '4%',
          top: "10px",
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            data: [
                "旅游行业",
                "教育培训",
                "游戏行业",
                "医疗行业",
                "电商行业",
                "社交行业",
                "金融行业" 
            ],
            axisTick: {
              alignWithLabel: true
            },
            axisLabel: {
                color: "rgba(255, 255, 255, 0.6)",
                fontSize: "12",
            },
            axisLine:{
                show: false,
            }
          }
        ],
        yAxis: [
          {
            type: 'value',
            axisLabel: {
                color: "rgba(255, 255, 255, 0.6)",
                fontSize: "12",
            },
            axisLine:{
                // show: false,
                lineStyle:{
                    color: "rgba(255, 255, 255, 0.1)"
                }
            },
            splitLine:{
                lineStyle:{
                    color: "rgba(255, 255, 255, 0.1)"
                }
            }
          }
        ],
        series: [
          {
            name: 'Direct',
            type: 'bar',
            barWidth: '35%',
            data: [200, 300, 300, 900, 1500, 1200, 600],
            itemStyle:{
                barBorderRadius: 5
            }
          }
        ]
      };
      mychart.setOption(option);
      window.addEventListener("resize", function(){
          mychart.resize(); 
      })

})();
(function(){
    var mychart = echarts.init(document.querySelector(".bar2 .chart"));
    var option = {
        grid: {
          left: '22%',
          top:"10%",
          bottom: '10%',
          containLabel: false
        },
        xAxis: {
          type: 'value',
          show: false,
          boundaryGap: [0, 0.01]
        },
        yAxis: {
          type: 'category',
          data: ['Brazil', 'Indonesia', 'USA', 'India', 'China', 'World'],
          axisLine:{
            show:false,
          },
          axisTick:{
              show:false,
          },
          axisLabel:{
            color:"#fff",
          },
        },
        series: [
          {
            name: '条',
            type: 'bar',
            data: [100, 100, 100, 100, 100, 100],
            itemStyle:{
                barBorderRadius:20
            }
          },
          {
            name: '2012',
            type: 'bar',
            data: [100, 100, 100, 100, 100, 100],

          },
          
        ]
      };
      mychart.setOption(option);
})();



function fetchDataAndPlotChart(){
    let ca=0;
    let ci=0;
    axios.get('http://127.0.0.1:8000/userinfo').then(response=> {
        const apiData=response.data;
        for(i in apiData){
           if(apiData[i]==='Android'){
            ca++;
           }
           else if(apiData[i]==='iOS'){
            ci++;
           }
        }
       
    })
    
    
    .catch(error=>{
        console.error('Error fetching data:', error);
    })
    return ca,ci;
}
function plotOSChart(columnData){


  var ctx = document.getElementById('main-chart').getContext('2d');
  var myChart = new Chart(ctx, {
      type: 'bar',
      
      data: {
          labels: ['Android','iOS'],
          datasets: [{
              label: 'DeviceOS',
              data: columnData,
              
              borderColor: 'rgb(75, 192, 192)',
  
              borderWidth: 1
          }]
        },
      options: {
          responsive: true
      }
  });
}
document.addEventListener("DOMContentLoaded",fetchDataAndPlotChart);





function plotOSChart(columnData){
    let ca=0;
    let ci=0;
    axios.get('http://127.0.0.1:8000/userinfo').then(response=> {
        const apiData=response.data;
        console.log(apiData);
        for(i in apiData){
           if(apiData[i].deviceos==='Android'){
            ca++;
           }
           else if(apiData[i].deviceos==='iOS'){
            ci++;
           }
        }
        console.log("Total Android: "+ca);
        var ctx = document.getElementById('main-chart').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'doughnut',
            
            data: {
                labels: ['Android','iOS'],
                datasets: [{
                    label: 'DeviceOS',
                    data: [ca,ci] ,
                    backgroundColor: [
                      'rgba(255,99,132,2)',
                      'rgba(255,205,86,2)'
      
                  ],
                    borderColor: 'rgb(75, 192, 192)',
        
                    borderWidth: 1
                }]
              },
            options: {
                responsive: true
            }
        });
    })
    .catch(error=>{
        console.error('Error fetching data:', error);
    })
    
    
    


  
}
document.addEventListener("DOMContentLoaded",plotOSChart);





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
            type: 'bar',
            
            data: {
                labels: ['Android','iOS'],
                datasets: [{
                    label: 'DeviceOS',
                    data: [{x:0,y:ca},{x:1,y:ci}] ,
                    backgroundColor: [
                      'rgba(85,85,85, 1)'
      
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


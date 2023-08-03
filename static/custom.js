

function plotOSChart(){
    let ca=0;
    let ci=0;
    const start_date=document.getElementById('start_date');
    const start_dateval=start_date.value;
    const end_date=document.getElementById('end_date');
    const end_dateval=end_date.value;
    debugger;
    const urlWithParams=url+'/userinfo?start_date='+start_dateval+'&end_date='+end_dateval;
    axios.get(urlWithParams).then(response=> {
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

        if(window.myChart instanceof Chart){
            window.myChart.destroy();
           }
        var ctx = document.getElementById('mainChart').getContext('2d');
        window.myChart = new Chart(ctx, {
            type: 'doughnut',
            
            data: {
                labels: ['Android','iOS'],
                datasets: [{
                    label: 'DeviceOS',
                    data: [ca,ci] ,
                    backgroundColor: [
                      'rgba(153,156,164)',
                      'rgba(49,49,49)'
      
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


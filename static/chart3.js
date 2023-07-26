
function plotWatchChart(columnData){
    let c1=0;
    let c2=0;
    let c3=0;
    let c4=0;
    let c5=0;
    let c6=0;
    let c7=0;
    axios.get('http://127.0.0.1:8000/userinfo').then(response=> {
        const apiData=response.data;
        console.log(apiData);
        for(i in apiData){
           if(apiData[i].devicetype==='GizFit ULTRA'){
            c1++;
           }
           else if(apiData[i].devicetype==='GizFit SLATE2'){
            c2++;
           }
           else if(apiData[i].devicetype==='GizFit SLATE'){
            c3++;
           }
           else if(apiData[i].devicetype==='GizFit BLAZE'){
            c4++;
           }
           else if(apiData[i].devicetype==='920 Glow Luxe'){
            c5++;
           }
           else if(apiData[i].devicetype==='GizFit BLAZE MAX'){
            c6++;
           }
           else if(apiData[i].devicetype==='GizFit BLAZE X'){
            C7++;
           }
        }
        //console.log("Total Android: "+ca);
        var ctx3= document.getElementById('main-chart3').getContext('2d');
        var myChart3 = new Chart(ctx3, {
            type: 'bar',
            
            data: {
                labels: ['GizFit ULTRA','GizFit SLATE2','GizFit SLATE','GizFit BLAZE','920 Glow Luxe','GizFit BLAZE MAX','GizFit BLAZE X'],
                datasets: [{
                    label: 'watches',
                    data: [{x:0,y:c1},{x:1,y:c2},{x:2,y:c3},{x:3,y:c4},{x:4,y:c5},{x:5,y:c6},{x:6,y:c7}] ,
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
document.addEventListener("DOMContentLoaded",plotWatchChart);

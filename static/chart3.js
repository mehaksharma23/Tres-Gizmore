var dataArray=[];
function plotWatchChart(columnData){
    let c1=0;
    let c2=0;
    let c3=0;
    let c4=0;
    let c5=0;
    let c6=0;
    let c7=0;
    fetch('http://127.0.0.1:8000/userinfo').then(response=> response.json()).then(response=> {
        response.forEach(item => {
            const devicetype=item.devicetype;
            dataArray.push(devicetype);
        });
       
        console.log(dataArray);
        for(i in dataArray){
           if(dataArray[i]==='GizFit ULTRA'){
            c1++;
           }
           else if(dataArray[i]==='GizFit SLATE2'){
            c2++;
           }
           else if(dataArray[i]==='GizFit SLATE'){
            c3++;
           }
           else if(dataArray[i]==='GizFit BLAZE'){
            c4++;
           }
           else if(dataArray[i]==='920 Glow Luxe'){
            c5++;
           }
           else if(dataArray[i]==='GizFit BLAZE MAX'){
            c6++;
           }
           else if(dataArray[i]==='GizFit BLAZE X'){
            c7++;
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
                        'rgba(255, 99, 132, 2)',
                        'rgba(255, 159, 64, 2)',
                        'rgba(255, 205, 86, 2)',
                        'rgba(75, 192, 192, 2)',
                        'rgba(54, 162, 235, 2)',
                        'rgba(153, 102, 255, 2)',
                        'rgba(201, 203, 207, 2)'
      
      
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

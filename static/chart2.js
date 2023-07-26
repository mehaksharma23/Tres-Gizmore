
function plotMonthlyChart(columnData){
    let c1=0;
    let c2=0;
    let c3=0;
    let c4=0;
    let c5=0;
    let c6=0;
    let c7=0;
    let c8=0;
    let c9=0;
    let c10=0;
    let c11=0;
    let c12=0;
    axios.get('http://127.0.0.1:8000/userinfo').then(response=> {
        const apiData=response.data;
        console.log(apiData);
        for(i in apiData){
          let month=  (apiData[i].datecreated).getMonth();
           if(month===0){
            c1++;
           }
           else if(month===1){
            c2++;
           }
           else if(month===2){
            c3++;
           }
           else if(month===3){
            c4++;
           }
           else if(month===4){
            c5++;
           }
           else if(month===5){
            c6++;
           }
           else if(month===6){
            c7++;
           }
           else if(month===7){
            c8++;
           }
           else if(month===8){
            c9++;
           }
           else if(month===9){
            c10++;
           }
           else if(month===10){
            c11++;
           }
           else if(month===11){
            c12++;
           }
        }
        console.log("Total Android: "+ca);
        var ctx2 = document.getElementById('main-chart2').getContext('2d');
        var myChart2 = new Chart(ctx2, {
            type: 'bar',
            
            data: {
                labels: ['January','February','March','April','May','June','July','August','September','October','November','December'],
                datasets: [{
                    label: 'DeviceOS',
                    data: [{x:0,y:c1},{x:1,y:c2},{x:2,y:c3},{x:3,y:c4},{x:4,y:c5},{x:5,y:c6},{x:6,y:c7},{x:7,y:c8},{x:8,y:c9},{x:9,y:c10},{x:10,y:c11},{x:11,y:c12}] ,
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
document.addEventListener("DOMContentLoaded",plotMonthlyChart);


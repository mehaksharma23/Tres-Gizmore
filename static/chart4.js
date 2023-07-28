
function plotGenderChart(){
    let ca=0;
    let ci=0;
    const start_date=document.getElementById('start_date');
    const start_dateval=start_date.value;
    const end_date=document.getElementById('end_date');
    const end_dateval=end_date.value;
    const urlWithParams='http://127.0.0.1:8000/userinfo?start_date='+start_dateval+'&end_date='+end_dateval;
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
       // console.log("Total Android: "+ca);

       if(window.myChart4 instanceof Chart){
        window.myChart4.destroy();
       }
       
        var ctx4 = document.getElementById('mainChart4').getContext('2d');
        
        window.myChart4 = new Chart(ctx4, {
            type: 'doughnut',
            
            data: {
                labels: ['Female','Male'],
                datasets: [{
                    label: 'Gender',
                    data: [ca,ci] ,
                    backgroundColor: [
                      'rgba(245,116,39,0.8)',
                      'rgba(61,138,251)'
      
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
document.addEventListener("DOMContentLoaded",plotGenderChart);


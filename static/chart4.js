
function plotGenderChart(columnData){
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
       // console.log("Total Android: "+ca);
        var ctx4 = document.getElementById('main-chart4').getContext('2d');
        var myChart4 = new Chart(ctx4, {
            type: 'doughnut',
            
            data: {
                labels: ['Female','Male'],
                datasets: [{
                    label: 'Gender',
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
document.addEventListener("DOMContentLoaded",plotGenderChart);


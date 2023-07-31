


function getStartDate(){
    
   const start_date=document.getElementById('start_date');
   const start_dateval=start_date.value;
   console.log(start_dateval);
  
   return start_dateval;
   
}

function getEndDate(){
    const end_date=document.getElementById('end_date');
    const end_dateval=end_date.value;
    console.log(end_dateval);
   
    plotOSChart();
    plotWatchChart();
    plotMonthlyChart();
    plotGenderChart();
  
    return end_dateval;
}

function plotMonthlyChart() {
    let c1 = 0;
    let c2 = 0;
    let c3 = 0;
    let c4 = 0;
    let c5 = 0;
    let c6 = 0;
    let c7 = 0;
    let c8 = 0;
    let c9 = 0;
    let c10 = 0;
    let c11 = 0;
    let c12 = 0;
    const start_date=document.getElementById('start_date');
    const start_dateval=start_date.value;
    const end_date=document.getElementById('end_date');
    const end_dateval=end_date.value;
    debugger;
  
    const urlWithParams='http://127.0.0.1:8000/userinfo?start_date='+start_dateval+'&end_date='+end_dateval;
    axios.get(urlWithParams).then(response => {
        const apiData = response.data;
        console.log(apiData);
        for (i in apiData) {
            let month = new Date(apiData[i].datecreated).getMonth();
            if (month === 0) {
                c1++;
            }
            else if (month === 1) {
                c2++;
            }
            else if (month === 2) {
                c3++;
            }
            else if (month === 3) {
                c4++;
            }
            else if (month === 4) {
                c5++;
            }
            else if (month === 5) {
                c6++;
            }
            else if (month === 6) {
                c7++;
            }
            else if (month === 7) {
                c8++;
            }
            else if (month === 8) {
                c9++;
            }
            else if (month === 9) {
                c10++;
            }
            else if (month === 10) {
                c11++;
            }
            else if (month === 11) {
                c12++;
            }
        }
       
        //console.log("Total Android: "+ca);
        if(window.myChart2 instanceof Chart){
            window.myChart2.destroy();
           }

       
        var ctx2 = document.getElementById('mainChart2').getContext('2d');
        window.myChart2 = new Chart(ctx2, {
            type: 'bar',

            data: {
                labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
                datasets: [{
                    label: 'Months',
                    data: [{ x: 0, y: c1 }, { x: 1, y: c2 }, { x: 2, y: c3 }, { x: 3, y: c4 }, { x: 4, y: c5 }, { x: 5, y: c6 }, { x: 6, y: c7 }, { x: 7, y: c8 }, { x: 8, y: c9 }, { x: 9, y: c10 }, { x: 10, y: c11 }, { x: 11, y: c12 }],
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
        .catch(error => {
            console.error('Error fetching data:', error);
        })






}

document.addEventListener("DOMContentLoaded",plotMonthlyChart);


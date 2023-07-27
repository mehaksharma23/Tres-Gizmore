const apiUrl='http://127.0.0.1:8000/userinfo';
async function fetchDataFromAPI(){
    try{
        const response=await fetch(apiUrl);
        if(!response.ok){
            throw new Error("Network response was not ok");
        }
        const data=await response.json();
        return data;
    }
    catch (error){
        console.error("Error fetching data:", error.message);
        return [];
    }
}
function filterDataByYear(data,year){
    return data.filter((entry)=> new Date(entry.datecreated).getFullYear()===year);
}

function createChart(yearlyData){
    const ctx2=document.getElementById("main-chart2").getContext("2d");
    const mychart2=new Chart(ctx2, {
        type:"bar",
        data: {
            labels:yearlyData.map((entry) => entry.datecreated),
            datasets: [
                {
                    label:"Data for year",
                    data:yearlyData.map((entry=>entry.value)),
                    backgroundColor: "rgba(75,192,192,1)",
                    borderColor: "rgba(75,192,192,1)",
                    borderWidth: 1,
                }
            ]
        },
        options: {
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'day'
                    }
                }
            }
            responsive: true
        }
    });
}


async function initializeChart(){
    try{
        const rawData= await fetchDataFromAPI();
        const targetYear=2023 ;
        const filteredData= filterDataByYear(rawData,targetYear);
        console.log(filteredData);
        createChart(filteredData);
    }
    catch(error){
        console.error("Error initializing chart:", error.message);
    }
}

initializeChart();

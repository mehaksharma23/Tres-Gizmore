var currentDate=new Date();
var defaultEndDate=formatDate(currentDate);
var defaultStartDate=new Date(currentDate);
defaultStartDate.setDate(defaultStartDate.getDate()-7);
defaultStartDate=formatDate(defaultStartDate);
document.getElementById("start_date").value=defaultStartDate;
document.getElementById("end_date").value=defaultEndDate;
function formatDate(date){
    var year=date.getFullYear();
    var month=("0" + (date.getMonth()+1)).slice(-2);
    var day=("0" + date.getDate()).slice(-2);
    return year + "-" + month + "-" + day;
}


window.onload=function(){
    countRows();
    active();
    inactive();
    newUsers();
};

function countRows(){
    let users=0;
    const urlWithParams='http://preproduction-k:5001/summary';
    axios.get(urlWithParams).then(response => {
        const apiData = response.data;
        console.log(apiData);
      
        document.getElementById("users1").innerHTML=apiData.row_count;
    })
}

function active(){
    let users=0;
    const urlWithParams='http://preproduction-k:5001/active';
    axios.get(urlWithParams).then(response => {
        const apiData = response.data;
        console.log(apiData);
      
        document.getElementById("users2").innerHTML=apiData.active_user;
    })
}

function inactive(){
    let users=0;
    const urlWithParams='http://preproduction-k:5001/inactive';
    axios.get(urlWithParams).then(response => {
        const apiData = response.data;
        console.log(apiData);
      
        document.getElementById("users3").innerHTML=apiData.inactive_user;
    })
}

function newUsers(){
    let users=0;
    const urlWithParams='http://preproduction-k:5001/new';
    axios.get(urlWithParams).then(response => {
        const apiData=response.data;
        console.log(apiData);

        document.getElementById("users4").innerHTML=apiData.new_user;
    })

}
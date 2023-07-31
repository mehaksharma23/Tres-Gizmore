window.onload=function(){
    countRows();
    active();
    inactive();
    newUsers();
};

function countRows(){
    let users=0;
    const urlWithParams='http://127.0.0.1:8000/summary';
    axios.get(urlWithParams).then(response => {
        const apiData = response.data;
        console.log(apiData);
      
        document.getElementById("users1").innerHTML=apiData.row_count;
    })
}

function active(){
    let users=0;
    const urlWithParams='http://127.0.0.1:8000/active';
    axios.get(urlWithParams).then(response => {
        const apiData = response.data;
        console.log(apiData);
      
        document.getElementById("users2").innerHTML=apiData.active_user;
    })
}

function inactive(){
    let users=0;
    const urlWithParams='http://127.0.0.1:8000/inactive';
    axios.get(urlWithParams).then(response => {
        const apiData = response.data;
        console.log(apiData);
      
        document.getElementById("users3").innerHTML=apiData.inactive_user;
    })
}

function newUsers(){
    let users=0;
    const urlWithParams='http://127.0.0.1:8000/new';
    axios.get(urlWithParams).then(response => {
        const apiData=response.data;
        console.log(apiData);

        document.getElementById("users4").innerHTML=apiData.new_user;
    })

}
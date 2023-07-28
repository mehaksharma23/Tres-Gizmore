window.onload=function(){
    countRows();
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
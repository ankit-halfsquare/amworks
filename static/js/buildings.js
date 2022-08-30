var Url = window.location.href;
$(document).ready(function(){ 
    function getBuildinds(){
        var url = `${Url}core/api/test-building/`;

        $.ajax({
            url: url,
            type: "GET",
            dataType: "json",
            success: function (data) {
                console.log(data);
                craeteBuildingTable(data)
            },
            error: function (error) {
                console.log(`Error ${error}`);
            }
        });
        
    }
    getBuildinds()
    function craeteBuildingTable(data){
        item=''
        for (var i in data) {
            i = parseInt(i);
           
            row = data[i]
            item += ` <tr>`
                    + `<th>${i+1}</th>`
                    + `<td>${row.name}</td>`
                    + `<td>${row.code}</td>`
                    + `<td>${row.city}</td>`
                    + `<td>${row.state}</td>`
                    + `<td>${row.country}</td>`
                    + `<td>${row.zip}</td>`
                    + `<td>${row.status}</td>`
                    + `<td>`
                    + `<a  class="btn btn-sm btn-info" href="#" >View Details</a>`
                    + `</td>`
                    + `</tr>`
        }
        var wrapper = document.getElementById("table-body");
        wrapper.innerHTML = "";
        wrapper.innerHTML += item;
    }

    
}) 
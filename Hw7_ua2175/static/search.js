
function print_results(names){
        $.each(names, function(index, item){
                let newRow = $("<div class='row clickdiv' " + "data-name='" + item["title"] + "'>")
                let newLink = $("<a class='no_underline' href='http://127.0.0.1:5000/view/" + item["id"] + "'>")
                newRow.append(newLink)
                newLink.html(item["title"])
                $("#searches").append(newRow)
        })
}

$(document).ready(function(){
        /*console.log("In search.js")
        console.log(results)
        console.log(query)
        console.log(num_results)*/

        $("#searches").empty()
        $("#ipaperheading").html("Search results for \"" + query + "\"")
        if(parseInt(num_results) == 0){
                $("#searches").html("No results found.")
                /*console.log("Worked")
                console.log(parseInt(num_results))*/
        }
        else{
                print_results(results)
        }
})
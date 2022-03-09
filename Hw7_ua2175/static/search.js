
function print_results(names){
        $.each(names, function(index, item){
                /*let newRow = $("<div class='row clickdiv' " + "data-name='" + item["title"] + "'>")
                let newLink = $("<a class='no_underline' href='http://127.0.0.1:5000/view/" + item["id"] + "'>")
                newRow.append(newLink)
                newLink.html(item["title"])
                $("#searches").append(newRow)*/

                let newRow = $("<div class='row homerow'>")
                let col1 = $("<div class='col-md-3 rowtitle'>")
                col1.html(item["title"])

                let col2 = $("<div class='col-md-6'>")
                col2.html(item["text"])

                let col3 = $("<div class='col-md-3'>")
                let clickableImg = $("<a href='http://127.0.0.1:5000/view/" + item["id"] + "'><img class='imglink' src='" + item["image"] + "' alt='picture of" + item["title"] + "'></a>")
                col3.append(clickableImg)

                newRow.append(col1)
                newRow.append(col2)
                newRow.append(col3)
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
                $("#searches").html("No matches found.")
                /*console.log("Worked")
                console.log(parseInt(num_results))*/
        }
        else{
                let numResultsText = $("<div class='numresults'>")
                numResultsText.html(num_results + " found")
                $("#ipaperheading").append(numResultsText)
                print_results(results)
        }
})
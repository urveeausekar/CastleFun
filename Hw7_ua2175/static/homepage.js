
function print_most_popular_of_the_week(names){
        $.each(names, function(index, item){
                /*let newRow = $("<div class='row clickdiv' " + "data-name='" + item["title"] + "'>")
                let newLink = $("<a class='no_underline' href='http://127.0.0.1:5000/view/" + item["id"] + "'>")
                newRow.append(newLink)
                newLink.html(item["title"])
                $("#popular_week").append(newRow)*/

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
                $("#popular_week").append(newRow)

        })
}

$(document).ready(function(){
        /*console.log("Hello from homepage!")
        console.log(most_popular)*/
        print_most_popular_of_the_week(most_popular)

})
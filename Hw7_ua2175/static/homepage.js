
function print_most_popular_of_the_week(names){
        $.each(names, function(index, item){
                let newRow = $("<div class='row clickdiv' " + "data-name='" + item["title"] + "'>")
                let newLink = $("<a class='no_underline' href='http://127.0.0.1:5000/view/" + item["id"] + "'>")
                newRow.append(newLink)
                newLink.html(item["title"])
                $("#popular_week").append(newRow)
        })
}

$(document).ready(function(){
        /*console.log("Hello from homepage!")
        console.log(most_popular)*/
        print_most_popular_of_the_week(most_popular)

})

function print_most_popular_of_the_week(names){
        $.each(names, function(index, item){
                /*let newRow = $("<div class='row clickdiv' " + "data-name='" + item["title"] + "'>")
                let newLink = $("<a class='no_underline' href='http://127.0.0.1:5000/view/" + item["id"] + "'>")
                newRow.append(newLink)
                newLink.html(item["title"])
                $("#popular_week").append(newRow)*/

                let newRow = $("<div class='row homerow'>")


                let col3 = $("<div class='col-md-4'>")
                let clickableImg = $("<a href='http://127.0.0.1:5000/view/" + item["id"] + "'><img class='imglink' src='" + item["image"] + "' alt='picture of" + item["title"] + "'></a>")
                col3.append(clickableImg)

                let col1 = $("<div class='col-md-8'>")
                let titlediv = $("<div class='titlediv'>")
                titlediv.html(item["title"])
                col1.append(titlediv)

                

                let col2 = $("<div class='contentdiv'>")
                col2.html(item["text"])
                col1.append(col2)

                /*let nrow = $("<div class='row'>")
                let ncol1 = $("<div class='col-md-6'>")
                let ncol2 = $("<div class='col-md-6'>")

                let genrearray = item["genres"]
                let genrelist = $("<ul>")
                $.each(genrearray, function(i, genreitem){
                        let newlistitem = $("<li>")
                        newlistitem.html(genreitem)
                        genrelist.append(newlistitem)
                })
                ncol1.append(genrelist)
                nrow.append(ncol1)
                col1.append(nrow)

                
                /*let poparray = item["pop"]
                let poplist = $("<ul>")
                $.each(poparray, function(i, popitem){
                        let newlistitem = $("<li>")
                        newlistitem.html(popitem)
                        poplist.append(newlistitem)
                })
                ncol2.append(poplist)
                nrow.append(ncol2)*/
                

                
                newRow.append(col3)
                newRow.append(col1)
                $("#popular_week").append(newRow)

        })
}

$(document).ready(function(){
        /*console.log("Hello from homepage!")
        console.log(most_popular)*/
        print_most_popular_of_the_week(most_popular)

})

function print_titles(names){
        let title = ""
        $.each(names, function(index, item){

                let newRow = $("<div class='row homerow'>")
                let col1 = $("<div class='col-md-3 rowtitle'>")
                let ltitle = item["title"].toLowerCase()
                if(ltitle.includes(lquery)){
                        let position = ltitle.indexOf(lquery)
                        title = item["title"].slice(0, position) + "<span class='highlight'>" + item["title"].slice(position, position + lquery.length) + "</span>" + item["title"].slice(position + lquery.length)
                }
                col1.html(title)

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

function print_pop(names){
        let newpopitem = ""
        $.each(names, function(index, item){
                let newRow = $("<div class='row homerow'>")
                let col1 = $("<div class='col-md-3 rowtitle'>")
                col1.html(item["title"])

                let col2 = $("<div class='col-md-3'>")
                let poparray = item["pop"]
                let poplist = $("<ul>")
                $.each(poparray, function(i, popitem){
                        let newlistitem = $("<li>")
                        let lpopitem = popitem.toLowerCase()
                        if(lpopitem.includes(lquery)){
                                let position = lpopitem.indexOf(lquery)
                                newpopitem = popitem.slice(0, position) + "<span class='highlight'>" + popitem.slice(position, position + lquery.length) + "</span>" + popitem.slice(position + lquery.length)
                        }
                        else{
                                newpopitem = popitem
                        }
                        newlistitem.html(newpopitem)
                        poplist.append(newlistitem)
                })
                col2.append(poplist)

                let col25 = $("<div class='col-md-3'>")
                let genrearray = item["genres"]
                let genrelist = $("<ul>")
                $.each(genrearray, function(i, genreitem){
                        let newlistitem = $("<li>")
                        newlistitem.html(genreitem)
                        genrelist.append(newlistitem)
                })
                col25.append(genrelist)

                let col3 = $("<div class='col-md-3'>")
                let clickableImg = $("<a href='http://127.0.0.1:5000/view/" + item["id"] + "'><img class='imglink' src='" + item["image"] + "' alt='picture of" + item["title"] + "'></a>")
                col3.append(clickableImg)

                newRow.append(col1)
                newRow.append(col2)
                newRow.append(col25)
                newRow.append(col3)
                $("#searches").append(newRow)
        })
}

function print_genres(names){
        let newgitem = ""
        $.each(names, function(index, item){
                let newRow = $("<div class='row homerow'>")
                let col1 = $("<div class='col-md-3 rowtitle'>")
                col1.html(item["title"])

                let col15 = $("<div class='col-md-3'>")
                let poparray = item["pop"]
                let poplist = $("<ul>")
                $.each(poparray, function(i, popitem){
                        let newlistitem = $("<li>")
                        newlistitem.html(popitem)
                        poplist.append(newlistitem)
                })
                col15.append(poplist)

                let col2 = $("<div class='col-md-3'>")
                let genrearray = item["genres"]
                let genrelist = $("<ul>")
                $.each(genrearray, function(i, genreitem){
                        let newlistitem = $("<li>")
                        let lgitem = genreitem.toLowerCase()
                        if(lgitem.includes(lquery)){
                                let position = lgitem.indexOf(lquery)
                                newgitem = genreitem.slice(0, position) + "<span class='highlight'>" + genreitem.slice(position, position + lquery.length) + "</span>" + genreitem.slice(position + lquery.length)
                        }
                        else{
                                newgitem = genreitem
                        }
                        newlistitem.html(newgitem)
                        genrelist.append(newlistitem)
                })
                col2.append(genrelist)

                let col3 = $("<div class='col-md-3'>")
                let clickableImg = $("<a href='http://127.0.0.1:5000/view/" + item["id"] + "'><img class='imglink' src='" + item["image"] + "' alt='picture of" + item["title"] + "'></a>")
                col3.append(clickableImg)

                newRow.append(col1)
                newRow.append(col15)
                newRow.append(col2)
                newRow.append(col3)
                $("#searches").append(newRow)
        })
}

$(document).ready(function(){
        console.log("In search.js")
        console.log(title_results)
        console.log(pop_results)
        console.log(genre_results)
        console.log(query)
        console.log(num_results)

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

                let titleheading = $("<div class='foundsectionheading'>")
                titleheading.html = ("Found in \"Titles\"")
                $("#searches").append(titleheading)
                print_titles(title_results)

                let popheading = $("<div class='foundsectionheading'>")
                popheading.html("Found in \"Popular Trivia\"")
                $("#searches").append(popheading)
                print_pop(pop_results)

                let genreheading = $("<div class='foundsectionheading'>")
                genreheading.html("Found in \"Genre\"")
                $("#searches").append(genreheading)
                print_genres(genre_results)
        }
})
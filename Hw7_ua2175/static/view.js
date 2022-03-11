
/*function display_data(item){
        let imgDiv = $("<div class='image'>")
        let img = $("<img src='" + item["image"] +"' width='800' height='500'>")
        imgDiv.append(img)
        $("#alldata").append(imgDiv)

        let yearDiv = $("<div class='year paddata'>")
        yearDiv.html("Year of Construction : " + item["year"])
        $("#alldata").append(yearDiv)

        let summaryDiv = $("<div class='summary paddata'>")
        summaryDiv.html(item["summary"])
        $("#alldata").append(summaryDiv)

        let countryDiv = $("<div class='country paddata'>")
        countryDiv.html("Location : " + item["country"])
        $("#alldata").append(countryDiv)

        let keyheading = $("<div class='keyheading paddata'>")
        keyheading.html("Keywords : ")
        $("#alldata").append(keyheading)

        let keyWords = $("<div id='ikeywords' class='keywords'><ul>")
        $.each(item["genres"], function(i, element){
                let listitem = $("<li class='listitem'>")
                listitem.html(element)
                keyWords.append(listitem)
        })
        $("#alldata").append(keyWords)
} */

$(document).ready(function(){
        console.log(data)

        $("#edit").click(function(){
                window.location.href = '/edit/' + data["id"]
        })

        /*$("#heading").html(data["title"])*/
        /*display_data(data)*/
})


function send_new_castle(data, id){
        $.ajax({
                type: "POST",
                url: "http://127.0.0.1:5000/edit_data/" + id.toString(),
                dataType: "text",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(data),
                success: function(result){
                        /*var id = result["id"]
                        let successmsg = $("<span>New item successfully submitted! View it </span>")
                        let link = $("<a href='/view/" + id + "'>Here</a>")
                        successmsg.append(link)
                        $("#successmsg").append(successmsg)

                        $("#ititle").val('')
                        $("#iimgl").val('')
                        $("#iyear").val('')
                        $("#icountry").val('')
                        $("#isummary").val('')
                        $("#ipop").val('')
                        $("#igenre").val('')
                        $("#irating").val('')
                        $("#itime").val('')
                        $("#ioneline").val('')

                        $("#ititle").focus()*/
                        console.log("Back in ajax success")
                        window.location.href = "http://127.0.0.1:5000/view/" + id.toString();
                        console.log("After trying to redirect")


                        
                },
                error: function(request, status, error){
                        console.log("Error")
                        console.log(request)
                        console.log(status)
                        console.log(error)
                }
        });
}


function load_existing_info(item){
        $("#ititle").val(item["title"])
        $("#iimgl").val(item["image"])
        $("#iyear").val(item["year"])
        $("#icountry").val(item["country"])
        $("#isummary").val(item["summary"])
        $("#ipop").val(item["pop"])
        $("#igenre").val(item["genres"])
        $("#irating").val(item["rating"])
        $("#itime").val(item["time"])
        $("#ioneline").val(item["text"])
}

$(document).ready(function(){
        load_existing_info(data)

        $("#submit").click(function(){
                console.log("Submit pressed")
                let focusdone = 0
                let errcount = 0
                
                let title = $("#ititle").val().trim()
                let imgl = $("#iimgl").val().trim()
                let year = $("#iyear").val().trim()
                let country = $("#icountry").val().trim()
                let summary = $("#isummary").val().trim()
                let pop = $("#ipop").val().trim()
                let genre = $("#igenre").val().trim()
                let rating = $("#irating").val().trim()
                let time = $("#itime").val().trim()
                let oneline = $("#ioneline").val().trim()

                if(title == ''){
                        errcount = errcount + 1
                        $("#errtitle").html("Title field cannot be left blank!")
                        if(focusdone == 0){
                                focusdone = 1
                                $("#ititle").focus()
                        }
                }
                else
                        $("#errtitle").html('')

                if(imgl == ''){
                        errcount = errcount + 1
                        $("#errimgl").html("Image link field cannot be left blank!")
                        if(focusdone == 0){
                                focusdone = 1
                                $("#iimgl").focus()
                        }
                }
                else
                        $("#errimgl").html("")


                if(year == ''){
                        errcount = errcount + 1
                        $("#erryear").html("Year field cannot be left blank!")
                        if(focusdone == 0){
                                focusdone = 1
                                $("#iyear").focus()
                        }
                }
                else if($.isNumeric(year) == false){
                        errcount = errcount + 1
                        $("#erryear").html("Year must be a number!")
                        if(focusdone == 0){
                                focusdone = 1
                                $("#iyear").focus()
                        }
                }
                else
                        $("#erryear").html("")


                if(country == ''){
                        errcount = errcount + 1
                        $("#errcountry").html("Country field cannot be left blank!")
                        if(focusdone == 0){
                                focusdone = 1
                                $("#icountry").focus()
                        }
                }
                else
                        $("#errcountry").html("")


                if(summary == ''){
                        errcount = errcount + 1
                        $("#errsummary").html("Summary field cannot be left blank!")
                        if(focusdone == 0){
                                focusdone = 1
                                $("#isummary").focus()
                        }
                }
                else
                        $("#errsummary").html("")



                if(pop == ''){
                        errcount = errcount + 1
                        $("#errpop").html("Popular trivia field cannot be left blank!")
                        if(focusdone == 0){
                                focusdone = 1
                                $("#ipop").focus()
                        }
                }
                else
                        $("#errpop").html("")


                if(genre == ''){
                        errcount = errcount + 1
                        $("#errgenre").html("Genre field cannot be left blank!")
                        if(focusdone == 0){
                                focusdone = 1
                                $("#igenre").focus()
                        }
                }
                else
                        $("#errgenre").html("")


                if(rating == ''){
                        errcount = errcount + 1
                        $("#errrating").html("Rating field cannot be left blank!")
                        if(focusdone == 0){
                                focusdone = 1
                                $("#irating").focus()
                        }
                }
                else
                        $("#errrating").html("")


                if(time == ''){
                        errcount = errcount + 1
                        $("#errtime").html("Timing field cannot be left blank!")
                        if(focusdone == 0){
                                focusdone = 1
                                $("#itime").focus()
                        }
                }
                else
                        $("#errtime").html("")



                if(oneline == ''){
                        errcount = errcount + 1
                        $("#erroneline").html("This field cannot be left blank!")
                        if(focusdone == 0){
                                focusdone = 1
                                $("#ioneline").focus()
                        }
                }
                else
                        $("#erroneline").html("")

                let id = parseInt(data["id"]);
                console.log(id)

                if(errcount == 0){
                        // make AJAX call
                        newData = {
                                "title": title,
                                "name" : title,
                                "image": imgl,
                                "year": year,
                                "country": country,
                                "summary": summary,
                                "genres": genre,
                                "pop" : pop,
                                "rating" : rating,
                                "time" : time,
                                "text" : oneline
                        }

                        send_new_castle(newData, id)
                }
        })

        $("#discard").click(function(){
                console.log("Discard clicked")
                let id = parseInt(data["id"]);
                window.location.href = "http://127.0.0.1:5000/view/" + id.toString();
        })

})
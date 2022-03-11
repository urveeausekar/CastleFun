
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
})
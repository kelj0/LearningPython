function remove(filename){
    console.log("TEST")
    $.ajax({
        type: "POST",
        url: '/remove',
        data: {filename:filename},
        success: function(){
            setTimeout(function(){location.reload();},1)
        }
      });
}
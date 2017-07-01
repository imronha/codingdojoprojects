var pokemon = "";
for(var i=1; i<152; i++){
    pokemon += '<img id='+i+' src="http://pokeapi.co/media/img/'+i+'.png">'
}
$(document).ready(function(){
    $('#pokemon').append(pokemon);

$(document).on('click','img',function(){
    $.get("http://pokeapi.co/api/v1/pokemon/"+$(this).attr('id'),function(res){
        // <img id='+i+' src="http://pokeapi.co/media/img/'+i+'.png
        var name_str = "<h1>"+res.name+"</h1>";
        $("#name").html(name_str);

        var pic_str = '<img src="http://pokeapi.co/media/img/'+res.pkdx_id+'.png">';
        $("#pic").html(pic_str);

        var type_str = "";
        type_str += "<h4>Types</h4>";
        type_str += "<ul>";
        for(var i = 0; i < res.types.length; i++) {
            type_str += "<li>" + res.types[i].name + "</li>";
        }
        type_str += "</ul>";
        $("#types").html(type_str);

        var height_str = "";
        height_str += "<h4>Height</h4>";
        height_str += "<ul><li>" + res.height + "</li></ul>";
        $("#height").html(height_str);

        var weight_str = "";
        weight_str += "<h4>Weight</h4>";
        weight_str += "<ul><li>" + res.weight + "</li></ul>";
        $("#weight").html(weight_str);

        console.log(res);
    }, "json");
});
});

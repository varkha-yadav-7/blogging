function openNav() 
{
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
}
function closeNav() 
{
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
}
function liked(id) 
{
    if($(`#like${id}`).html()=='Liked')
    {
        $.ajax(
        {
            type: "POST",
            url: "/unliking/",   
            data: {"csrfmiddlewaretoken":$('input[name=csrfmiddlewaretoken]').val(),"id": id},
            success: function(response)
            {
                $(`#like${id}`).html('Like');
                var p=$(`#totalL${id}`).html();
                p=p.substring(8);
                var k=parseInt(p)
                p--;
                $(`#totalL${id}`).html(`Likes : ${p}`);
            },
            error: function(){ console.log('error')}
        });
    }
    else if($(`#like${id}`).html()=='Like')
    {
        $.ajax(
        {
            type: "POST",
            url: "/liking/",   
            data: {"csrfmiddlewaretoken":$('input[name=csrfmiddlewaretoken]').val(),"id": id},
            success: function(response)
            {
                $(`#like${id}`).html('Liked');
                var p=$(`#totalL${id}`).html();
                p=p.substring(8);
                console.log(p);
                var k=parseInt(p)
                p++;
                $(`#totalL${id}`).html(`Likes : ${p}`);
            },
            error: function(){ console.log('error')}
        });
    }
}
function bookmarked(id)
{
    if($(`#book${id}`).html()=='Bookmarked')
    {
        $.ajax(
        {
            type: "POST",
            url: "/unbookmarking/",   
            data: {"csrfmiddlewaretoken":$('input[name=csrfmiddlewaretoken]').val(),"id": id},
            success: function(response){$(`#book${id}`).html('Bookmark');},
            error: function(){ console.log('error')}
        });
    }
    else if($(`#book${id}`).html()=='Bookmark')
    {
        $.ajax(
        {
            type: "POST",
            url: "/bookmarking/",   
            data: {"csrfmiddlewaretoken":$('input[name=csrfmiddlewaretoken]').val(),"id": id},
            success: function(response){$(`#book${id}`).html('Bookmarked');},
            error: function(){ console.log('error')}
        });
    }
}
function comments(id)
{
    var p=$(`#totalC${id}`).html();
    p=p.substring(11);
    console.log(p);
    var k=parseInt(p)
    p++;
    $(`#totalC${id}`).html(`Comments : ${p}`);
}
function showLikes(id)
{
    $.ajax(
    {
        type: "POST",
        url: "/likes/",   
        data: {"csrfmiddlewaretoken":$('input[name=csrfmiddlewaretoken]').val(),"id": id},
        success: function(response)
        {
            var s=response.replace('[','');
            s=s.replace(']','');
            if(s!='')
            {
                s=s.split('"').join('');
                var res=s.split(',');
                var list = document.createElement('ul');
                for (var i = 0; i < res.length; i++) 
                {
                    var item = document.createElement('li');
                    item.appendChild(document.createTextNode(res[i]));
                    list.appendChild(item);
                }
                $('#likers').html(list);
            }
            else
                $('#likers').html('No one has liked the post yet');
        },
        error: function(){ console.log('error')}
    });
}
function showComments(id)
{
    $.ajax(
    {
        type: "POST",
        url: "/comments/",   
        data: {"csrfmiddlewaretoken":$('input[name=csrfmiddlewaretoken]').val(),"id": id},
        success: function(response)
        {
            var resp=response.replace('{','');
            resp=resp.replace('}','');
            if(resp!='')
            {
                resp=resp.split('"').join('');
                var res=resp.split(',');
                var list = document.createElement('ul');
                for (var i = 0; i < res.length; i++) 
                {
                    var item = document.createElement('li');
                    item.appendChild(document.createTextNode(res[i]));
                    list.appendChild(item);
                }
                $('#commenters').html(list);
            }
            else
                $('#commenters').html('No one has commented on the post yet');
        },
        error: function(){ console.log('error')}
    });
}
function notif()
{
    $.ajax({
        type:'POST',
        url:'/notify/',
        data:{"csrfmiddlewaretoken":$('input[name=csrfmiddlewaretoken]').val()},
        success: function(response)
        {
            var s=response.replace('[','');
            s=s.replace(']','');
            if(s!="")
            {
                s=s.split('"').join('');
                var res=s.split(',');
                var list = document.createElement('ul');
                for (var i = 0; i < res.length; i++) 
                {
                    var item = document.createElement('li');
                    item.setAttribute("style","padding:5px");
                    item.appendChild(document.createTextNode(res[i]));
                    list.appendChild(item);
                }
                $('#notifylist').html(list);
                $('#nbadge').html('');
            }
            else
            {
                $('#notifylist').attr("style","text-align:center;");
                $('#notifylist').html('No new Notifications');
            }
        },
        error: function(){console.log('error');}
    });
}

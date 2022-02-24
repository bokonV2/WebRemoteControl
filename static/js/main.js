var socket = io('http://' + document.domain + ':' + location.port );
var mode = "handler" // or removeBtn
function openClouse(id) {
  console.log(id)
  var content = document.getElementById(id);
  var button = document.getElementById("b" + id);
  content.style.display = content.style.display === "none" ? 'flex' : 'none';
  button.innerHTML = button.innerHTML === "Close" ? 'Open' : 'Close';
}

function removeBtn(id) {
  console.log(id)
  var content = document.getElementById(id);
  var button = document.getElementById("r" + id);
  // content.style.display = content.style.display === "none" ? 'flex' : 'none';
  button.innerHTML = button.innerHTML === "Cancel" ? 'Remove btn' : 'Cancel';
  if (button.innerHTML === "Cancel"){
    content.style.backgroundColor = "red";
    mode = "removeBtn";
  }else{
    content.style.backgroundColor = "white";
    mode = "handler";
  }
}

function mmove(sw){
  var radio=document.getElementsByName("button");
   var len=radio.length;

  if (sw == 0) {
    for(var i=0;i<len;i++)
    {
        radio[i].disabled=true;
    }
  } else {
    for(var i=0;i<len;i++)
    {
        radio[i].disabled=false;
    }
  }
}

function kpress(sw) {
  var radio=document.getElementsByName('presses');
   var len=radio.length;

  if (sw == 0) {
    for(var i=0;i<len;i++)
    {
        radio[i].disabled=true;
    }
  } else {
    for(var i=0;i<len;i++)
    {
        radio[i].disabled=false;
    }
  }
}

function doForm(group_id, type) {
  var data = {};
  data["group_id"] = group_id;
  data["type"] = type;

  var all = document.querySelectorAll("#user_form input, #user_form textarea, #user_form select");
  for (let field of all) {
    if (field.type != "submit" && field.type != "button") {
      if (field.type=="radio" || field.type=="checkbox") {
        if (field.checked) { data[field.name] = field.value; }
      }
      else { data[field.name] = field.value; }
    }
  }

  socket.emit('addButtonOnGr', data);
  document.location.href = "/";
  console.log(data)
}

function removeGroup(id) {
  socket.emit('removeGroup', id);
  document.location.href = "/";
}

function addGroup() {
  var name = document.getElementById("name").value;
  socket.emit('addGroup', name);
  document.location.href = "/";
}

function buttonPress(id) {
  socket.emit(mode, id);
  if (mode === "removeBtn") {
    window.location.reload();
  }
}

socket.on('connect', function() {
  console.log("connect");
  var a = document.getElementById('errConnect');
  a.style.display = a.style.display === "none" ? 'block' : 'none';
});

socket.on('disconnect', function() {
  var a = document.getElementById('errConnect');
  a.style.display = a.style.display === "none" ? 'block' : 'none';
});

socket.on('reload', function(data){
  window.location.reload();
});

var socket = io('http://' + document.domain + ':' + location.port );

function openClouse(id) {
  console.log(id)
  var content = document.getElementById(id);
  var button = document.getElementById("b" + id);
  content.style.display = content.style.display === "none" ? 'flex' : 'none';
  button.innerHTML = button.innerHTML === "Close" ? 'Open' : 'Close';
}

function removeGroup(id) {
  socket.emit('removeGroup', id);
  document.location.href = "/";
}

function addButtonM(groupID, type) {
  var name = document.getElementById('name').value;
  var x = document.getElementById('x').value;
  var y = document.getElementById('y').value;
  var duration = document.getElementById('duration').value;
  var data = {name:name, x:x, y:y, duration:duration, group_id:groupID, type:type};
  socket.emit('addButtonOnGr', data);
  document.location.href = "/";
}

function addButtonK(groupID, type) {
  var name = document.getElementById('name').value;
  var text = document.getElementById('text').innerHTML;
  var data = {name:name, text:text, group_id:groupID, type:type};
  socket.emit('addButtonOnGr', data);
  document.location.href = "/";
}
function addButtonS(groupID, type) {
  var name = document.getElementById('name').value;
  var data = {name:name, group_id:groupID, type:type};
  socket.emit('addButtonOnGr', data);
  document.location.href = "/";
}

function addGroup() {
  var name = document.getElementById("name").value;
  socket.emit('addGroup', name);
  document.location.href = "/";
}

function buttonPress(id) {
  socket.emit('handler', id);
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

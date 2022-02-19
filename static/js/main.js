function openClouse(id) {
  console.log(id)
  var content = document.getElementById(id)
  var button = document.getElementById("b" + id)
  content.style.display = content.style.display === "none" ? 'flex' : 'none';
  button.innerHTML = button.innerHTML === "Close" ? 'Open' : 'Close';
}

function addButton(id) {
  document.location.href = "/addButton/" + id + "/0/0";
}

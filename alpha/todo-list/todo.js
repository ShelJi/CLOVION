const list = document.getElementById("list");
getData();

function addTask() {
    var inputValue = document.getElementsByClassName("inputBox")[0].value.trim();

    if (inputValue == '') {
        window.alert("vela vetti illana inga varadha o_o")
    }
    else {
        let newList = document.createElement("li");
        newList.textContent = inputValue;
        list.appendChild(newList);

        let close = document.createElement("span");
        close.innerHTML = "\u00d7";
        newList.appendChild(close);
        saveData();
    }
    document.getElementsByClassName("inputBox")[0].value = "";
}

list.addEventListener("click", function (e) {
    if (e.target.tagName == "LI") {
        e.target.classList.toggle("checked");
        saveData();
    }
    else if (e.target.tagName == "SPAN") {
        e.target.parentElement.remove();
        saveData();
    }
}, false);

function saveData() {
    localStorage.setItem("data", list.innerHTML);
}
function getData() {
    list.innerHTML = localStorage.getItem("data");
}
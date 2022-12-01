
function mostrar_elemento(this_, m) {
    var id2 = this_.value + "_id";

    if (document.getElementById(id2)){
        this_.removeAttribute("checked");
        var obj = document.getElementById(id2);
        parent = obj.parentNode;
        parent.removeChild(obj);
    }
    else {
        this_.setAttribute("checked", "checked");
        var obj = document.getElementById(m);
        
        var elem = document.createElement("li");
        elem.setAttribute("id", id2);
        elem.textContent = this_.value;
        obj.appendChild(elem);
    }
}

function mostrar_elemento_radio(this_, m, value) {
    var id2 = this_.value + "_id";

    if (document.getElementById(id2)) {
        this_.removeAttribute("checked");
        var obj = document.getElementById(id2);
        parent = obj.parentNode;
        parent.removeChild(obj);
    }
    else {
        this_.setAttribute("checked", "checked");
        var obj = document.getElementById(m);

        var elem = document.createElement("li");
        elem.setAttribute("id", id2);
        elem.textContent = this_.value;
        obj.appendChild(elem);
    }
}


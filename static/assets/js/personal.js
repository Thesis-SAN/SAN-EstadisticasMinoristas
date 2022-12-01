function mostrar_elemento(this_, id2, newid, value) {
    /*
    ver si el elemento con id1 esta senalado
        - SI: entonces buscar elemento con id2 y agregar hijo con id=newid y valor=value
        - NO: buscar elemento con id2, buscar elemento con id=newid si exite borrarlo
    */
    var isChecked = this_.checked;
    if (!isChecked) {
        this_.setAttribute("checked", "checked")
        var obj = document.getElementById(id2);
        if (obj) {
            var elem = document.createElement("il");
            elem.setAttribute("id", newid);
            elem.setAttribute("value", value);
            obj.appendChild(elem);
        }
    }
    else {
        // var obj = document.getElementById(id2);
        this_.removeAttribute("checked")
        var obj = document.getElementById(newid);
        if (obj) {
            parent = obj.parentNode;
            parent.removeChild(obj);
        }
    }
}

function mostrar_elemento(this_) {
    var id2 = this_.value + "_id"
    if (this_.hasOwnProperty("checked")){
        this_.removeAttribute("checked")
        var obj = document.getElementById(newid);
        if (obj) {
            parent = obj.parentNode;
            parent.removeChild(obj);
        }
    }
    else{
        this_.setAttribute("checked", "checked")
        var obj = document.getElementById(id2);
        if (obj) {
            var elem = document.createElement("il");
            elem.setAttribute("id", newid);
            elem.setAttribute("value", value);
            obj.appendChild(elem);
        }
    }
}


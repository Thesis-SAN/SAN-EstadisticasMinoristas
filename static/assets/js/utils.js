
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

function ratio_selected(this_, dest_addr){
    if (this_.hasChildNodes()) {
        var children = this_.childNodes;
        for (var i = 0; i < children.length; i++) {
            // do something with each child as children[i]
            // NOTE: List is live, adding or removing children will change the list
            if(children[i].checked){
                
            }
            else{

            }
        }
    }
}

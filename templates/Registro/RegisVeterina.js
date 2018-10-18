// JavaScript Document
function mostrarArchivo() {
    var direccion = document.getElementById('archivoImagen').value;
    var nombre = direccion.split("\\");
    document.getElementById('tituloArch').innerHTML = nombre[nombre.length - 1];
}

function iniciarCampos() {
    for (var i = 0; i < 24; i++) {
        if (i < 10) {
            document.getElementById("hora1").innerHTML += "<option value='0" + i + "'>0" + i + "</option>";
            document.getElementById("hora2").innerHTML += "<option value='0" + i + "'>0" + i + "</option>";
        } else {
            document.getElementById("hora1").innerHTML += "<option value='" + i + "'>" + i + "</option>";
            document.getElementById("hora2").innerHTML += "<option value='" + i + "'>" + i + "</option>";
        }
    }
    for (var i = 0; i < 60; i++) {
        if (i < 10) {
            document.getElementById("minu1").innerHTML += "<option value='0" + i + "'>0" + i + "</option>";
            document.getElementById("minu2").innerHTML += "<option value='0" + i + "'>0" + i + "</option>";
        } else {
            document.getElementById("minu1").innerHTML += "<option value='" + i + "'>" + i + "</option>";
            document.getElementById("minu2").innerHTML += "<option value='" + i + "'>" + i + "</option>";
        }
    }
}

function agregarServicio() {
    document.getElementById("hora1").innerHTML += "<option value='0" + i + "'>0" + i + "</option>";
}
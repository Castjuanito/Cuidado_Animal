// JavaScript Document
function mostrarArchivo() {
    var direccion = document.getElementById('archivoImagen').value;
    var nombre = direccion.split("\\");
    document.getElementById('tituloArch').innerHTML = nombre[nombre.length - 1];
}
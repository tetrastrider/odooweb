/* const port = 4000;
const http = require('http'); */
/* const colors = require('color'); */
//const colors = require('colors/safe');
/* const handleServer = (req,res)=>{
    res.writeHead(200,{'context-type':'text/html'});
    res.write('<h1>hola</h1>');
    res.end();
}

const server = http.createServer(handleServer);
server.listen(port,()=>{console.log('servidor en el puerto ',port);}); */
//console.log(colors.green('hello'));
//console.log('hello'.green);

//npm init //crea un manifest typo json
//npm install //instala el proyecto con todas sus dependencias
//npm -g express//crea un proyecto express
//
//npm install -g @angular/cli //generador de proyectos angularc
//ng new proyecto
//ng serve
//ng generate component nombre
//ng genrate service nombre
//EXPRESS EDITION
const express = require('express');
const server = express();
server.get('/',(req,res)=>{
    res.send('<h1>hola</h1>');
    res.end();
});
server.listen(4000,()=>{
    console.log('servidor en puerto 300')
    console.log(__dirname)
    console.log(__filename)
});

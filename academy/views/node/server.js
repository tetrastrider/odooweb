/* import saludo from './modulo';
import mat from './newmodule'; */
/* const saludo = require('./modulo')
const math = require('./newmodule') */
/* const file = require('./file') */
/*math.set(5,5)
math.add() */

/* const fs = require('fs'); */
/* fs.writeFile('./server.log','dimelo',(error)=>{
    if(error){console.log('no se pudo crear el archivo')}
    console.log('archivo creado')
}) */
/* fs.readFile('./server.log',(error,data)=>{
    if(error){console.log('error')}
    console.log(data.toString())
}) */
const http = require('http');
http.createServer((req,res)=>{
    res.writeHead(200,{'context-type':'text/html'});
    res.write('<h1>pagiina en node js</h1>');
    res.end()
}).listen(4000)//crtl+c 2 veces cancela el servidor
const file = require('fs');
fs.writeFile('./server.log',function(error){
    if(error){console.log('no se pudo crear el archivo')}
    console.log('archivo creado')
})
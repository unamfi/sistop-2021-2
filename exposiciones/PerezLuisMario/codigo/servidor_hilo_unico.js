const http = require('http');

const PORT = 5000;

const server = http.createServer((request, response) => {
    console.log(`Procesando solicitud en proceso: ${process.pid}`)
    setTimeout(() => {
        response.writeHead(200, {'Content-Type': 'text/plain'})
        response.end('Succesful Request!');
    }, Math.random() * 6 * 1000);
});

server.listen(PORT, () => console.log(`> Listening on port ${PORT}`));
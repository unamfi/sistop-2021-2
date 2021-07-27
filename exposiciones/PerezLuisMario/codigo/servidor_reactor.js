const http = require('http');

const PORT = 5000;

const server = http.createServer((request, response) => {
    const chunks = [];
    request.setEncoding('utf-8');
    // Notar que los callbacks se dan en
    // un orden poco ortodoxo. Pero esto no
    // representa ningún problema.
    request.on('error', err => {
        console.error('Error: \n', err);
        response.writeHead(500)
        response.end();
    });
    request.on('end', () => {
        console.log('Received', chunks.join(''));
        response.writeHead(200);
        // Echo-o-o !!
        response.end(chunks.join(''));
    });
    request.on('data', chunk => {
        chunks.push(chunk);
    });
});

server.listen(PORT, () => console.log(`> Listening on port ${PORT}`));
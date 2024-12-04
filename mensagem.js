const express = require('express');
const app = express();
const port = 3000;

app.get('/api', (req, res) => {
    res.json({ mensagem: 'esse é minha api rest' });
});

app.listen(port, () => {
    console.log(`Servidor rodando em:${port}`);
});

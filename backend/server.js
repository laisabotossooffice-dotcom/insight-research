const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json());

// Simulação de base de dados de indicadores
const indicadores = {
    projeto: "InsightResearch",
    status: "Operacional",
    kpis: { eficienca: "94%", qualidade: "98.5%" }
};

// Rota de Health Check
app.get('/health', (req, res) => res.status(200).send('API Ativa'));

// Rota Principal (CRUD - Read)
app.get('/api/dashboard', (req, res) => {
    try {
        res.status(200).json(indicadores);
    } catch (error) {
        res.status(500).json({ error: "Erro interno no servidor" });
    }
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => console.log(`🚀 Server sênior rodando na porta ${PORT}`));
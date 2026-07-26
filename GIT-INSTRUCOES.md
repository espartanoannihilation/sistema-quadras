# Arena Manager — Teresina PI (Vôlei & Beach Tennis)

## Dados do Espaço (tudo visível, nada oculto)

- **Nome:** Arena Sport Teresina
- **Endereço:** Av. Joaquim Nabuco, 1450 — Jardim Aurora, Teresina-PI
- **Horário:** Seg a Sex 05h–23h | Sáb e Dom 06h–22h
- **WhatsApp:** 86994733462
- **Pix:** 06164531322
- **Atendimento humano:** Seg a Sex 08h–18h | Sáb 09h–13h

## Arquivos do Projeto

### Código (frontend)
- `src/App.tsx` — aplicação principal
- `src/components/` — Hero, Services, Portfolio, Process, Contact, Navbar, Assistant, etc.
- `src/lib/space.ts` — dados do espaço, reservas, regras

### Scripts (automação / reserva / sistema)
- `scripts/reserva.sh` — Bash simples (dia + hora + quadra)
- `scripts/reserva.py` — Python (argumentos --dia --hora --quadra)
- `scripts/reserva.ps1` — PowerShell
- `scripts/automacao.py` / `.bat` — automação completa (--auto)
- `scripts/sistema_que_marca.py` / `.bat` — o próprio sistema marca

### Configurações ocultas (para modificação por IA)
- `arena_config.json` / `.py`
- `arena_core.json`
- `dados_espaco.json`

### Páginas de reserva diretas (tudo visível)
- `public/reserva-direta.html` — seleção de dia/hora + WhatsApp + Pix
- `public/whatsapp-conector.html` — conector direto
- `public/whatsapp-guia.html` — guia completo de automação

## Como subir no GitHub

1. Crie um repositório novo em github.com
2. Copie TODOS os arquivos desta pasta (exceto `node_modules/`, `dist/`, `.vercel/`)
3. Execute localmente:
```bash
git init
git add .
git commit -m "Arena Manager - Teresina PI - Reserva direta WhatsApp + Pix"
git remote add origin https://github.com/SEU-USUARIO/arena-manager.git
git push -u origin main
```

Não preciso de acesso ao GitHub — apenas mande os arquivos para o repositório. Tudo está aqui.

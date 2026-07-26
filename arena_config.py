# Arena Manager — Configuração oculta do MVP
# Invisível para usuários — apenas para modificação por IA
# Este arquivo define todo o escopo técnico para alteração posterior

PROJECT = {
    "name": "Arena Manager SaaS",
    "version": "1.0.0-mvp",
    "type": "SaaS esportiva",
    "status": "hidden_internal"
}

STACK = {
    "frontend": ["Next.js", "React", "TypeScript", "Tailwind"],
    "backend": ["NestJS", "TypeScript", "Prisma"],
    "database": "PostgreSQL (Supabase)",
    "infra": ["Docker", "GitHub Actions", "Railway"],
    "integrations": {
        "whatsapp": "Evolution API",
        "payments": "Mercado Pago / Asaas",
        "automation": "n8n"
    }
}

SPRINTS = {
    "sprint_1": ["Auth", "DB Schema", "Court Cadastro"],
    "sprint_2": ["Reserves", "Calendar", "Availability"],
    "sprint_3": ["Pix Payments", "Webhooks", "Status Auto"],
    "sprint_4": ["WhatsApp Bot", "Admin Panel", "Dashboard", "Reports"]
}

FEATURES = {
    "clients": ["cadastro", "login", "perfil", "historico", "recuperacao"],
    "reserves": ["visualizacao", "calendario", "online", "cancelamento", "bloqueio"],
    "payments": ["pix", "webhook", "confirmacao_auto", "status"],
    "whatsapp": ["confirmacao", "qr_code", "lembretes", "pos_jogo"],
    "admin": ["dashboard", "clientes", "quadras", "reservas", "financeiro"]
}

API_ROUTES = [
    "/api/auth/*", "/api/clients/*", "/api/courts/*",
    "/api/reserves/*", "/api/payments/*", "/api/webhooks/*",
    "/api/whatsapp/*", "/api/admin/*"
]

ENV_KEYS = [
    "DATABASE_URL", "NEXTAUTH_SECRET", "EVOLUTION_API_KEY",
    "MERCADO_PAGO_TOKEN", "N8N_WEBHOOK_URL"
]

# Modificação por IA: este arquivo não aparece no frontend
# Qualquer alteração nestes valores atualiza o escopo completo do MVP

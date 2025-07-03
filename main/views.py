from django.shortcuts import render
from django.contrib import messages
from .models import Contato

def home(request):
    return render(request, 'home.html')





def projetos(request):
    projetos = [
        {
            'titulo': 'Controle de Instrutores',
            'descricao': 'Sistema para autoescola com controle de entrada/saída, leitura de placa e impressão de tickets.',
            'tecnologias': ['Django', 'SQLite', 'Bootstrap', 'Tailwind', 'Postgres'],
            'imagem': '/static/img/controle_instrutores.JPG',  # opcional
            'seguranca': 'Acesso restrito via login, proteção CSRF, e integração futura com câmera de segurança.',
            'link': 'https://github.com/tiagomiranda/controle-instrutores'
        },
        {
            'titulo': 'Checklist Farmácia',
            'descricao': 'Aplicativo desktop com interface Tkinter para checklist de farmácia, exportação em PDF e geração de relatórios.',
            'tecnologias': ['Python', 'Tkinter', 'ReportLab'],
            'imagem': '/static/img/farmacia.png',  # quando quiser, adicione aqui
            'seguranca': 'Validação de campos e bloqueio de alterações indevidas no histórico.',
            'link': 'https://github.com/tiagomiranda/checklist-farmacia'
        },
        {
            'titulo': 'Consulta Tabela Fipe',
            'descricao': 'Sistema simples para consultar valores atualizados de veículos via API pública da Fipe.',
            'tecnologias': ['Python', 'Requests', 'API REST'],
            'imagem': '/static/img/fipe.png',
            'seguranca': 'Consumo seguro de API com tratamento de erros e dados validados no frontend.',
            'link': 'https://github.com/tiagomiranda/fipe-api'
        },
        {
            'titulo': 'Controle Financeiro de Casais',
            'descricao': 'Sistema completo de gestão financeira para casais com múltiplos usuários, controle de receitas, despesas, categorias, metas, gráficos e histórico completo com filtros.',
            'tecnologias': ['Django', 'Python', 'SQLite', 'Chart.js', 'Bootstrap'],
            'imagem': '/static/img/financas_casais.png',  # pode deixar vazio por enquanto
            'seguranca': 'Login individual com autenticação, dados protegidos por sessão, validações contra manipulação de dados e organização por usuário.',
            'link': 'https://github.com/tiagomiranda/financas-casais'  # ajuste conforme seu GitHub
        }

    ]
    return render(request, 'projetos.html', {'projetos': projetos})






def contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')

        Contato.objects.create(nome=nome, email=email, mensagem=mensagem)
        messages.success(request, 'Mensagem enviada com sucesso!')

    return render(request, 'contato.html')



from django.shortcuts import render

def sobre(request):
    return render(request, 'sobre.html')




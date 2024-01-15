from django.shortcuts import render, redirect,  get_object_or_404
from django.core.mail import send_mail
from app_personal_website.models import Project, ProjectImage

def homepage(request):
    projects = Project.objects.all()
    return render(request, 'homepage.html', {'projects': projects})

def about(request):

    return render(request, 'about.html')

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        titulo = request.POST.get('titulo')
        mensagem = request.POST.get('mensagem')

        # Verifica se está capturando os dados corretamente
        print(nome, email, titulo, mensagem)

        # Configurar e enviar o email
        send_mail(
            f'{titulo} - Enviado por: {nome}',  # Assunto do email
            f'De: {email}\n\n{mensagem}',  # Corpo da mensagem
            'seu_email@exemplo.com',  # Email do remetente
            ['leony.ferreira95@gmail.com'],  # Lista de destinatários
            fail_silently=False,
        )

        # Redirecionar após o envio do email
        return redirect('homepage')
    return render(request, 'contact.html')


def admin_panel(request):
    return render(request, 'admin-panel.html')

def new_project(request):
    if request.method == 'POST':
        project_title = request.POST.get('project_title')
        project_tags = request.POST.get('project_tags')
        project_description = request.POST.get('project_description')

        # Crie um novo projeto
        project = Project.objects.create(
            project_title=project_title,
            project_tags=project_tags,
            project_description=project_description
        )

        # Processar as imagens
        for image in request.FILES.getlist('images'):
            project_image = ProjectImage(project_image=image)
            project_image.save()
            project.project_images.add(project_image)

        return redirect('project_list')  # Substitua 'projects' pelo nome correto da sua URL

    return render(request, 'new-project.html')


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'project_detail.html', {'project': project})


def edit_project(request):
    return render(request, 'edit-project.html')

def delete_project(request):
    return render(request, 'delete-project.html')
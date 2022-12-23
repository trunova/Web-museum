from django.shortcuts import render
from django.views import View
from django.core.handlers.wsgi import WSGIRequest
from gallery.models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class MuseumView(View):
    def get(self, request: WSGIRequest):
        context = {}
        pieces = Museum_piece.objects.all()
        exhibitions = Exhibition.objects.all()
        authors = Author.objects.all()
        images = Images.objects.all()
        exhibition_museum_pieces = Exhibition_museum_piece.objects.all()
        exhibition_images = []
        for exhibition in exhibitions:
            f = False
            for exhibition_piece in exhibition_museum_pieces:
                if exhibition.id == exhibition_piece.exhibition_id.id:
                    f = True
                    for image in images:
                        if image.piece == exhibition_piece.museum_piece_id:
                            exhibition_images.append((exhibition, image))
                            break
                    break
            if not f:
                exhibition_images.append((exhibition, None))
        pieces_images = []
        for piece in pieces:
            f = False
            for image in images:
                if image.piece == piece:
                    f = True
                    pieces_images.append((piece, image))
                    break
            if not f:
                pieces_images.append((piece, None))
        context['pieces_images'] = pieces_images
        context['authors'] = authors
        context['images'] = images
        context['exhibition_images'] = exhibition_images
        return render(request, 'gallery/museum.html', context)


    def post(self, request: WSGIRequest):
        context = {}
        if request.POST.get('add_exhibition'):
            return HttpResponseRedirect("/gallery/add_exhibition/")
        if request.POST.get('add_museum_piece'):
            return HttpResponseRedirect("/gallery/add_museum_piece/")
        if request.POST.get('add_author'):
            return HttpResponseRedirect("/gallery/add_author/")
        return render(request, 'gallery/museum.html', context)


class AddExhibition(View):
    def get(self, request: WSGIRequest):
        form = ExhibitionForm()
        form_ex_piece = Exhibition_museum_pieceForm()
        context = {}
        form_ex_piece.fields['museum_piece_id'].queryset = Museum_piece.objects.all()
        context['form'] = form
        context['form_ex_piece'] = form_ex_piece
        return render(request, 'gallery/add_exhibition.html', context)

    def post(self, request: WSGIRequest):
        form = ExhibitionForm(request.POST)
        form_ex_piece = Exhibition_museum_pieceForm(request.POST)
        context = {}
        if form.is_valid():
            f = Exhibition(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                date_and_time=form.cleaned_data.get('date_and_time')
            )
            f.save()
            if form_ex_piece.is_valid():
                ex_piece = Exhibition_museum_piece(
                    exhibition_id=f,
                    museum_piece_id=form_ex_piece.cleaned_data.get('museum_piece_id')
                )
                ex_piece.save()
            return HttpResponseRedirect("/gallery/")
        context['form'] = form
        return render(request, 'gallery/add_exhibition.html', context)


class AddMuseumPiece(View):
    def get(self, request: WSGIRequest):
        form = Museum_pieceForm()
        form_images = ImagesForm()
        form.fields['author_id'].queryset = Author.objects.all()
        form.fields['hall_id'].queryset = Hall.objects.all()
        context = {}
        context['form'] = form
        context['form_images'] = form_images
        return render(request, 'gallery/add_museum_piece.html', context)

    def post(self, request: WSGIRequest):
        form = Museum_pieceForm(request.POST)
        form_images = ImagesForm(request.POST, request.FILES)
        context = {}
        if form.is_valid():
            piece = Museum_piece(
                piece_name=form.cleaned_data.get('piece_name'),
                description=form.cleaned_data.get('description'),
                date_of_creation=form.cleaned_data.get('date_of_creation'),
                piece_type=form.cleaned_data.get('piece_type'),
                author_id=form.cleaned_data.get('author_id'),
                hall_id=form.cleaned_data.get('hall_id')
            )
            piece.save()
            if form_images.is_valid():
                files = request.FILES.getlist('image')
                context['files'] = files
                for file in files:
                    img = Images(
                        piece=piece,
                        image=file
                    )
                    img.save()
            return HttpResponseRedirect("/gallery/")
        context['form'] = form
        context['form_images'] = form_images
        return render(request, 'gallery/add_museum_piece.html', context)


class AddAuthor(View):
    def get(self, request: WSGIRequest):
        form = AuthorForm()
        context = {}
        context['form'] = form
        return render(request, 'gallery/add_author.html', context)

    def post(self, request: WSGIRequest):
        form = AuthorForm(request.POST)
        context = {}
        if form.is_valid():
            f = Author(full_name=form.cleaned_data.get('full_name'))
            f.save()
            return HttpResponseRedirect("/gallery/")
        context['form'] = form
        return render(request, 'gallery/add_author.html', context)


class Registration(View):
    def get(self, request: WSGIRequest):
        form = RegistrationForm()
        context = {}
        context['form'] = form
        return render(request, 'gallery/registration.html', context)

    def post(self, request: WSGIRequest):
        form = RegistrationForm(request.POST, request.FILES)
        context = {}
        if form.is_valid():
            user = form.save()
            profile = Profile(
                user=user,
                email=form.cleaned_data.get('email')
            )
            profile.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect("/gallery/")
        else:
            context['errors'] = form.errors
            form = RegistrationForm()
            user = None
        context['form'] = form
        context['user'] = user
        return render(request, 'gallery/registration.html', context)


class AboutMe(View):
    def get(self, request: WSGIRequest):
        context = {}
        context['user'] = request.user
        return render(request, 'gallery/about_me.html', context)


class Login(LoginView):
    template_name = 'gallery/authentication.html'
    form_class = LoginForm
    next_page = "../../gallery/"


class Logout(LogoutView):
    next_page = "../../gallery/"


class PieceDetailed(View):
    def get(self, request: WSGIRequest, piece_id):
        piece = Museum_piece.objects.get(id=piece_id)
        images = Images.objects.all()
        select_images = []
        for image in images:
            if image.piece.id == piece_id:
                select_images.append(image)
        context = {}
        context['piece'] = piece
        context['select_images'] = select_images
        context['piece_id'] = piece_id
        return render(request, 'gallery/detail_piece.html', context)

    def post(self, request: WSGIRequest, piece_id):
        context = {}
        context['piece_id'] = piece_id
        if request.POST.get("del_{d}".format(d=piece_id)):
            piece = Museum_piece.objects.get(id=piece_id)
            piece.delete()
            return HttpResponseRedirect("/gallery/")
        return render(request, 'gallery/detail_piece.html', context)


class PieceChange(View):
    def get(self, request: WSGIRequest, piece_id):
        piece = Museum_piece.objects.get(id=piece_id)
        images = Images.objects.all()
        select_images = []
        for image in images:
            if image.piece.id == piece_id:
                select_images.append(image)
        context = {}
        context['piece'] = piece
        context['select_images'] = select_images
        context['piece_id'] = piece_id
        form = Museum_pieceForm(instance=piece)
        if len(select_images) != 0:
            form_images = ImagesForm(instance=select_images[0])
        else: form_images = ImagesForm()
        context = {}
        context['form'] = form
        context['form_images'] = form_images
        return render(request, 'gallery/change_piece.html', context)

    def post(self, request: WSGIRequest, piece_id):
        piece = Museum_piece.objects.get(id=piece_id)
        images = Images.objects.all()
        select_images = []
        for image in images:
            if image.piece.id == piece_id:
                select_images.append(image)
        form = Museum_pieceForm(request.POST, instance=piece)
        form_images = ImagesForm(request.POST, request.FILES, instance=select_images[0])
        context = {}
        if form.is_valid():
            new_piece = form.save()
            if form_images.is_valid():
                new_img = form_images.save()
            return HttpResponseRedirect("/gallery/")
        context['form'] = form
        context['form_images'] = form_images
        return render(request, 'gallery/change_piece.html', context)


class ExhibitionDetailed(View):
    def get(self, request: WSGIRequest, exh_id):
        exhibition = Exhibition.objects.get(id=exh_id)
        exhibition_museum_pieces = Exhibition_museum_piece.objects.all()
        images = Images.objects.all()
        select_images = []
        for exhibition_piece in exhibition_museum_pieces:
            if exh_id == exhibition_piece.exhibition_id.id:
                for image in images:
                    if image.piece == exhibition_piece.museum_piece_id:
                        select_images.append(image)
                        break
                break
            else:
                select_images.append((exhibition, None))
        context = {}
        context['exhibition'] = exhibition
        context['select_images'] = select_images
        context['exh_id'] = exh_id
        return render(request, 'gallery/detail_exh.html', context)

    def post(self, request: WSGIRequest, exh_id):
        context = {}
        context['exh_id'] = exh_id
        if request.POST.get("del_{d}".format(d=exh_id)):
            exhibition = Exhibition.objects.get(id=exh_id)
            exhibition.delete()
            return HttpResponseRedirect("/gallery/")
        return render(request, 'gallery/detail_exh.html', context)


class ExhibitionChange(View):
    def get(self, request: WSGIRequest, exh_id):
        exhibition = Exhibition.objects.get(id=exh_id)
        exhibition_museum_pieces = Exhibition_museum_piece.objects.all()
        images = Images.objects.all()
        select_images = []
        for exhibition_piece in exhibition_museum_pieces:
            if exh_id == exhibition_piece.exhibition_id.id:
                for image in images:
                    if image.piece == exhibition_piece.museum_piece_id:
                        select_images.append(image)
                        break
                break
            else:
                select_images.append((exhibition, None))
        context = {}
        form = ExhibitionForm(instance=exhibition)
        form_ex_piece = Exhibition_museum_pieceForm(instance=exhibition_museum_pieces[0])
        # form_ex_piece.fields['museum_piece_id'].queryset = Museum_piece.objects.all()
        context['form'] = form
        context['form_ex_piece'] = form_ex_piece
        context['exhibition'] = exhibition
        context['select_images'] = select_images
        context['exh_id'] = exh_id
        return render(request, 'gallery/change_exhibition.html', context)

    def post(self, request: WSGIRequest, exh_id):
        exhibition = Exhibition.objects.get(id=exh_id)
        exhibition_museum_pieces = Exhibition_museum_piece.objects.all()
        images = Images.objects.all()
        select_images = []
        for exhibition_piece in exhibition_museum_pieces:
            if exh_id == exhibition_piece.exhibition_id.id:
                for image in images:
                    if image.piece == exhibition_piece.museum_piece_id:
                        select_images.append(image)
                        break
                break
            else:
                select_images.append(None)
        context = {}

        form = ExhibitionForm(request.POST, instance=exhibition)
        form_ex_piece = Exhibition_museum_pieceForm(request.POST, instance=exhibition_museum_pieces[0])

        if form.is_valid():
            context['d'] = 'ddddddd'

            new_exhibition = form.save()
            if form_ex_piece.is_valid():
                new_pices = form_ex_piece.save()
            return HttpResponseRedirect("/gallery/")
        context['form'] = form
        context['form_ex_piece'] = form_ex_piece
        return render(request, 'gallery/change_exhibition.html', context)


# class PieceDel(View):
#     def get(self, request: WSGIRequest, piece_id):
#         piece = Museum_piece.objects.get(id=piece_id)
#         images = Images.objects.all()
#         select_images = []
#         for image in images:
#             if image.piece.id == piece_id:
#                 select_images.append(image)
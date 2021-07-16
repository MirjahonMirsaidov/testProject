from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path, reverse
from django import forms

from .models import Samples, Items, Category
from .utils import write_samples_from_tsv, write_items_from_tsv


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


admin.site.register(Category)


@admin.register(Samples)
class SamplesAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_id', 'date', 'name', 'text')

    def get_urls(self):
        # adding upload tsv button-link to the admin
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == 'POST':
            csv_file = request.FILES['csv_upload']
            if not csv_file.name.endswith('.tsv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            write_samples_from_tsv(csv_file)
            # url = reverse('base.html')
            return HttpResponseRedirect('/admin/main/samples/')
        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rank', 'quantity', 'verified', 'category')

    def category(self, obj):
        # displaying all categories of item
        return [cat.name for cat in obj.categories.all()]

    def get_urls(self):
        # adding upload tsv button-link to the admin
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == 'POST':
            csv_file = request.FILES['csv_upload']
            if not csv_file.name.endswith('.tsv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            write_items_from_tsv(csv_file)
            # url = reverse('base.html')
            return HttpResponseRedirect('/admin/main/items/')
        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

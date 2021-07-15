from django.core.exceptions import ObjectDoesNotExist

from .models import Samples, Items, Category


def write_samples_from_tsv(tsv_file):
    tsv_file = tsv_file.read().decode('utf-8')
    data = tsv_file.split('\n')

    for row in data:
        fields = row.split('\t')
        try:
            id, item_id, date, name, text = fields
            if Samples.objects.filter(id=id).exists():
                sample = Samples.objects.get(id=id)
                sample.item_id = item_id
                sample.date = date
                sample.name = name
                sample.text = text
                sample.save()
            else:
                Samples.objects.create(
                    id=id,
                    item_id=item_id,
                    date=date,
                    name=name,
                    text=text
                )
        except:
            continue


def write_items_from_tsv(tsv_file):
    tsv_file = tsv_file.read().decode('utf-8')
    data = tsv_file.split('\n')

    for row in data:
        fields = row.split('\t')
        try:
            id, name, rank, quantity, verified, categories = fields
            print(fields)
            print({'id': id, 'name': name, 'rank': rank,
                   'quantity': quantity, 'verified': verified,
                   'categories': categories})
            if Items.objects.filter(id=id).exists():
                item = Items.objects.get(id=id)
                item.name = name
                item.quantity = quantity
                item.verified = verified
                item.save()
            else:
                item = Items.objects.create(
                    id=id,
                    name=name,
                    rank=rank,
                    quantity=quantity,
                    verified=verified,
                )
            categories = categories.split(';')
            for category in categories:
                if '.' in category:
                    cat, subcat = category.split('.')
                    try:
                        cat = Category.objects.get(name=cat, item=item)
                        Category.objects.create(
                            name=subcat,
                            item=item,
                            parent=cat
                        )
                    except ObjectDoesNotExist:
                        continue
                else:
                    Category.objects.create(
                        name=category,
                        item=item,
                        parent=None
                    )

        except:
            continue




